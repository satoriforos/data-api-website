#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.usdemographics.GenderCounty import GenderCounty
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country



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


sex_file_path = Path("~/Downloads/County Demographic Datasets/sex-condensed.xlsx")
xls = pd.ExcelFile(sex_file_path.expanduser().as_posix())

header_translations = {
    "Areaname": "city_state",
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
    "SEX250200D": "females_2000",
    "SEX250201D": "females_2001",
    "SEX250202D": "females_2002",
    "SEX250203D": "females_2003",
    "SEX250204D": "females_2004",
    "SEX250205D": "females_2005",
    "SEX250206D": "females_2006",
    "SEX250207D": "females_2007",
    "SEX250208D": "females_2008",
    "SEX250209D": "females_2009"
}

headers = list(header_translations.keys())

sheets = {
    "Sheet1": pd.read_excel(xls, "Sheet1"),
    "Sheet2": pd.read_excel(xls, "Sheet2"),
    "Sheet3": pd.read_excel(xls, "Sheet3"),
    "Sheet4": pd.read_excel(xls, "Sheet4"),
    "Sheet5": pd.read_excel(xls, "Sheet5"),
}

sex_data = []
for i in sheets["Sheet1"].index:
    sex_row = {}
    for sheet in sheets:
        for header in headers:
            if header in sheets[sheet].keys():
                sex_row[header_translations[header]] = sheets[sheet][header][i]
    for key, value in sex_row.items():
        if value == "#" or value == "*" or value == "-" or value == "":
            sex_row[key] = None
    sex_data.append(sex_row)

gender_data = []
for sd in sex_data:
    gender = GenderCounty(database_manager)
    gender.country_id = country_id
    city_state = sd["city_state"].split(", ")
    gender.county_name = city_state[0]
    gender.state_id = None
    gender.state_code = None
    if len(city_state) > 1:
        print(city_state[1])
        for state in us_states:
            if state.code == city_state[1].upper():
                gender.state_id = state.id
                gender.state_code = state.code
                break
    else:
        for state in us_states:
            if state.code.upper() == sd["city_state"]:
                gender.state_id = state.id
                gender.county_name = None
                break
    gender.county_code = int(sd["county_code"])
    for county in us_counties:
        if county.fips == gender.county_code:
            gender.county_code = county.id
            break
    gender.males_2000 = int(sd["males_2000"])
    gender.males_2001 = int(sd["males_2001"])
    gender.males_2002 = int(sd["males_2002"])
    gender.males_2003 = int(sd["males_2003"])
    gender.males_2004 = int(sd["males_2004"])
    gender.males_2005 = int(sd["males_2005"])
    gender.males_2006 = int(sd["males_2006"])
    gender.males_2007 = int(sd["males_2007"])
    gender.males_2008 = int(sd["males_2008"])
    gender.males_2009 = int(sd["males_2009"])
    gender.females_2000 = int(sd["females_2000"])
    gender.females_2001 = int(sd["females_2001"])
    gender.females_2002 = int(sd["females_2002"])
    gender.females_2003 = int(sd["females_2003"])
    gender.females_2004 = int(sd["females_2004"])
    gender.females_2005 = int(sd["females_2005"])
    gender.females_2006 = int(sd["females_2006"])
    gender.females_2007 = int(sd["females_2007"])
    gender.females_2008 = int(sd["females_2008"])
    gender.females_2009 = int(sd["females_2009"])
    gender_data.append(gender)

database_manager.insert_many(gender_data)

