#!/usr/bin/env python3
import sys
sys.path.append("../../../")
import re
from os import environ
import re
from settings.settings import settings
from modules.HttpServer import HttpServer
from modules.apimanager.ApiManager import ApiManager
from modules.apimanager.SubscriptionPlan import SubscriptionPlan
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.Country import Country
from modules.usdemographics.IncomeCounty import IncomeCounty
from modules.usdemographics.PopulationCounty import PopulationCounty
from common import eligible_headers
from common import get_is_eligible
from collections import OrderedDict


class ApiParamNoCountryCodeProvidedError(Exception):
    pass


class ApiParamInvalidCountryCodeError(Exception):
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
    if "code" not in query_params:
        raise ApiParamNoCountryCodeProvidedError

    raw_country_code_string = query_params["code"]
    country_code_string = raw_country_code_string.upper()

    if country_code_string is None:
        raise ApiParamInvalidCountryCodeError

    match = re.match(r'^[A-Za-z]{2}$', country_code_string)
    if match is None:
        raise ApiParamInvalidCountryCodeError

    country = Country.fetch_by_code(database_manager, country_code_string)
    if country is None:
        raise ApiParamInvalidCountryCodeError

    country_name = country.name
    if country.code == "US":
        country_name = "United States"

    county_total = IncomeCounty.fetch_by_country_name(
        database_manager,
        country_name.upper()
    )
    population_total = PopulationCounty.fetch_by_country_name(
        database_manager,
        country_name.upper()
    )
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
    for header, is_eligible in eligible_headers.items():
        if is_eligible is True:
            zip_totals[header] = 0
            total = getattr(
                    county_total,
                    header
                )
            if total is None:
                total = 0
            zip_totals[header] = (
                round(
                    total
                )
            )

    years = [str(x) for x in range(1979, 2000, 10)]
    totals = {}
    for year in years:
        totals[year] = population_total.get_population_for_year(year)

    raw_output_data = OrderedDict({})
    for year in years:
        output_year = {}
        for header, value in zip_totals.items():
            if year in header:
                output_year[header[:-len(year)-1]] = 100 * value / totals[year]
            if len(output_year) > 0:
                raw_output_data[year] = output_year

    # get percentages
    output_data = OrderedDict({})
    notes = []
    medians = {}
    for year in raw_output_data:
        output_data[year] = {"breakdown":{}}
        for key, value in raw_output_data[year].items():
            if key == "median":
                medians[year] = value
            else:
                output_data[year]["breakdown"][key] = 100 * value / totals[year]
        output_data[year]["median_income"] = {
            "currency": "USD",
            "amount": medians[year]
        }
        if get_is_eligible(subscription_plan, "totals") is True:
            output_data[year]['total_people'] = totals[year]
        else:
            notes.append("Upgrade to a paid plan for totals")

    if len(output_data) == 1:
        notes.append("Upgrade plan for historical data")

    output = OrderedDict({
        "income_ranges": output_data,
        "units": "percent",
        "location": {
            "country": {
                "name": "United States of America",
                "code": "US",
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
except ApiParamNoCountryCodeProvidedError:
    http_server.set_status(400)
    json_response = {"error": "A country code parameter is required"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidCountryCodeError:
    http_server.set_status(400)
    json_response = {"error": "Invalid country code provided"}
    http_server.print_headers()
    http_server.print_json(json_response)
