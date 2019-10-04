from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager
from .county2zipCode import county2zipCode


class ZipCode(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    zip_code = None
    zip_code_type = None
    city = None
    state_code = None
    city_id = None
    state_id = None
    country_id = None
    area_km2 = None
    location_type = None
    latitude = None
    longitude = None
    location_code = None
    is_decommisioned = False
    num_tax_returns = None
    estimated_population = None
    total_wages = None
    ctime = None
    mtime = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    def get_county_percentages(self):
        conditions = [{
            "column": "zip",
            "equivalence": "=",
            "value": self.zip_code
        }]
        c2zs = self.database_manager.fetch_by(
            county2zipCode(self.database_manager),
            conditions
        )
        return c2zs

    def get_city_area_km2(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(self)
        )
        query = "SELECT ROUND(sum(`area_m2`)/1000000) as `area_km2` FROM `{}` WHERE `city`={};".format(
            table_name,
            self.database_manager.database.escape(self.city)
        )
        results = self.__execute_sql_query(query)
        area_km2 = int(results[0]["area_km2"])
        return area_km2

    def get_mean_income(self):
        total_wages = self.total_wages
        if total_wages is None:
            total_wages = 0
        num_tax_returns = self.num_tax_returns
        if num_tax_returns is None:
            mean_income = None
        else:
            mean_income = int(total_wages / num_tax_returns)
        return mean_income

    def get_estimated_national_population(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(self)
        )
        query = "SELECT sum(`estimated_population`) as `estimated_population` FROM `{}`;".format(
            table_name
        )
        results = self.__execute_sql_query(query)
        estimated_population = int(results[0]["estimated_population"])
        return estimated_population

    def get_estimated_city_population(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(self)
        )
        query = "SELECT sum(`estimated_population`) as `estimated_population` FROM `{}` WHERE `city`={};".format(
            table_name,
            self.database_manager.database.escape(self.city)
        )
        results = self.__execute_sql_query(query)
        estimated_population = int(results[0]["estimated_population"])
        return estimated_population

    def get_mean_national_income(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(self)
        )
        query = "SELECT sum(`total_wages`) as `total_wages` FROM `{}`;".format(
            table_name
        )
        results = self.__execute_sql_query(query)
        total_wages = int(results[0]["total_wages"])

        query = "SELECT sum(`num_tax_returns`) as `total_returns` FROM `{}`;".format(
            table_name
        )
        results = self.__execute_sql_query(query)
        total_returns = int(results[0]["total_returns"])
        mean_national_income = int(total_wages / total_returns)
        return mean_national_income
        
    def get_mean_city_income(self):
        table_name = DatabaseManager.camel_to_underscore(
            DatabaseManager.get_class_name(self)
        )
        query = "SELECT sum(`total_wages`) as `total_wages` FROM `{}` WHERE `city`={};".format(
            table_name,
            self.database_manager.database.escape(self.city)
        )
        results = self.__execute_sql_query(query)
        total_wages = int(results[0]["total_wages"])

        query = "SELECT sum(`num_tax_returns`) as `total_returns` FROM `{}` WHERE `city`={};".format(
            table_name,
            self.database_manager.database.escape(self.city)
        )
        results = self.__execute_sql_query(query)
        total_returns = int(results[0]["total_returns"])
        mean_city_income = int(total_wages / total_returns)
        return mean_city_income

    def get_area_codes(self):
        area_codes = []
        if self.city_id is not None:
            conditions = [{
                "column": "city_id",
                "equivalence": "=",
                "value": self.city_id
            }]

            area_code_template = AreaCode(database_manager)
            area_codes = self.database_manager.fetch_by(
                area_code_template,
                conditions
            )

        if len(area_codes) == 0:
            if self.state_id is not None:
                conditions = [{
                    "column": "city_id",
                    "equivalence": "=",
                    "value": self.state_id
                }]

                area_code_template = AreaCode(database_manager)
                area_codes = self.database_manager.fetch_by(
                    area_code_template,
                    conditions
                )

        return area_codes
        
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

    def get_counties(self):
        counties = []
        conditions = [{
            "column": "zip",
            "equivalence": "=",
            "value": int(self.zip_code)
        }]
        county2zipCodes = self.database_manager.fetch_by(
            county2zipCode(self.database_manager),
            conditions
        )
        if len(county2zipCodes) > 0:
            county_ids = []
            for county2zip in county2zipCodes:
                county_ids.append(county2zip.id)
            conditions = [{
                "column": "id",
                "equivalence": "IN",
                "value": ", ".join(county_ids)
            }]
            counties = database_manager.fetch_by(
                UsCounty(database_manager),
                conditions
            )
        return counties

    @staticmethod
    def fetch_by_zip_int(database_manager, zip_int, is_decommisioned=None):
        conditions = [{
            "column": "zip_code",
            "equivalence": "=",
            "value": zip_int
        }]
        if is_decommisioned is not None:
            conditions.append({
                "column": "is_decommisioned",
                "equivalence": "=",
                "value": int(is_decommisioned)
            })
        return ZipCode.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = ZipCode(database_manager)
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
