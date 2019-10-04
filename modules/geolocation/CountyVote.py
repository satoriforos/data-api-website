from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class CountyVote(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    combined_fips = None
    votes_dem_2016 = None
    votes_gop_2016 = None
    total_votes_2016 = None
    per_dem_2016 = None
    per_gop_2016 = None
    diff_2016 = None
    per_point_diff_2016 = None
    state_abbr = None
    county_name = None
    FIPS = None
    total_votes_2012 = None
    votes_dem_2012 = None
    votes_gop_2012 = None
    county_fips = None
    state_fips = None
    per_dem_2012 = None
    per_gop_2012 = None
    diff_2012 = None
    per_point_diff_2012 = None
    ctime = None
    mtime = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    @staticmethod
    def fetch_by_name(database_manager, name):
        conditions = [{
            "column": "name",
            "equivalence": "=",
            "value": name
        }]
        return CountyVote.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_code(database_manager, code):
        conditions = [{
            "column": "code",
            "equivalence": "=",
            "value": code
        }]
        return CountyVote.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return CountyVote.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = CountyVote(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
