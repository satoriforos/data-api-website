from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager


class CrimeCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    state_id = None
    state_code = None
    county_code = None
    violent_crimes_1981 = None
    violent_crimes_1982 = None
    violent_crimes_1983 = None
    violent_crimes_1984 = None
    violent_crimes_1985 = None
    violent_crimes_1986 = None
    violent_crimes_1987 = None
    violent_crimes_1988 = None
    violent_crimes_1989 = None
    violent_crimes_1990 = None
    violent_crimes_1991 = None
    violent_crimes_1992 = None
    violent_crimes_1993 = None
    violent_crimes_1994 = None
    violent_crimes_1995 = None
    violent_crimes_1996 = None
    violent_crimes_1997 = None
    violent_crimes_1998 = None
    violent_crimes_1999 = None
    violent_crimes_2000 = None
    violent_crimes_2001 = None
    violent_crimes_2002 = None
    violent_crimes_2003 = None
    violent_crimes_2004 = None
    violent_crimes_2005 = None
    violent_crimes_2006 = None
    violent_crimes_2007 = None
    violent_crimes_2008 = None
    murders_1990 = None
    murders_1991 = None
    murders_1992 = None
    murders_1993 = None
    murders_1994 = None
    murders_1995 = None
    murders_1996 = None
    murders_1997 = None
    murders_1998 = None
    murders_1999 = None
    murders_2000 = None
    murders_2001 = None
    murders_2002 = None
    murders_2003 = None
    murders_2004 = None
    murders_2005 = None
    murders_2006 = None
    murders_2007 = None
    murders_2008 = None
    forcible_rapes_1990 = None
    forcible_rapes_1991 = None
    forcible_rapes_1992 = None
    forcible_rapes_1993 = None
    forcible_rapes_1994 = None
    forcible_rapes_1995 = None
    forcible_rapes_1996 = None
    forcible_rapes_1997 = None
    forcible_rapes_1998 = None
    forcible_rapes_1999 = None
    forcible_rapes_2000 = None
    forcible_rapes_2001 = None
    forcible_rapes_2002 = None
    forcible_rapes_2003 = None
    forcible_rapes_2004 = None
    forcible_rapes_2005 = None
    forcible_rapes_2006 = None
    forcible_rapes_2007 = None
    forcible_rapes_2008 = None
    robberies_1981 = None
    robberies_1982 = None
    robberies_1983 = None
    robberies_1984 = None
    robberies_1985 = None
    robberies_1986 = None
    robberies_1987 = None
    robberies_1988 = None
    robberies_1989 = None
    robberies_1990 = None
    robberies_1991 = None
    robberies_1992 = None
    robberies_1993 = None
    robberies_1994 = None
    robberies_1995 = None
    robberies_1996 = None
    robberies_1997 = None
    robberies_1998 = None
    robberies_1999 = None
    robberies_2000 = None
    robberies_2001 = None
    robberies_2002 = None
    robberies_2003 = None
    robberies_2004 = None
    robberies_2005 = None
    robberies_2006 = None
    robberies_2007 = None
    robberies_2008 = None
    aggravated_assaults_1981 = None
    aggravated_assaults_1982 = None
    aggravated_assaults_1983 = None
    aggravated_assaults_1984 = None
    aggravated_assaults_1985 = None
    aggravated_assaults_1986 = None
    aggravated_assaults_1987 = None
    aggravated_assaults_1988 = None
    aggravated_assaults_1989 = None
    aggravated_assaults_1990 = None
    aggravated_assaults_1991 = None
    aggravated_assaults_1992 = None
    aggravated_assaults_1993 = None
    aggravated_assaults_1994 = None
    aggravated_assaults_1995 = None
    aggravated_assaults_1996 = None
    aggravated_assaults_1997 = None
    aggravated_assaults_1998 = None
    aggravated_assaults_1999 = None
    aggravated_assaults_2000 = None
    aggravated_assaults_2001 = None
    aggravated_assaults_2002 = None
    aggravated_assaults_2003 = None
    aggravated_assaults_2004 = None
    aggravated_assaults_2005 = None
    aggravated_assaults_2006 = None
    aggravated_assaults_2007 = None
    aggravated_assaults_2008 = None
    property_crimes_1981 = None
    property_crimes_1982 = None
    property_crimes_1983 = None
    property_crimes_1984 = None
    property_crimes_1985 = None
    property_crimes_1986 = None
    property_crimes_1987 = None
    property_crimes_1988 = None
    property_crimes_1989 = None
    property_crimes_1990 = None
    property_crimes_1991 = None
    property_crimes_1992 = None
    property_crimes_1993 = None
    property_crimes_1994 = None
    property_crimes_1995 = None
    property_crimes_1996 = None
    property_crimes_1997 = None
    property_crimes_1998 = None
    property_crimes_1999 = None
    property_crimes_2000 = None
    property_crimes_2001 = None
    property_crimes_2002 = None
    property_crimes_2003 = None
    property_crimes_2004 = None
    property_crimes_2005 = None
    property_crimes_2006 = None
    property_crimes_2007 = None
    property_crimes_2008 = None
    burglaries_1981 = None
    burglaries_1982 = None
    burglaries_1983 = None
    burglaries_1984 = None
    burglaries_1985 = None
    burglaries_1986 = None
    burglaries_1987 = None
    burglaries_1988 = None
    burglaries_1989 = None
    burglaries_1990 = None
    burglaries_1991 = None
    burglaries_1992 = None
    burglaries_1993 = None
    burglaries_1994 = None
    burglaries_1995 = None
    burglaries_1996 = None
    burglaries_1997 = None
    burglaries_1998 = None
    burglaries_1999 = None
    burglaries_2000 = None
    burglaries_2001 = None
    burglaries_2002 = None
    burglaries_2003 = None
    burglaries_2004 = None
    burglaries_2005 = None
    burglaries_2006 = None
    burglaries_2007 = None
    burglaries_2008 = None
    larceny_thefts_1981 = None
    larceny_thefts_1982 = None
    larceny_thefts_1983 = None
    larceny_thefts_1984 = None
    larceny_thefts_1985 = None
    larceny_thefts_1986 = None
    larceny_thefts_1987 = None
    larceny_thefts_1988 = None
    larceny_thefts_1989 = None
    larceny_thefts_1990 = None
    larceny_thefts_1991 = None
    larceny_thefts_1992 = None
    larceny_thefts_1993 = None
    larceny_thefts_1994 = None
    larceny_thefts_1995 = None
    larceny_thefts_1996 = None
    larceny_thefts_1997 = None
    larceny_thefts_1998 = None
    larceny_thefts_1999 = None
    larceny_thefts_2000 = None
    larceny_thefts_2001 = None
    larceny_thefts_2002 = None
    larceny_thefts_2003 = None
    larceny_thefts_2004 = None
    larceny_thefts_2005 = None
    larceny_thefts_2006 = None
    larceny_thefts_2007 = None
    larceny_thefts_2008 = None
    motor_vehicle_thefts_1981 = None
    motor_vehicle_thefts_1982 = None
    motor_vehicle_thefts_1983 = None
    motor_vehicle_thefts_1984 = None
    motor_vehicle_thefts_1985 = None
    motor_vehicle_thefts_1986 = None
    motor_vehicle_thefts_1987 = None
    motor_vehicle_thefts_1988 = None
    motor_vehicle_thefts_1989 = None
    motor_vehicle_thefts_1990 = None
    motor_vehicle_thefts_1991 = None
    motor_vehicle_thefts_1992 = None
    motor_vehicle_thefts_1993 = None
    motor_vehicle_thefts_1994 = None
    motor_vehicle_thefts_1995 = None
    motor_vehicle_thefts_1996 = None
    motor_vehicle_thefts_1997 = None
    motor_vehicle_thefts_1998 = None
    motor_vehicle_thefts_1999 = None
    motor_vehicle_thefts_2000 = None
    motor_vehicle_thefts_2001 = None
    motor_vehicle_thefts_2002 = None
    motor_vehicle_thefts_2003 = None
    motor_vehicle_thefts_2004 = None
    motor_vehicle_thefts_2005 = None
    motor_vehicle_thefts_2006 = None
    motor_vehicle_thefts_2007 = None
    motor_vehicle_thefts_2008 = None
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
        return CrimeCounty.fetch_by(database_manager, conditions)

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
        return CrimeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_county_code(database_manager, county_code):
        conditions = [{
            "column": "county_code",
            "equivalence": "=",
            "value": county_code
        }]
        return CrimeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return CrimeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = CrimeCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj
