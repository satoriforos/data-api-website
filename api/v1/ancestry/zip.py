#!/usr/bin/env python3
import sys
sys.path.append("../../../")
import re
from os import environ
from settings.settings import settings
from modules.HttpServer import HttpServer
from modules.apimanager.ApiManager import ApiManager
from modules.apimanager.SubscriptionPlan import SubscriptionPlan
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.ZipCode import ZipCode
from modules.geolocation.UsState import UsState
from modules.usdemographics.AncestryCounty import AncestryCounty
from requests.utils import requote_uri
from common import eligible_headers
from common import get_is_eligible
from collections import OrderedDict

class ApiParamNoZipCodeProvidedError(Exception):
    pass


class ApiParamInvalidZipCodeError(Exception):
    pass


def get_database_connection(mysql_settings):
    database_manager = DatabaseManager(
        host=mysql_settings["server"],
        port=mysql_settings["port"],
        user=mysql_settings["username"],
        password=mysql_settings["password"],
        db=mysql_settings["schema"],
        charset=mysql_settings["charset"]
    )
    return database_manager


http_server = HttpServer(environ, sys.stdin)
database_manager = get_database_connection(settings["mysql"])
api_manager = ApiManager(http_server, database_manager)


def handle_get(http_server, database_manager, ip, account, api_key):
    query_params = http_server.get_query_parameters()
    if "zip" not in query_params:
        raise ApiParamNoZipCodeProvidedError

    raw_zip_code_string = query_params["zip"]
    zip_code_string = raw_zip_code_string
    if "-" in raw_zip_code_string:
        dash_position = raw_zip_code_string.find("-")
        zip_code_string = raw_zip_code_string[0:dash_position]

    match = re.match(r'^\d+$', zip_code_string)
    if match is None:
        raise ApiParamInvalidZipCodeError

    zip_code_int = int(zip_code_string)
    zip_code = ZipCode.fetch_by_zip_int(
        database_manager,
        zip_code_int,
        is_decommisioned=False
    )

    if zip_code is None:
        raise ApiParamInvalidZipCodeError

    state = UsState.fetch_by_id(database_manager, zip_code.state_id)
    city_name = zip_code.city
    if zip_code.city is not None:
        city_name = zip_code.city.title()

    county_percentages = zip_code.get_county_percentages()
    county_fips = []
    if len(county_percentages) > 0:
        county_fips = [c.get_state_county_fips() for c in county_percentages]
        county_fips = list(set(county_fips))

    subscription_plan = SubscriptionPlan.fetch_by_id(
        database_manager,
        account.subscription_plan_id
    )
    for header in eligible_headers:
        eligible_headers[header] = get_is_eligible(
            subscription_plan,
            header
        )

    zip_totals = {}
    if len(county_fips) > 0:
        ancestry_county_conditions = [{
            "column": "county_code",
            "equivalence": "IN",
            "value": county_fips
        }]
        county_totals = database_manager.fetch_by(
            AncestryCounty(database_manager),
            ancestry_county_conditions
        )
    else:
        raise ApiParamInvalidZipCodeError

    for header, is_eligible in eligible_headers.items():
        if is_eligible is True:
            zip_totals[header] = 0
            for county_total in county_totals:
                for county_percentage in county_percentages:
                    if county_percentage.get_state_county_fips() == \
                            county_total.county_code:
                        total = getattr(
                                county_total,
                                header
                            )
                        if total is None:
                            total = 0
                        zip_totals[header] += (
                            round(
                                total * county_percentage.zip_population_percent
                            )
                        )
                        break

    years = [str(x) for x in range(1980, 2010)]
    raw_output_data = OrderedDict({})
    totals = {}
    for year in years:
        output_year = {}
        for header, value in zip_totals.items():
            if year in header:
                output_year[header[:-len(year)-1]] = value
            if len(output_year) > 0:
                raw_output_data[year] = output_year
        if year not in totals:
            if year in raw_output_data:
                totals[year] = sum([v for k, v in raw_output_data[year].items()])

    # get percentages
    output_data = OrderedDict({})
    notes = []
    for year in raw_output_data:
        output_data[year] = {"breakdown":{}}
        for key, value in raw_output_data[year].items():
            output_data[year]["breakdown"][key] = 100 * value / totals[year]
        if get_is_eligible(subscription_plan, "totals") is True:
            output_data[year]['total'] = totals[year]
        else:
            notes.append("Upgrade to a paid plan for totals")

    if len(output_data) == 1:
        notes.append("Upgrade plan for historical data")

    notes = list(set(notes))

    state_name = ""
    state_code = ""
    if state.code is not None:
        state_code = state.code
    if state.name is not None:
        state_name = state.name
    output = OrderedDict({
        "ancestry_ranges": output_data,
        "units": "percent",
        "location": {
            "city": {
                "name": city_name,
                "api_endpoint": '/v1/ancestry/city?city={}&state={}'.format(
                    requote_uri(city_name),
                    state_code.upper()
                ),
            },
            "state": {
                "name": state_name,
                "code": state_code.upper(),
                "api_endpoint": '/v1/ancestry/state?code={}'.format(state_code.upper()),
            },
            "country": {
                "name": "United States of America",
                "code": "US",
                "api_endpoint": '/v1/ancestry/country?code=US',
            }
        },
        "notes": notes
    })
    http_server.print_headers()
    http_server.print_json(output)


api_manager.set_method_callback(
    ApiManager.HTTP_METHOD_GET,
    handle_get
)


api_manager.require_auth()


try:
    api_manager.run()
except ApiParamNoZipCodeProvidedError:
    http_server.set_status(400)
    json_response = {"error": "A 'zip' parameter is required"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidZipCodeError:
    http_server.set_status(400)
    json_response = {"error": "Invalid zip code provided"}
    http_server.print_headers()
    http_server.print_json(json_response)
