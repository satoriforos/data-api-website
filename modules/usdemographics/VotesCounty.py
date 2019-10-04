from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class VotesCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    county_code = None
    state_id = None
    state_code = None
    country_id = None
    '''
    percent_voted_1980 = None
    percent_other_1980 = None
    percent_democrat_1980 = None
    percent_republican_1980 = None
    percent_ted_1984 = None
    percent_other_1984 = None
    percent_democrat_1984 = None
    percent_republican_1984 = None
    percent_ted_1988 = None
    percent_other_1988 = None
    percent_democrat_1988 = None
    percent_republican_1988 = None
    percent_ted_1992 = None
    percent_other_1992 = None
    percent_democrat_1992 = None
    percent_republican_1992 = None
    percent_ted_1996 = None
    percent_other_1996 = None
    percent_democrat_1996 = None
    percent_republican_1996 = None
    percent_ted_2000 = None
    percent_other_2000 = None
    percent_democrat_2000 = None
    percent_republican_2000 = None
    percent_ted_2004 = None
    percent_other_2004 = None
    percent_democrat_2004 = None
    percent_republican_2004 = None
    percent_ted_2008 = None
    percent_other_2008 = None
    percent_democrat_2008 = None
    percent_republican_2008 = None
    '''


    total_1980 = None
    total_1984 = None
    total_1988 = None
    total_1992 = None
    total_1996 = None
    total_2000 = None
    total_2004 = None
    total_2008 = None
    democrat_1980 = None
    democrat_1984 = None
    democrat_1988 = None
    democrat_1992 = None
    democrat_1996 = None
    democrat_2000 = None
    democrat_2004 = None
    democrat_2008 = None
    republican_1980 = None
    republican_1984 = None
    republican_1988 = None
    republican_1992 = None
    republican_1996 = None
    republican_2000 = None
    republican_2004 = None
    republican_2008 = None
    other_1980 = None
    other_1984 = None
    other_1988 = None
    other_1992 = None
    other_1996 = None
    other_2000 = None
    other_2004 = None
    other_2008 = None


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
        return VotesCounty.fetch_by(database_manager, conditions)

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
        return VotesCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equilence": "=",
            "lue": id
        }]
        return VotesCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = VotesCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
