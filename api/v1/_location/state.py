#!/usr/bin/env python3
import sys
sys.path.append("../../../")
from os import environ
from settings.settings import settings
from modules.HttpServer import HttpServer
from modules.apimanager.ApiManager import ApiManager
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsState import UsState


class ApiParamNoCodeOrNameProvidedError(Exception):
    pass


class ApiParamInvalidCodeError(Exception):
    pass


class ApiParamInvalidNameError(Exception):
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
    if "code" not in query_params and "name" not in query_params:
        raise ApiParamNoCodeOrNameProvidedError

    if "code" in query_params:
        code = query_params["code"]
        state = UsState.fetch_by_code(database_manager, code)
        if state is None:
            raise ApiParamInvalidCodeError

    if "name" in query_params:
        name = query_params["name"]
        state = UsState.fetch_by_code(database_manager, name)
        if state is None:
            raise ApiParamInvalidNameError

    if state is not None:
        output = {
            "name": state.name,
            "code": state.code
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
except ApiParamNoCodeOrNameProvidedError:
    http_server.set_status(400)
    json_response = {"error": "A 'code' ore 'name' parameter is required"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidCodeError:
    http_server.set_status(400)
    json_response = {"error": "Invalid state code provided"}
    http_server.print_headers()
    http_server.print_json(json_response)
except ApiParamInvalidNameError:
    http_server.set_status(400)
    json_response = {"error": "Invalid state name provided"}
    http_server.print_headers()
    http_server.print_json(json_response)
