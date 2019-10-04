#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.GenderCounty import GenderCounty


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
    Path("~/Downloads/County Demographic Datasets/SEX01.xls"),
]

header_translations = {
    "Area_name": "city_state",
    "STCOU": "county_code",
    "SEX150200D": "males_2000",
    "SEX150201D": "males_2001",
    "SEX150202D": "males_2002",
    "SEX150203D": "males_2003",
    "SEX150204D": "males_2004",
    "SEX150205D": "males_2005",
    "SEX150206D": "males_2006",
    "SEX150207D": "males_2007",
    "SEX150208D": "males_2008",
    "SEX150209D": "males_2009",
    "SEX100210D": "males_2010",
    "SEX250200D": "females_2000",
    "SEX250201D": "females_2001",
    "SEX250202D": "females_2002",
    "SEX250203D": "females_2003",
    "SEX250204D": "females_2004",
    "SEX250205D": "females_2005",
    "SEX250206D": "females_2006",
    "SEX250207D": "females_2007",
    "SEX250208D": "females_2008",
    "SEX250209D": "females_2009",
    "SEX200210D": "females_2010",
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



gender_data = []
for i in range(0, sheets[0].shape[0]):
    gender_row = GenderCounty(database_manager)
    gender_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Area_name" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(gender_row, output_header, int(sheet[input_header][i]))
        if gender_row.county_code is None:
            gender_row.country_id = country_id
            city_state = sheet["Area_name"][i].split(", ")
            gender_row.county_name = city_state[0]
            gender_row.state_id = None
            gender_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        gender_row.state_id = state.id
                        gender_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Area_name"][i]:
                        gender_row.state_id = state.id
                        gender_row.county_name = None
                        break
            gender_row.county_code = int(sheet["STCOU"][i])
    gender_data.append(gender_row)
            


#for gender_row in gender_data:
#    gender_row.database_manager = database_manager

#for gender_row in gender_data:
#    database_manager.insert(gender_row)

database_manager.insert_many(gender_data)






