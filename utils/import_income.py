#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.IncomeCounty import IncomeCounty


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
    Path("~/Downloads/County Demographic Datasets/INC/INC01.xls"),
    Path("~/Downloads/County Demographic Datasets/INC/INC02.xls"),
    Path("~/Downloads/County Demographic Datasets/INC/INC03.xls"),
]

header_translations = {
    "Area_name": "city_state",
    "STCOU": "county_code",
    "INC110179D": "median_1979",
    "INC110189D": "median_1989",
    "INC110199D": "median_1999",
    "INC150179D": "less_than_10000_1979",
    "INC150189D": "less_than_10000_1989",
    "INC150199D": "less_than_10000_1999",
    "INC170179D": "between_10000_and_14999_1979",
    "INC170189D": "between_10000_and_14999_1989",
    "INC170199D": "between_10000_and_14999_1999",
    "INC180179D": "between_15000_and_19999_1979",
    "INC180189D": "between_15000_and_19999_1989",
    "INC180199D": "between_15000_and_19999_1999",
    "INC190179D": "between_20000_and_24999_1979",
    "INC190189D": "between_20000_and_24999_1989",
    "INC190199D": "between_20000_and_24999_1999",
    "INC200179D": "between_25000_and_29999_1979",
    "INC200189D": "between_25000_and_29999_1989",
    "INC200199D": "between_25000_and_29999_1999",
    "INC210179D": "between_30000_and_34999_1979",
    "INC210189D": "between_30000_and_34999_1989",
    "INC210199D": "between_30000_and_34999_1999",
    "INC220179D": "between_35000_and_39999_1979",
    "INC220189D": "between_35000_and_39999_1989",
    "INC220199D": "between_35000_and_39999_1999",
    "INC230179D": "between_40000_and_49999_1979",
    "INC230189D": "between_40000_and_49999_1989",
    "INC230199D": "between_40000_and_49999_1999",
    "INC240189D": "between_40000_and_44999_1989",
    "INC240199D": "between_40000_and_44999_1999",
    "INC250189D": "between_45000_and_49999_1989",
    "INC250199D": "between_45000_and_49999_1999",
    "INC260179D": "between_50000_and_74999_1979",
    "INC260189D": "between_50000_and_74999_1989",
    "INC260199D": "between_50000_and_74999_1999",
    "INC270189D": "between_50000_and_59999_1989",
    "INC270199D": "between_50000_and_59999_1999",
    "INC280189D": "between_60000_and_74999_1989",
    "INC280199D": "between_60000_and_74999_1999",
    "INC290179D": "over_75000_1979",
    "INC290189D": "over_75000_1989",
    "INC290199D": "over_75000_1999",
    "INC300189D": "between_75000_and_99999_1989",
    "INC300199D": "between_75000_and_99999_1999",
    "INC310189D": "between_100000_and_124999_1989",
    "INC310199D": "between_100000_and_124999_1999",
    "INC320189D": "between_125000_and_149999_1989",
    "INC320199D": "between_125000_and_149999_1999",
    "INC330189D": "over_150000_1989",
    "INC330199D": "over_150000_1999",
    "INC340199D": "between_150000_and_199999_1999",
    "INC350199D": "over_200000_1999"
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



income_data = []
for i in range(0, sheets[0].shape[0]):
    income_row = IncomeCounty(database_manager)
    income_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Area_name" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(income_row, output_header, int(sheet[input_header][i]))
        if income_row.county_code is None:
            income_row.country_id = country_id
            city_state = sheet["Area_name"][i].split(", ")
            income_row.county_name = city_state[0]
            income_row.state_id = None
            income_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        income_row.state_id = state.id
                        income_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Area_name"][i]:
                        income_row.state_id = state.id
                        income_row.county_name = None
                        break
            income_row.county_code = int(sheet["STCOU"][i])
    income_data.append(income_row)
            


#for income_row in income_data:
#    income_row.database_manager = database_manager

#for income_row in income_data:
#    database_manager.insert(income_row)

database_manager.insert_many(income_data)






