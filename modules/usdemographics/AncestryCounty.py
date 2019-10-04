from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class AncestryCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    state_id = None
    state_code = None
    county_code = None
    country_id = None
    total_1990 = None
    total_2000 = None
    total_2009 = None
    american_1990 = None
    american_2000 = None
    american_2009 = None
    arab_1990 = None
    arab_2000 = None
    arab_2009 = None
    british_2009 = None
    czech_1990 = None
    czech_2000 = None
    czech_2009 = None
    danish_1990 = None
    danish_2000 = None
    danish_2009 = None
    dutch_1990 = None
    dutch_2000 = None
    dutch_2009 = None
    english_1990 = None
    english_2000 = None
    english_2009 = None
    european_2009 = None
    french_1990 = None
    french_2000 = None
    french_2009 = None
    french_canadian_1990 = None
    french_canadian_2000 = None
    french_canadian_2009 = None
    german_1990 = None
    german_2000 = None
    german_2009 = None
    greek_1990 = None
    greek_2000 = None
    greek_2009 = None
    hungarian_1990 = None
    hungarian_2000 = None
    hungarian_2009 = None
    irish_1990 = None
    irish_2000 = None
    irish_2009 = None
    italian_1990 = None
    italian_2000 = None
    italian_2009 = None
    lithuanian_1990 = None
    lithuanian_2000 = None
    lithuanian_2009 = None
    norwegian_1990 = None
    norwegian_2000 = None
    norwegian_2009 = None
    polish_1990 = None
    polish_2000 = None
    polish_2009 = None
    portuguese_1990 = None
    portuguese_2000 = None
    portuguese_2009 = None
    russian_1990 = None
    russian_2000 = None
    russian_2009 = None
    scotch_irish_1990 = None
    scotch_irish_2000 = None
    scotch_irish_2009 = None
    scottish_1990 = None
    scottish_2000 = None
    scottish_2009 = None
    slovak_1990 = None
    slovak_2000 = None
    slovak_2009 = None
    subsaharan_african_1990 = None
    subsaharan_african_2000 = None
    subsaharan_african_2009 = None
    swedish_1990 = None
    swedish_2000 = None
    swedish_2009 = None
    swiss_1990 = None
    swiss_2000 = None
    swiss_2009 = None
    ukrainian_1990 = None
    ukrainian_2000 = None
    ukrainian_2009 = None
    welsh_1990 = None
    welsh_2000 = None
    welsh_2009 = None
    west_indian_1990 = None
    west_indian_2000 = None
    west_indian_2009 = None
    other_1990 = None
    other_2000 = None
    other_groups_2009 = None
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
        return AncestryCounty.fetch_by(database_manager, conditions)

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
        return AncestryCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_county_code(database_manager, county_code):
        conditions = [{
            "column": "county_code",
            "equivalence": "=",
            "value": county_code
        }]
        return AncestryCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return AncestryCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = AncestryCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj





