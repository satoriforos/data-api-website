from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class IncomeCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    state_id = None
    state_code = None
    county_code = None
    country_id = None
    median_1979 = None
    median_1989 = None
    median_1999 = None
    less_than_10000_1979 = None
    less_than_10000_1989 = None
    less_than_10000_1999 = None
    between_10000_and_14999_1979 = None
    between_10000_and_14999_1989 = None
    between_10000_and_14999_1999 = None
    between_15000_and_19999_1979 = None
    between_15000_and_19999_1989 = None
    between_15000_and_19999_1999 = None
    between_20000_and_24999_1979 = None
    between_20000_and_24999_1989 = None
    between_20000_and_24999_1999 = None
    between_25000_and_29999_1979 = None
    between_25000_and_29999_1989 = None
    between_25000_and_29999_1999 = None
    between_30000_and_34999_1979 = None
    between_30000_and_34999_1989 = None
    between_30000_and_34999_1999 = None
    between_35000_and_39999_1979 = None
    between_35000_and_39999_1989 = None
    between_35000_and_39999_1999 = None
    between_40000_and_49999_1979 = None
    between_40000_and_49999_1989 = None
    between_40000_and_49999_1999 = None
    between_40000_and_44999_1989 = None
    between_40000_and_44999_1999 = None
    between_45000_and_49999_1989 = None
    between_45000_and_49999_1999 = None
    between_50000_and_74999_1979 = None
    between_50000_and_74999_1989 = None
    between_50000_and_74999_1999 = None
    between_50000_and_59999_1989 = None
    between_50000_and_59999_1999 = None
    between_60000_and_74999_1989 = None
    between_60000_and_74999_1999 = None
    over_75000_1979 = None
    over_75000_1989 = None
    over_75000_1999 = None
    between_75000_and_99999_1989 = None
    between_75000_and_99999_1999 = None
    between_100000_and_124999_1989 = None
    between_100000_and_124999_1999 = None
    between_125000_and_149999_1989 = None
    between_125000_and_149999_1999 = None
    over_150000_1989 = None
    over_150000_1999 = None
    between_150000_and_199999_1999 = None
    over_200000_1999 = None
    ctime = None
    mtime = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    @staticmethod
    def fetch_by_state_name(database_manager, state_name):
        conditions = [
            {
                "column": "county_name",
                "equivalence": "=",
                "value": state_name.upper()
            },
            {
                "column": "state_id",
                "equivalence": "IS",
                "value": None
            },
        ]
        return IncomeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_country_name(database_manager, country_name):
        conditions = [
            {
                "column": "county_name",
                "equivalence": "=",
                "value": country_name.upper()
            },
            {
                "column": "state_id",
                "equivalence": "IS",
                "value": None
            },
        ]
        return IncomeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_county_code(database_manager, county_code):
        conditions = [{
            "column": "county_code",
            "equivalence": "=",
            "value": county_code
        }]
        return IncomeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return IncomeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = IncomeCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
