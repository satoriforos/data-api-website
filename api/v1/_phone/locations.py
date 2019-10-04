#!/usr/bin/env python3
import sys
sys.path.append("../../../")
import re
from os import environ
from settings.settings import settings
from modules.HttpServer import HttpServer
from modules.apimanager.ApiManager import ApiManager
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.DatabaseObject import DatabaseObject
from modules.phones.AreaCode import AreaCode
from modules.geolocation.Country import Country
from modules.geolocation.UsState import UsState
from modules.geolocation.City import City
import phonenumbers


class ApiParamNoPhoneProvidedError(Exception):
    pass


class ApiParamInvalidPhoneError(Exception):
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
    if "phone" not in query_params:
        raise ApiParamNoPhoneProvidedError

    http_server.print_headers()
    phone_string = query_params["phone"]

    matches = re.match(
        r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$",
        phone_string
    )
    if matches is None:
        raise ApiParamInvalidPhoneError

    try:
        phone = phonenumbers.parse(phone_string, "US")
        formatted_number = phonenumbers.format_number(
            phone,
            phonenumbers.PhoneNumberFormat.NATIONAL
        )
    except:
        raise ApiParamInvalidPhoneError

    area_code_string = re.findall(r"\(([^\)]{3})\)", formatted_number)
    if len(area_code_string) == 0:
        raise ApiParamInvalidPhoneError

    area_code_conditions = [{
        "column": "area_code",
        "equivalence": "=",
        "value": area_code_string[0]
    }]
    area_codes = database_manager.fetch_by(
        AreaCode(database_manager),
        area_code_conditions
    )
    locations = []
    if len(area_codes) > 0:
        city_ids = [area_code.city_id for area_code in area_codes]
        state_ids = [area_code.state_id for area_code in area_codes]
        country_id = area_codes[0].country_id

        city_conditions = [{
            "column": "id",
            "equivalence": "IN",
            "value": city_ids
        }]
        cities = database_manager.fetch_by(
            City(database_manager),
            city_conditions
        )
        city_names = set([city.name for city in cities])

        state_conditions = [{
            "column": "id",
            "equivalence": "IN",
            "value": state_ids
        }]
        states = database_manager.fetch_by(
            UsState(database_manager),
            state_conditions
        )
        state_names = set([state.name for state in states])

        
        country_conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": country_id
        }]
        country_info = None
        country = Country.fetch_by_id(
            database_manager,
            area_codes[0].country_id
        )
        if country is not None:
            country_info = {"name": country.name, "code": country.code}


        for city in cities:
            city_state = None
            for state in states:
                if city.state_id == state.id:
                    city_state = {"name": state.name, "code": state.code}
                    break

            location = {
                "is_overlay": DatabaseObject.get_boolean_from_string(
                    area_codes[0].is_overlay
                ),
                "city": city.name,
                "state": city_state,
                "country": country_info
            }
            locations.append(location)

    output = {
        "locations": locations
    }
    http_server.print_json(output)


api_manager.set_method_callback(
    ApiManager.HTTP_METHOD_GET,
    handle_get
)

api_manager.require_auth()


try:
    api_manager.run()
except ApiParamNoPhoneProvidedError:
    http_server.set_status(400)
    json_response = {"error": "An 'phone' parameter is required"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidPhoneError:
    http_server.set_status(400)
    json_response = {"error": "Invalid phone number provided"}
    http_server.print_headers()
    http_server.print_json(json_response)

