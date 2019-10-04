#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.AncestryCounty import AncestryCounty


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
    Path("~/Downloads/County Demographic Datasets/ANC/ANC01.xls"),
    Path("~/Downloads/County Demographic Datasets/ANC/ANC02.xls"),
    Path("~/Downloads/County Demographic Datasets/ANC/ANC03.xls"),
]

header_translations = {
    "Area_name": "city_state",
    "STCOU": "county_code",
    "ANC700190D": "total_1990",
    "ANC700200D": "total_2000",
    "ANC700209D": "total_2009",
    "ANC710190D": "american_1990",
    "ANC710200D": "american_2000",
    "ANC710209D": "american_2009",
    "ANC715190D": "arab_1990",
    "ANC715200D": "arab_2000",
    "ANC715209D": "arab_2009",
    "ANC720209D": "british_2009",
    "ANC730190D": "czech_1990",
    "ANC730200D": "czech_2000",
    "ANC730209D": "czech_2009",
    "ANC735190D": "danish_1990",
    "ANC735200D": "danish_2000",
    "ANC735209D": "danish_2009",
    "ANC740190D": "dutch_1990",
    "ANC740200D": "dutch_2000",
    "ANC740209D": "dutch_2009",
    "ANC745190D": "english_1990",
    "ANC745200D": "english_2000",
    "ANC745209D": "english_2009",
    "ANC750209D": "european_2009",
    "ANC755190D": "french_1990",
    "ANC755200D": "french_2000",
    "ANC755209D": "french_2009",
    "ANC760190D": "french_canadian_1990",
    "ANC760200D": "french_canadian_2000",
    "ANC760209D": "french_canadian_2009",
    "ANC765190D": "german_1990",
    "ANC765200D": "german_2000",
    "ANC765209D": "german_2009",
    "ANC770190D": "greek_1990",
    "ANC770200D": "greek_2000",
    "ANC770209D": "greek_2009",
    "ANC775190D": "hungarian_1990",
    "ANC775200D": "hungarian_2000",
    "ANC775209D": "hungarian_2009",
    "ANC780190D": "irish_1990",
    "ANC780200D": "irish_2000",
    "ANC780209D": "irish_2009",
    "ANC785190D": "italian_1990",
    "ANC785200D": "italian_2000",
    "ANC785209D": "italian_2009",
    "ANC790190D": "lithuanian_1990",
    "ANC790200D": "lithuanian_2000",
    "ANC790209D": "lithuanian_2009",
    "ANC795190D": "norwegian_1990",
    "ANC795200D": "norwegian_2000",
    "ANC795209D": "norwegian_2009",
    "ANC800190D": "polish_1990",
    "ANC800200D": "polish_2000",
    "ANC800209D": "polish_2009",
    "ANC805190D": "portuguese_1990",
    "ANC805200D": "portuguese_2000",
    "ANC805209D": "portuguese_2009",
    "ANC815190D": "russian_1990",
    "ANC815200D": "russian_2000",
    "ANC815209D": "russian_2009",
    "ANC820190D": "scotch_irish_1990",
    "ANC820200D": "scotch_irish_2000",
    "ANC820209D": "scotch_irish_2009",
    "ANC825190D": "scottish_1990",
    "ANC825200D": "scottish_2000",
    "ANC825209D": "scottish_2009",
    "ANC830190D": "slovak_1990",
    "ANC830200D": "slovak_2000",
    "ANC830209D": "slovak_2009",
    "ANC835190D": "subsaharan_african_1990",
    "ANC835200D": "subsaharan_african_2000",
    "ANC835209D": "subsaharan_african_2009",
    "ANC840190D": "swedish_1990",
    "ANC840200D": "swedish_2000",
    "ANC840209D": "swedish_2009",
    "ANC845190D": "swiss_1990",
    "ANC845200D": "swiss_2000",
    "ANC845209D": "swiss_2009",
    "ANC850190D": "ukrainian_1990",
    "ANC850200D": "ukrainian_2000",
    "ANC850209D": "ukrainian_2009",
    "ANC860190D": "welsh_1990",
    "ANC860200D": "welsh_2000",
    "ANC860209D": "welsh_2009",
    "ANC865190D": "west_indian_1990",
    "ANC865200D": "west_indian_2000",
    "ANC865209D": "west_indian_2009",
    "ANC880190D": "other_1990",
    "ANC880200D": "other_2000",
    "ANC880209D": "other_groups_2009"
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



ancestry_data = []
for i in range(0, sheets[0].shape[0]):
    ancestry_row = AncestryCounty(database_manager)
    ancestry_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Area_name" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(ancestry_row, output_header, int(sheet[input_header][i]))
        if ancestry_row.county_code is None:
            ancestry_row.country_id = country_id
            city_state = sheet["Area_name"][i].split(", ")
            ancestry_row.county_name = city_state[0]
            ancestry_row.state_id = None
            ancestry_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        ancestry_row.state_id = state.id
                        ancestry_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Area_name"][i]:
                        ancestry_row.state_id = state.id
                        ancestry_row.county_name = None
                        break
            ancestry_row.county_code = int(sheet["STCOU"][i])
    ancestry_data.append(ancestry_row)
            


#for ancestry_row in ancestry_data:
#    ancestry_row.database_manager = database_manager

#for ancestry_row in ancestry_data:
#    database_manager.insert(ancestry_row)

database_manager.insert_many(ancestry_data)




