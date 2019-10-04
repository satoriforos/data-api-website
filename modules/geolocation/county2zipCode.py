from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class county2zipCode(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    state_id = None
    county_id = None
    county_fips = None
    county_subdivision_fips = None
    county_subdivision_class_code = None
    zip = None
    land_area = None
    zip_population_percent = None
    zip_land_area_percent = None
    county_subdivision_population_percent = None
    county_subdividion_land_area_percent = None
    zip_land_area = None
    zip_population = None
    county_subdivision_land_area = None
    county_subdivision_population = None
    population_2010 = None
    ctime = None
    mtime = None
    county_subdivision_housing_units = None
    zip_housing_units = None
    housing_units = None
    zip_housing_units_percent = None
    county_subdivision_housing_units_percent = None
    zip_area = None
    county_subdivision_area = None
    zip_area_percent = None
    county_subdivision_area_percent = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    def get_state_county_fips(self):
        return int(
            "{0:02d}{1:03d}".format(
                self.state_fips, self.county_fips
            )
        )

    @staticmethod
    def fetch_by_zip_int(database_manager, zip_int):
        conditions = [{
            "column": "zip",
            "equivalence": "=",
            "value": int(zip_int)
        }]
        return county2zipCode.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = county2zipCode(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
