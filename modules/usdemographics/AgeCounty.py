from modules.DatabaseObject import DatabaseObject
from modules.databasemanager.DatabaseManager import DatabaseManager

class AgeCounty(DatabaseObject):

    local_exclusions = [
    ]

    id = None
    city_state = None
    county_name = None
    state_id = None
    state_code = None
    county_code = None
    country_id = None
    total_1980 = None
    total_1990 = None
    total_2000 = None
    total_2001 = None
    total_2002 = None
    total_2003 = None
    total_2004 = None
    total_2005 = None
    total_2006 = None
    total_2007 = None
    total_2008 = None
    total_2009 = None
    total_2010 = None
    median_age_1980 = None
    median_age_1990 = None
    median_age_2000 = None
    median_age_2010 = None
    under_5_1980 = None
    under_5_1990 = None
    under_5_2000 = None
    under_5_2001 = None
    under_5_2002 = None
    under_5_2003 = None
    under_5_2004 = None
    under_5_2005 = None
    under_5_2006 = None
    under_5_2007 = None
    under_5_2008 = None
    under_5_2009 = None
    under_5_2010 = None
    age_5_to_9_2000 = None
    age_5_to_9_2001 = None
    age_5_to_9_2002 = None
    age_5_to_9_2003 = None
    age_5_to_9_2004 = None
    age_5_to_9_2005 = None
    age_5_to_9_2006 = None
    age_5_to_9_2007 = None
    age_5_to_9_2008 = None
    age_5_to_9_2009 = None
    age_5_to_9_2010 = None
    age_5_to_14_1980 = None
    age_5_to_14_1990 = None
    age_5_to_14_2000 = None
    age_5_to_14_2010 = None
    age_5_to_17_1980 = None
    age_5_to_17_1990 = None
    age_5_to_17_2000 = None
    age_5_to_17_2010 = None
    age_10_to_14_2000 = None
    age_10_to_14_2001 = None
    age_10_to_14_2002 = None
    age_10_to_14_2003 = None
    age_10_to_14_2004 = None
    age_10_to_14_2005 = None
    age_10_to_14_2006 = None
    age_10_to_14_2007 = None
    age_10_to_14_2008 = None
    age_10_to_14_2009 = None
    age_10_to_14_2010 = None
    age_15_to_19_2000 = None
    age_15_to_19_2001 = None
    age_15_to_19_2002 = None
    age_15_to_19_2003 = None
    age_15_to_19_2004 = None
    age_15_to_19_2005 = None
    age_15_to_19_2006 = None
    age_15_to_19_2007 = None
    age_15_to_19_2008 = None
    age_15_to_19_2009 = None
    age_15_to_19_2010 = None
    under_18_1980 = None
    under_18_1990 = None
    under_18_2000 = None
    under_18_2001 = None
    under_18_2002 = None
    under_18_2003 = None
    under_18_2004 = None
    under_18_2005 = None
    under_18_2006 = None
    under_18_2007 = None
    under_18_2008 = None
    under_18_2009 = None
    under_18_2010 = None
    age_18_to_44_2010 = None
    age_18_and_over_1980 = None
    age_18_and_over_1990 = None
    age_18_and_over_2010 = None
    age_20_to_24_1980 = None
    age_20_to_24_1990 = None
    age_20_to_24_2000 = None
    age_20_to_24_2010 = None
    age_20_to_24_2001 = None
    age_20_to_24_2002 = None
    age_20_to_24_2003 = None
    age_20_to_24_2004 = None
    age_20_to_24_2005 = None
    age_20_to_24_2006 = None
    age_20_to_24_2007 = None
    age_20_to_24_2008 = None
    age_20_to_24_2009 = None
    age_25_to_29_1980 = None
    age_25_to_29_1990 = None
    age_25_to_29_2000 = None
    age_25_to_29_2010 = None
    age_25_to_29_2001 = None
    age_25_to_29_2002 = None
    age_25_to_29_2003 = None
    age_25_to_29_2004 = None
    age_25_to_29_2005 = None
    age_25_to_29_2006 = None
    age_25_to_29_2007 = None
    age_25_to_29_2008 = None
    age_25_to_29_2009 = None
    age_25_to_34_1980 = None
    age_25_to_34_1990 = None
    age_25_to_34_2000 = None
    age_25_to_34_2010 = None
    age_30_to_34_1980 = None
    age_30_to_34_1990 = None
    age_30_to_34_2000 = None
    age_30_to_34_2010 = None
    age_30_to_34_2001 = None
    age_30_to_34_2002 = None
    age_30_to_34_2003 = None
    age_30_to_34_2004 = None
    age_30_to_34_2005 = None
    age_30_to_34_2006 = None
    age_30_to_34_2007 = None
    age_30_to_34_2008 = None
    age_30_to_34_2009 = None
    age_35_to_39_1990 = None
    age_35_to_39_2000 = None
    age_35_to_39_2010 = None
    age_35_to_39_2001 = None
    age_35_to_39_2002 = None
    age_35_to_39_2003 = None
    age_35_to_39_2004 = None
    age_35_to_39_2005 = None
    age_35_to_39_2006 = None
    age_35_to_39_2007 = None
    age_35_to_39_2008 = None
    age_35_to_39_2009 = None
    age_35_to_44_1980 = None
    age_35_to_44_1990 = None
    age_35_to_44_2000 = None
    age_35_to_44_2010 = None
    age_40_to_44_1990 = None
    age_40_to_44_2000 = None
    age_40_to_44_2010 = None
    age_40_to_44_2001 = None
    age_40_to_44_2002 = None
    age_40_to_44_2003 = None
    age_40_to_44_2004 = None
    age_40_to_44_2005 = None
    age_40_to_44_2006 = None
    age_40_to_44_2007 = None
    age_40_to_44_2008 = None
    age_40_to_44_2009 = None
    age_45_to_49_1990 = None
    age_45_to_49_2000 = None
    age_45_to_49_2010 = None
    age_45_to_49_2001 = None
    age_45_to_49_2002 = None
    age_45_to_49_2003 = None
    age_45_to_49_2004 = None
    age_45_to_49_2005 = None
    age_45_to_49_2006 = None
    age_45_to_49_2007 = None
    age_45_to_49_2008 = None
    age_45_to_49_2009 = None
    age_45_to_54_1980 = None
    age_45_to_54_1990 = None
    age_45_to_54_2000 = None
    age_45_to_54_2010 = None
    age_45_to_64_2010 = None
    age_50_to_54_1990 = None
    age_50_to_54_2000 = None
    age_50_to_54_2010 = None
    age_50_to_54_2001 = None
    age_50_to_54_2002 = None
    age_50_to_54_2003 = None
    age_50_to_54_2004 = None
    age_50_to_54_2005 = None
    age_50_to_54_2006 = None
    age_50_to_54_2007 = None
    age_50_to_54_2008 = None
    age_50_to_54_2009 = None
    age_55_to_59_1980 = None
    age_55_to_59_1990 = None
    age_55_to_59_2000 = None
    age_55_to_59_2010 = None
    age_55_to_59_2001 = None
    age_55_to_59_2002 = None
    age_55_to_59_2003 = None
    age_55_to_59_2004 = None
    age_55_to_59_2005 = None
    age_55_to_59_2006 = None
    age_55_to_59_2007 = None
    age_55_to_59_2008 = None
    age_55_to_59_2009 = None
    age_60_to_64_1980 = None
    age_60_to_64_1990 = None
    age_60_to_64_2000 = None
    age_60_to_64_2010 = None
    age_60_to_64_2001 = None
    age_60_to_64_2002 = None
    age_60_to_64_2003 = None
    age_60_to_64_2004 = None
    age_60_to_64_2005 = None
    age_60_to_64_2006 = None
    age_60_to_64_2007 = None
    age_60_to_64_2008 = None
    age_60_to_64_2009 = None
    age_65_to_69_1990 = None
    age_65_to_69_2000 = None
    age_65_to_69_2010 = None
    age_65_to_69_2001 = None
    age_65_to_69_2002 = None
    age_65_to_69_2003 = None
    age_65_to_69_2004 = None
    age_65_to_69_2005 = None
    age_65_to_69_2006 = None
    age_65_to_69_2007 = None
    age_65_to_69_2008 = None
    age_65_to_69_2009 = None
    age_65_to_74_1990 = None
    age_65_to_74_2000 = None
    age_65_to_74_2010 = None
    age_65_and_over_1980 = None
    age_65_and_over_1990 = None
    age_65_and_over_2000 = None
    age_65_and_over_2001 = None
    age_65_and_over_2002 = None
    age_65_and_over_2003 = None
    age_65_and_over_2004 = None
    age_65_and_over_2005 = None
    age_65_and_over_2006 = None
    age_65_and_over_2007 = None
    age_65_and_over_2008 = None
    age_65_and_over_2009 = None
    age_65_and_over_2010 = None
    age_70_to_74_1990 = None
    age_70_to_74_2000 = None
    age_70_to_74_2010 = None
    age_70_to_74_2001 = None
    age_70_to_74_2002 = None
    age_70_to_74_2003 = None
    age_70_to_74_2004 = None
    age_70_to_74_2005 = None
    age_70_to_74_2006 = None
    age_70_to_74_2007 = None
    age_70_to_74_2008 = None
    age_70_to_74_2009 = None
    age_75_to_79_1990 = None
    age_75_to_79_2000 = None
    age_75_to_79_2010 = None
    age_75_to_79_2001 = None
    age_75_to_79_2002 = None
    age_75_to_79_2003 = None
    age_75_to_79_2004 = None
    age_75_to_79_2005 = None
    age_75_to_79_2006 = None
    age_75_to_79_2007 = None
    age_75_to_79_2008 = None
    age_75_to_79_2009 = None
    age_75_to_84_1990 = None
    age_75_to_84_2000 = None
    age_75_to_84_2010 = None
    age_80_to_84_1990 = None
    age_80_to_84_2000 = None
    age_80_to_84_2010 = None
    age_80_to_84_2001 = None
    age_80_to_84_2002 = None
    age_80_to_84_2003 = None
    age_80_to_84_2004 = None
    age_80_to_84_2005 = None
    age_80_to_84_2006 = None
    age_80_to_84_2007 = None
    age_80_to_84_2008 = None
    age_80_to_84_2009 = None
    age_75_and_over_2010 = None
    age_85_and_over_1990 = None
    age_85_and_over_2000 = None
    age_85_and_over_2001 = None
    age_85_and_over_2002 = None
    age_85_and_over_2003 = None
    age_85_and_over_2004 = None
    age_85_and_over_2005 = None
    age_85_and_over_2006 = None
    age_85_and_over_2007 = None
    age_85_and_over_2008 = None
    age_85_and_over_2009 = None
    age_85_and_over_2010 = None
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
        return AgeCounty.fetch_by(database_manager, conditions)

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
        return AgeCounty.fetch_by(database_manager, conditions)


    @staticmethod
    def fetch_by_county_code(database_manager, county_code):
        conditions = [{
            "column": "county_code",
            "equivalence": "=",
            "value": county_code
        }]
        return AgeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by_id(database_manager, id):
        conditions = [{
            "column": "id",
            "equivalence": "=",
            "value": id
        }]
        return AgeCounty.fetch_by(database_manager, conditions)

    @staticmethod
    def fetch_by(database_manager, conditions):
        obj_template = AgeCounty(database_manager)
        results = database_manager.fetch_by(
            obj_template,
            conditions,
            num_rows=1
        )
        if len(results) > 0:
            obj = results[0]
            return obj

