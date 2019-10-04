#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.RaceCounty import RaceCounty


def get_database_connection(mysql_settings):
    database_manager = DatabaseManager(
        host=mysql_settings["server"],
        port=mysql_settings["port"],
        user=mysql_settings["username"],
        password=mysql_settings["password"],
        db=mysql_settings["schema"],
        charset=mysql_settings["charset"]
    )
    return database_manager


database_manager = get_database_connection(settings["mysql"])

us_counties = database_manager.fetch_all(UsCounty(database_manager))
cities = database_manager.fetch_all(City(database_manager))
us_states = database_manager.fetch_all(UsState(database_manager))
countries = database_manager.fetch_all(Country(database_manager))

country_id = None
for country in countries:
    if country.code == "US":
        country_id = country.id
        break


file_paths = [
    Path("~/Downloads/County Demographic Datasets/RHI/RHI01.xls"),
    Path("~/Downloads/County Demographic Datasets/RHI/RHI02.xls"),
]

header_translations = {
    "Areaname": "city_state",
    "STCOU": "county_code",
    "RHI125200D": "white_2000",
    "RHI125201D": "white_2001",
    "RHI125202D": "white_2002",
    "RHI125203D": "white_2003",
    "RHI125204D": "white_2004",
    "RHI125205D": "white_2005",
    "RHI125206D": "white_2006",
    "RHI125207D": "white_2007",
    "RHI125208D": "white_2008",
    "RHI125209D": "white_2009",
    "RHI105210D": "white_2010",
    "RHI225200D": "black_2000",
    "RHI225201D": "black_2001",
    "RHI225202D": "black_2002",
    "RHI225203D": "black_2003",
    "RHI225204D": "black_2004",
    "RHI225205D": "black_2005",
    "RHI225206D": "black_2006",
    "RHI225207D": "black_2007",
    "RHI225208D": "black_2008",
    "RHI225209D": "black_2009",
    "RHI205210D": "black_2010",
    "RHI325200D": "aboriginal_alaskan_2000",
    "RHI325201D": "aboriginal_alaskan_2001",
    "RHI325202D": "aboriginal_alaskan_2002",
    "RHI325203D": "aboriginal_alaskan_2003",
    "RHI325204D": "aboriginal_alaskan_2004",
    "RHI325205D": "aboriginal_alaskan_2005",
    "RHI325206D": "aboriginal_alaskan_2006",
    "RHI325207D": "aboriginal_alaskan_2007",
    "RHI325208D": "aboriginal_alaskan_2008",
    "RHI325209D": "aboriginal_alaskan_2009",
    "RHI305210D": "aboriginal_alaskan_2010",
    "RHI425200D": "asian_2000",
    "RHI425201D": "asian_2001",
    "RHI425202D": "asian_2002",
    "RHI425203D": "asian_2003",
    "RHI425204D": "asian_2004",
    "RHI425205D": "asian_2005",
    "RHI425206D": "asian_2006",
    "RHI425207D": "asian_2007",
    "RHI425208D": "asian_2008",
    "RHI425209D": "asian_2009",
    "RHI405210D": "asian_2010",
    "RHI525200D": "hawaiian_pacific_islander2000",
    "RHI525201D": "hawaiian_pacific_islander2001",
    "RHI525202D": "hawaiian_pacific_islander2002",
    "RHI525203D": "hawaiian_pacific_islander2003",
    "RHI525204D": "hawaiian_pacific_islander2004",
    "RHI525205D": "hawaiian_pacific_islander2005",
    "RHI525206D": "hawaiian_pacific_islander2006",
    "RHI525207D": "hawaiian_pacific_islander2007",
    "RHI525208D": "hawaiian_pacific_islander2008",
    "RHI525209D": "hawaiian_pacific_islander2009",
    "RHI505210D": "hawaiian_pacific_islander2010",
    "RHI625200D": "mixed_2000",
    "RHI625201D": "mixed_2001",
    "RHI625202D": "mixed_2002",
    "RHI625203D": "mixed_2003",
    "RHI625204D": "mixed_2004",
    "RHI625205D": "mixed_2005",
    "RHI625206D": "mixed_2006",
    "RHI625207D": "mixed_2007",
    "RHI625208D": "mixed_2008",
    "RHI625209D": "mixed_2009",
    "RHI605210D": "mixed_2010",
    "RHI725200D": "hispanic_latino_2000",
    "RHI725201D": "hispanic_latino_2001",
    "RHI725202D": "hispanic_latino_2002",
    "RHI725203D": "hispanic_latino_2003",
    "RHI725204D": "hispanic_latino_2004",
    "RHI725205D": "hispanic_latino_2005",
    "RHI725206D": "hispanic_latino_2006",
    "RHI725207D": "hispanic_latino_2007",
    "RHI725208D": "hispanic_latino_2008",
    "RHI725209D": "hispanic_latino_2009",
    "RHI705210D": "hispanic_latino_2010",
    "RHI825200D": "white_non_hispanic_2000",
    "RHI825201D": "white_non_hispanic_2001",
    "RHI825202D": "white_non_hispanic_2002",
    "RHI825203D": "white_non_hispanic_2003",
    "RHI825204D": "white_non_hispanic_2004",
    "RHI825205D": "white_non_hispanic_2005",
    "RHI825206D": "white_non_hispanic_2006",
    "RHI825207D": "white_non_hispanic_2007",
    "RHI825208D": "white_non_hispanic_2008",
    "RHI825209D": "white_non_hispanic_2009",
    "RHI805210D": "white_non_hispanic_2010"
}





header_translations = {
    "RHI120200D": "white_2000",
    "RHI120201D": "white_2001",
    "RHI120202D": "white_2002",
    "RHI120203D": "white_2003",
    "RHI120204D": "white_2004",
    "RHI120205D": "white_2005",
    "RHI120206D": "white_2006",
    "RHI120207D": "white_2007",
    "RHI120208D": "white_2008",
    "RHI120209D": "white_2009",
    "RHI100210D": "white_2010",
    "RHI220200D": "black_2000",
    "RHI220201D": "black_2001",
    "RHI220202D": "black_2002",
    "RHI220203D": "black_2003",
    "RHI220204D": "black_2004",
    "RHI220205D": "black_2005",
    "RHI220206D": "black_2006",
    "RHI220207D": "black_2007",
    "RHI220208D": "black_2008",
    "RHI220209D": "black_2009",
    "RHI200210D": "black_2010",
    "RHI320200D": "aboriginal_alaskan_2000",
    "RHI320201D": "aboriginal_alaskan_2001",
    "RHI320202D": "aboriginal_alaskan_2002",
    "RHI320203D": "aboriginal_alaskan_2003",
    "RHI320204D": "aboriginal_alaskan_2004",
    "RHI320205D": "aboriginal_alaskan_2005",
    "RHI320206D": "aboriginal_alaskan_2006",
    "RHI320207D": "aboriginal_alaskan_2007",
    "RHI320208D": "aboriginal_alaskan_2008",
    "RHI320209D": "aboriginal_alaskan_2009",
    "RHI300210D": "aboriginal_alaskan_2010",
    "RHI420200D": "asian_2000",
    "RHI420201D": "asian_2001",
    "RHI420202D": "asian_2002",
    "RHI420203D": "asian_2003",
    "RHI420204D": "asian_2004",
    "RHI420205D": "asian_2005",
    "RHI420206D": "asian_2006",
    "RHI420207D": "asian_2007",
    "RHI420208D": "asian_2008",
    "RHI420209D": "asian_2009",
    "RHI400210D": "asian_2010",
    "RHI520200D": "hawaiian_pacific_islander_2000",
    "RHI520201D": "hawaiian_pacific_islander_2001",
    "RHI520202D": "hawaiian_pacific_islander_2002",
    "RHI520203D": "hawaiian_pacific_islander_2003",
    "RHI520204D": "hawaiian_pacific_islander_2004",
    "RHI520205D": "hawaiian_pacific_islander_2005",
    "RHI520206D": "hawaiian_pacific_islander_2006",
    "RHI520207D": "hawaiian_pacific_islander_2007",
    "RHI520208D": "hawaiian_pacific_islander_2008",
    "RHI520209D": "hawaiian_pacific_islander_2009",
    "RHI500210D": "hawaiian_pacific_islander_2010",
    "RHI620200D": "mixed_2000",
    "RHI620201D": "mixed_2001",
    "RHI620202D": "mixed_2002",
    "RHI620203D": "mixed_2003",
    "RHI620204D": "mixed_2004",
    "RHI620205D": "mixed_2005",
    "RHI620206D": "mixed_2006",
    "RHI620207D": "mixed_2007",
    "RHI620208D": "mixed_2008",
    "RHI620209D": "mixed_2009",
    "RHI600210D": "mixed_2010",
    "RHI720200D": "hispanic_latino_2000",
    "RHI720201D": "hispanic_latino_2001",
    "RHI720202D": "hispanic_latino_2002",
    "RHI720203D": "hispanic_latino_2003",
    "RHI720204D": "hispanic_latino_2004",
    "RHI720205D": "hispanic_latino_2005",
    "RHI720206D": "hispanic_latino_2006",
    "RHI720207D": "hispanic_latino_2007",
    "RHI720208D": "hispanic_latino_2008",
    "RHI720209D": "hispanic_latino_2009",
    "RHI700210D": "hispanic_latino_2010",
    "RHI820200D": "white_non_hispanic_2000",
    "RHI820201D": "white_non_hispanic_2001",
    "RHI820202D": "white_non_hispanic_2002",
    "RHI820203D": "white_non_hispanic_2003",
    "RHI820204D": "white_non_hispanic_2004",
    "RHI820205D": "white_non_hispanic_2005",
    "RHI820206D": "white_non_hispanic_2006",
    "RHI820207D": "white_non_hispanic_2007",
    "RHI820208D": "white_non_hispanic_2008",
    "RHI820209D": "white_non_hispanic_2009",
    "RHI800210D": "white_non_hispanic_2010",
}

headers = list(header_translations.keys())

excel_files = [
    pd.ExcelFile(file_path.expanduser().as_posix())
    for file_path in file_paths
]
sheets = []
for excel_file in excel_files:
    sheet_names = excel_file.sheet_names
    for sheet_name in sheet_names:
        sheets.append(pd.read_excel(excel_file, sheet_name))

race_data = []
for i in range(0, sheets[0].shape[0]):
    race_row = RaceCounty(database_manager)
    race_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Area_name" and input_header != "Areaname" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(race_row, output_header, int(sheet[input_header][i]))
        if race_row.county_code is None:
            race_row.country_id = country_id
            city_state = sheet["Areaname"][i].split(", ")
            race_row.county_name = city_state[0]
            race_row.state_id = None
            race_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        race_row.state_id = state.id
                        race_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Areaname"][i]:
                        race_row.state_id = state.id
                        race_row.county_name = None
                        break
            race_row.county_code = int(sheet["STCOU"][i])
    race_data.append(race_row)

for race_row in race_data:
    race_row.database_manager = database_manager


for race_row in race_data:
    database_manager.insert(race_row)


database_manager.insert_many(race_data)


