#!/usr/bin/env python3
import sys
sys.path.append("../../../../")
import re
from os import environ
from settings.settings import settings
from modules.HttpServer import HttpServer
from modules.apimanager.ApiManager import ApiManager
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.ZipCode import ZipCode
from modules.geolocation.UsState import UsState


class ApiParamNoZipCodeeProvidedError(Exception):
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
        raise ApiParamNoZipCodeeProvidedError

    http_server.print_headers()
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

    state = UsState.fetch_by_code(database_manager, zip_code.state_code)
    is_po_box = zip_code.zip_code_type == "PO BOX"
    city_name = zip_code.city
    if zip_code.city is not None:
        city_name = zip_code.city.capitalize()

    mean_income = zip_code.get_mean_income()
    mean_national_income = zip_code.get_mean_national_income()
    mean_state_income = state.get_mean_income()
    mean_city_income = zip_code.get_mean_city_income()
    estimated_national_population = zip_code.get_estimated_national_population()
    estimated_state_population = state.get_estimated_population()
    estimated_city_population = zip_code.get_estimated_city_population()

    area_km2 = zip_code.area_m2 / 1000000
    city_area_km2 = zip_code.get_city_area_km2()
    state_area_km2 = state.area_km2
    national_area_km2 = 9147420

    output = {
        "zip": zip_code_string,
        "geolocation": {
            "latitude": zip_code.latitude,
            "longitude": zip_code.longitude,
        },
        "is_po_box": is_po_box,
        "estimated_population": zip_code.estimated_population,
        "mean_income": mean_income,
        "utc_offset": zip_code.utc_offset,
        "area_km2": area_km2,
        "city": {
            "name": city_name,
            "mean_income": mean_city_income,
            "estimated_population": estimated_city_population,
            "area_km2": city_area_km2,
        },
        "state": {
            "name": state.name.capitalize(),
            "code": state.code.upper(),
            "mean_income": mean_state_income,
            "estimated_population": estimated_state_population,
            "area_km2": state_area_km2,
        },
        "country": {
            "name": "United States of America",
            "code": "US",
            "mean_income": mean_national_income,
            "estimated_population": estimated_national_population,
            "area_km2": national_area_km2,
        }
    }
    http_server.print_json(output)


api_manager.set_method_callback(
    ApiManager.HTTP_METHOD_GET,
    handle_get
)


api_manager.require_auth()


try:
    api_manager.run()
except ApiParamNoZipCodeeProvidedError:
    http_server.set_status(400)
    json_response = {"error": "A 'zip' parameter is required"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidZipCodeError:
    http_server.set_status(400)
    json_response = {"error": "Invalid zip code provided"}
    http_server.print_headers()
    http_server.print_json(json_response)

