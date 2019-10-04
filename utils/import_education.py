#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.EducationCounty import EducationCounty


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
    Path("~/Downloads/County Demographic Datasets/EDU/EDU01.xls"),
    Path("~/Downloads/County Demographic Datasets/EDU/EDU02.xls"),
]

header_translations = {
    "Area_name": "city_state",
    "STCOU": "county_code",
    "EDU600180D": "num_adults_1980",
    "EDU600190D": "num_adults_1990",
    "EDU600200D": "num_adults_2000",
    "EDU600209D": "num_adults_2005_2009",
    "EDU610190D": "less_than_grade_9_1990",
    "EDU610200D": "less_than_grade_9_2000",
    "EDU610209D": "less_than_grade_9_2005_2009",
    "EDU620190D": "grade_9_to_12_no_diploma_1990",
    "EDU620200D": "grade_9_to_12_no_diploma_2000",
    "EDU620209D": "grade_9_to_12_no_diploma_2005_2009",
    "EDU640190D": "high_school_graduate_1990",
    "EDU640200D": "high_school_graduate_2000",
    "EDU640209D": "high_school_graduate_2005_2009",
    "EDU650190D": "some_college_or_associate_degree_1990",
    "EDU650200D": "some_college_or_associate_degree_2000",
    "EDU660200D": "incomplete_college_2000",
    "EDU660209D": "incomplete_college_2005_2009",
    "EDU670200D": "associate_degree_2000",
    "EDU670209D": "associate_degree_2005_2009",
    "EDU680190D": "any_college_degree_1990",
    "EDU680200D": "any_college_degree_2000",
    "EDU690200D": "bachelors_degree_2000",
    "EDU690209D": "bachelors_degree_2005_2009",
    "EDU695200D": "graduate_degree_2000",
    "EDU695209D": "graduate_degree_2005_2009",
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


education_data = []
for i in range(0, sheets[0].shape[0]):
    education_row = EducationCounty(database_manager)
    education_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Area_name" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(education_row, output_header, int(sheet[input_header][i]))
        if education_row.county_code is None:
            education_row.country_id = country_id
            city_state = sheet["Area_name"][i].split(", ")
            education_row.county_name = city_state[0]
            education_row.state_id = None
            education_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        education_row.state_id = state.id
                        education_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Area_name"][i]:
                        education_row.state_id = state.id
                        education_row.county_name = None
                        break
            education_row.county_code = int(sheet["STCOU"][i])
    education_data.append(education_row)
            


#for education_row in education_data:
#    education_row.database_manager = database_manager

#for education_row in education_data:
#    database_manager.insert(education_row)

database_manager.insert_many(education_data)


