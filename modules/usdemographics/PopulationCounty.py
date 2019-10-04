from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class PopulationCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    state_id = None
    state_code = None
    county_code = None
    country_id = None
    total_1930 = None
    total_1940 = None
    total_1950 = None
    total_1960 = None
    total_1970 = None
    total_1980 = None
    total_1990 = None
    total_2000 = None
    total_2010 = None
    estimate_1971 = None
    estimate_1972 = None
    estimate_1973 = None
    estimate_1974 = None
    estimate_1975 = None
    estimate_1976 = None
    estimate_1977 = None
    estimate_1978 = None
    estimate_1979 = None
    estimate_1981 = None
    estimate_1982 = None
    estimate_1983 = None
    estimate_1984 = None
    estimate_1985 = None
    estimate_1986 = None
    estimate_1987 = None
    estimate_1988 = None
    estimate_1989 = None
    estimate_1990 = None
    estimate_1991 = None
    estimate_1992 = None
    estimate_1993 = None
    estimate_1994 = None
    estimate_1995 = None
    estimate_1996 = None
    estimate_1997 = None
    estimate_1998 = None
    estimate_1999 = None
    estimate_2000 = None
    estimate_2001 = None
    estimate_2002 = None
    estimate_2003 = None
    estimate_2004 = None
    estimate_2005 = None
    estimate_2006 = None
    estimate_2007 = None
    estimate_2008 = None
    estimate_2009 = None
    ctime = None
    mtime = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    def get_population_for_year(self, year):
        year = str(year)
        population = None
        if hasattr(self, "total_{}".format(year)):
            population = getattr(self, "total_{}".format(year))
        if hasattr(self, "estimate_{}".format(year)):
            population = getattr(self, "estimate_{}".format(year))
        return population

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
        return PopulationCounty.fetch_by(database_manager, conditions)

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
        return PopulationCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_county_code(database_manager, county_code):
        conditions = [{
            "column": "county_code",
            "equivalence": "=",
            "value": county_code
        }]
        return PopulationCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return PopulationCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = PopulationCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj


