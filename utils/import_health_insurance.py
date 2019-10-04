#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.HealthInsuranceCounty import HealthInsuranceCounty


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
    Path("~/Downloads/County Demographic Datasets/HEA/HEA01.xls"),
    Path("~/Downloads/County Demographic Datasets/HEA/HEA02.xls"),
]

header_translations = {
    "Areaname": "city_state",
    "STCOU": "county_code",
    "HEA610200D": "with_insurance_total_2000",
    "HEA620200D": "no_insurance_total_2000",
    "HEA630200D": "with_insurance_under_18_2000",
    "HEA640200D": "no_insurance_under_18_2000",
    "HEA700205D": "with_insurance_under_18_2005",
    "HEA700206D": "with_insurance_under_18_2006",
    "HEA700207D": "with_insurance_under_18_2007",
    "HEA710205D": "no_insurance_under_18_2005",
    "HEA710206D": "no_insurance_under_18_2006",
    "HEA710207D": "no_insurance_under_18_2007",
    "HEA720205D": "with_insurance_under_18_to_16_2005",
    "HEA720206D": "with_insurance_under_18_to_16_2006",
    "HEA720207D": "with_insurance_under_18_to_16_2007",
    "HEA730205D": "no_insurance_under_18_to_16_2005",
    "HEA730206D": "no_insurance_under_18_to_16_2006",
    "HEA730207D": "no_insurance_under_18_to_16_2007",
    "HEA740205D": "with_insurance_under_40_to_64_2005",
    "HEA740206D": "with_insurance_under_40_to_64_2006",
    "HEA740207D": "with_insurance_under_40_to_64_2007",
    "HEA750205D": "no_insurance_under_40_to_64_2005",
    "HEA750206D": "no_insurance_under_40_to_64_2006",
    "HEA750207D": "no_insurance_under_40_to_64_2007",
    "HEA760205D": "with_insurance_under_65_2005",
    "HEA760206D": "with_insurance_under_65_2006",
    "HEA760207D": "with_insurance_under_65_2007",
    "HEA770205D": "no_insurance_under_65_2005",
    "HEA770206D": "no_insurance_under_65_2006",
    "HEA770207D": "no_insurance_under_65_2007",
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



health_insurance_data = []
for i in range(0, sheets[0].shape[0]):
    health_insurance_row = HealthInsuranceCounty(database_manager)
    health_insurance_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Areaname" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(health_insurance_row, output_header, int(sheet[input_header][i]))
        if health_insurance_row.county_code is None:
            health_insurance_row.country_id = country_id
            city_state = sheet["Areaname"][i].split(", ")
            health_insurance_row.county_name = city_state[0]
            health_insurance_row.state_id = None
            health_insurance_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        health_insurance_row.state_id = state.id
                        health_insurance_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Areaname"][i]:
                        health_insurance_row.state_id = state.id
                        health_insurance_row.county_name = None
                        break
            health_insurance_row.county_code = int(sheet["STCOU"][i])
    health_insurance_data.append(health_insurance_row)
            


#for health_insurance_row in health_insurance_data:
#    health_insurance_row.database_manager = database_manager

for health_insurance_row in health_insurance_data:
    database_manager.insert(health_insurance_row)

database_manager.insert_many(health_insurance_data)





