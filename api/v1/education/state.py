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
from modules.geolocation.UsState import UsState
from modules.usdemographics.EducationCounty import EducationCounty
from common import eligible_headers
from common import get_is_eligible
from collections import OrderedDict


class ApiParamNoStateCodeProvidedError(Exception):
    pass


class ApiParamInvalidStateCodeError(Exception):
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
        raise ApiParamNoStateCodeProvidedError

    raw_state_code_string = query_params["code"]
    state_code_string = raw_state_code_string.upper()

    match = re.match(r'^[A-Za-z]{2}$', state_code_string)
    if match is None:
        raise ApiParamInvalidStateCodeError

    state = UsState.fetch_by_code(
        database_manager,
        state_code_string
    )

    if state is None:
        raise ApiParamInvalidStateCodeError

    county_total = EducationCounty.fetch_by_state_name(
        database_manager,
        state.name.upper()
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

    years = ["1980", "1990", "2000", "2009"]
    raw_output_data = OrderedDict({})
    totals = {}
    for year in years:
        output_year = {}
        for header, value in zip_totals.items():
            if "num_adults" not in header:
                if year in header:
                    ending = year
                    end = len(ending) + 1
                    if "_2005_" in header:
                        ending = "2005_{}".format(year)
                        end = len(ending) + 1
                    output_year[header[:-end]] = 100 * value / zip_totals[
                        "num_adults_{}".format(ending)
                    ]
            if len(output_year) > 0:
                raw_output_data[year] = output_year
        if year not in totals:
            if year in raw_output_data:
                ending = year
                if year == "2009":
                    ending = "2005_2009"
                totals[year] = zip_totals["num_adults_{}".format(ending)]

    # get percentages
    output_data = OrderedDict({})
    notes = []
    for year in raw_output_data:
        output_data[year] = {"breakdown":{}}
        for key, value in raw_output_data[year].items():
            output_data[year]["breakdown"][key] = value
        if get_is_eligible(subscription_plan, "totals") is True:
            output_data[year]['total_adults'] = totals[year]
        else:
            notes.append("Upgrade to a paid plan for totals")


    notes = list(set(notes))

    state_name = ""
    state_code = ""
    if state.code is not None:
        state_code = state.code
    if state.name is not None:
        state_name = state.name
    output = {
        "education_ranges": output_data,
        "location": {
            "state": {
                "name": state.name,
                "code": state.code.upper(),
            },
            "country": {
                "name": "United States of America",
                "code": "US",
                "api_endpoint": '/v1/education/country?code=US',
            }
        },
        "notes": notes
    }
    http_server.print_headers()
    http_server.print_json(output)


api_manager.set_method_callback(
    ApiManager.HTTP_METHOD_GET,
    handle_get
)


api_manager.require_auth()


try:
    api_manager.run()
except ApiParamNoStateCodeProvidedError:
    http_server.set_status(400)
    json_response = {"error": "A state code parameter is required"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidStateCodeError:
    http_server.set_status(400)
    json_response = {"error": "Invalid state code provided"}
    http_server.print_headers()
    http_server.print_json(json_response)
