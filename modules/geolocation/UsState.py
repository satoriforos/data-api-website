from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager
from .ZipCode import ZipCode
import random


class UsState(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    name = None
    code = None
    city = None
    country_id = None
    area_km2 = None
    is_decommisioned = False
    ctime = None
    mtime = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    def get_estimated_population(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(ZipCode(self.database_manager))
        )
        query = "SELECT sum(`estimated_population`) as `estimated_population` FROM `{}` WHERE `state_code`={};".format(
            table_name,
            self.database_manager.database.escape(self.code)
        )
        results = self.__execute_sql_query(query)
        estimated_population = int(results[0]["estimated_population"])
        return estimated_population
        
    def get_mean_income(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(ZipCode(self.database_manager))
        )
        query = "SELECT sum(`total_wages`) as `total_wages` FROM `{}` WHERE `state_code`={};".format(
            table_name,
            self.database_manager.database.escape(self.code)
        )
        results = self.__execute_sql_query(query)
        total_wages = int(results[0]["total_wages"])

        query = "SELECT sum(`num_tax_returns`) as `total_returns` FROM `{}` WHERE `state_code`={};".format(
            table_name,
            self.database_manager.database.escape(self.code)
        )
        results = self.__execute_sql_query(query)
        total_returns = int(results[0]["total_returns"])
        mean_city_income = int(total_wages / total_returns)
        return mean_city_income

    def __execute_sql_query(self, query):
        self.database_manager.database.row_factory = self.database_manager.dict_factory
        cursor = self.database_manager.database.cursor()
        cursor.execute(query)
        response = cursor.fetchall()
        results = []
        if len(response) > 0:
            for row in response:
                result = {}
                if isinstance(row, dict):
                    for column, value in row.items():
                        result[column] = value
                elif isinstance(row, tuple) or isinstance(row, list):
                    for idx, col in enumerate(cursor.description):
                        result[col[0]] = row[idx]
                results.append(result)
        return results

    @staticmethod
    def fetch_by_code(database_manager, code,):
        conditions = [{
            "column": "code",
            "equivalence": "=",
            "value": code
        }]
        return UsState.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return UsState.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = UsState(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj

    def from_dict(self, database_manager, data):
        super.from_dict(database_manager, data)
        if 'is_decommisioned' in data:
            self.is_banned = DatabaseObject.get_boolean_from_string(
                data["is_decommisioned"]
            )
