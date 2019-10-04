from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class RaceCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    county_code = None
    state_id = None
    state_code = None
    county_code = None
    white_2000 = None
    white_2001 = None
    white_2002 = None
    white_2003 = None
    white_2004 = None
    white_2005 = None
    white_2006 = None
    white_2007 = None
    white_2008 = None
    white_2009 = None
    white_2010 = None
    black_2000 = None
    black_2001 = None
    black_2002 = None
    black_2003 = None
    black_2004 = None
    black_2005 = None
    black_2006 = None
    black_2007 = None
    black_2008 = None
    black_2009 = None
    black_2010 = None
    aboriginal_alaskan_2000 = None
    aboriginal_alaskan_2001 = None
    aboriginal_alaskan_2002 = None
    aboriginal_alaskan_2003 = None
    aboriginal_alaskan_2004 = None
    aboriginal_alaskan_2005 = None
    aboriginal_alaskan_2006 = None
    aboriginal_alaskan_2007 = None
    aboriginal_alaskan_2008 = None
    aboriginal_alaskan_2009 = None
    aboriginal_alaskan_2010 = None
    asian_2000 = None
    asian_2001 = None
    asian_2002 = None
    asian_2003 = None
    asian_2004 = None
    asian_2005 = None
    asian_2006 = None
    asian_2007 = None
    asian_2008 = None
    asian_2009 = None
    asian_2010 = None
    hawaiian_pacific_islander_2000 = None
    hawaiian_pacific_islander_2001 = None
    hawaiian_pacific_islander_2002 = None
    hawaiian_pacific_islander_2003 = None
    hawaiian_pacific_islander_2004 = None
    hawaiian_pacific_islander_2005 = None
    hawaiian_pacific_islander_2006 = None
    hawaiian_pacific_islander_2007 = None
    hawaiian_pacific_islander_2008 = None
    hawaiian_pacific_islander_2009 = None
    hawaiian_pacific_islander_2010 = None
    mixed_2000 = None
    mixed_2001 = None
    mixed_2002 = None
    mixed_2003 = None
    mixed_2004 = None
    mixed_2005 = None
    mixed_2006 = None
    mixed_2007 = None
    mixed_2008 = None
    mixed_2009 = None
    mixed_2010 = None
    hispanic_latino_2000 = None
    hispanic_latino_2001 = None
    hispanic_latino_2002 = None
    hispanic_latino_2003 = None
    hispanic_latino_2004 = None
    hispanic_latino_2005 = None
    hispanic_latino_2006 = None
    hispanic_latino_2007 = None
    hispanic_latino_2008 = None
    hispanic_latino_2009 = None
    hispanic_latino_2010 = None
    white_non_hispanic_2000 = None
    white_non_hispanic_2001 = None
    white_non_hispanic_2002 = None
    white_non_hispanic_2003 = None
    white_non_hispanic_2004 = None
    white_non_hispanic_2005 = None
    white_non_hispanic_2006 = None
    white_non_hispanic_2007 = None
    white_non_hispanic_2008 = None
    white_non_hispanic_2009 = None
    white_non_hispanic_2010 = None
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
        return RaceCounty.fetch_by(database_manager, conditions)

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
        return RaceCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return RaceCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = RaceCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
