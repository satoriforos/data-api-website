from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager
import random


class AreaCode(DatabaseObject):
    local_exclusions = [
    ]
    id = None
    name = None
    code = None
    city_id = None
    state_id = None
    country_id = None
    is_active = True
    ctime = None
    mtime = None

    def __init__(self, database_manager):
        self.database_manager = database_manager

    @staticmethod
    def fetch_by_area_code(database_manager, area_code):
        conditions = [{
            "column": "area_code",
            "equivalence": "=",
            "value": area_code
        }]
        return AreaCode.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = AreaCode(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
