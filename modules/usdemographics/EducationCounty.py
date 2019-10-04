from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class EducationCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    state_id = None
    state_code = None
    county_code = None
    country_id = None
    num_adults_1980 = None
    num_adults_1990 = None
    num_adults_2000 = None
    num_adults_2005_2009 = None
    less_than_grade_9_1990 = None
    less_than_grade_9_2000 = None
    less_than_grade_9_2005_2009 = None
    grade_9_to_12_no_diploma_1990 = None
    grade_9_to_12_no_diploma_2000 = None
    grade_9_to_12_no_diploma_2005_2009 = None
    high_school_graduate_1990 = None
    high_school_graduate_2000 = None
    high_school_graduate_2005_2009 = None
    some_college_or_associate_degree_1990 = None
    some_college_or_associate_degree_2000 = None
    incomplete_college_2000 = None
    incomplete_college_2005_2009 = None
    associate_degree_2000 = None
    associate_degree_2005_2009 = None
    any_college_degree_1990 = None
    any_college_degree_2000 = None
    bachelors_degree_2000 = None
    bachelors_degree_2005_2009 = None
    graduate_degree_2000 = None
    graduate_degree_2005_2009 = None
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
        return EducationCounty.fetch_by(database_manager, conditions)

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
        return EducationCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_county_code(database_manager, county_code):
        conditions = [{
            "column": "county_code",
            "equivalence": "=",
            "value": county_code
        }]
        return EducationCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return EducationCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = EducationCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
