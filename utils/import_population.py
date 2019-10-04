#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.PopulationCounty import PopulationCounty


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
    Path("~/Downloads/County Demographic Datasets/POP/POP01.xls"),
    Path("~/Downloads/County Demographic Datasets/POP/POP02.xls"),
    Path("~/Downloads/County Demographic Datasets/POP/POP03.xls"),
    Path("~/Downloads/County Demographic Datasets/PST/PST01.xls"),
    Path("~/Downloads/County Demographic Datasets/PST/PST02.xls"),
]

header_translations = {
    "Area_name": "city_state",
    "STCOU": "county_code",
    "POP010130D": "total_1930",
    "POP010140D": "total_1940",
    "POP010150D": "total_1950",
    "POP010160D": "total_1960",
    "POP020170D": "total_1970",
    "POP020180D": "total_1980",
    "POP020190D": "total_1990",
    "POP010200D": "total_2000",
    "POP010210D": "total_2010",
    "PST015171D": "estimate_1971",
    "PST015172D": "estimate_1972",
    "PST015173D": "estimate_1973",
    "PST015174D": "estimate_1974",
    "PST015175D": "estimate_1975",
    "PST015176D": "estimate_1976",
    "PST015177D": "estimate_1977",
    "PST015178D": "estimate_1978",
    "PST015179D": "estimate_1979",
    "PST025181D": "estimate_1981",
    "PST025182D": "estimate_1982",
    "PST025183D": "estimate_1983",
    "PST025184D": "estimate_1984",
    "PST025185D": "estimate_1985",
    "PST025186D": "estimate_1986",
    "PST025187D": "estimate_1987",
    "PST025188D": "estimate_1988",
    "PST025189D": "estimate_1989",
    "PST035190D": "estimate_1990",
    "PST035191D": "estimate_1991",
    "PST035192D": "estimate_1992",
    "PST035193D": "estimate_1993",
    "PST035194D": "estimate_1994",
    "PST035195D": "estimate_1995",
    "PST035196D": "estimate_1996",
    "PST035197D": "estimate_1997",
    "PST035198D": "estimate_1998",
    "PST035199D": "estimate_1999",
    "PST045200D": "estimate_2000",
    "PST045201D": "estimate_2001",
    "PST045202D": "estimate_2002",
    "PST045203D": "estimate_2003",
    "PST045204D": "estimate_2004",
    "PST045205D": "estimate_2005",
    "PST045206D": "estimate_2006",
    "PST045207D": "estimate_2007",
    "PST045208D": "estimate_2008",
    "PST045209D": "estimate_2009"
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



population_data = []
for i in range(0, sheets[0].shape[0]):
    population_row = PopulationCounty(database_manager)
    population_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Area_name" and input_header != "Areaname" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(population_row, output_header, int(sheet[input_header][i]))
        if population_row.county_code is None:
            population_row.country_id = country_id
            city_state = sheet["Area_name"][i].split(", ")
            population_row.county_name = city_state[0]
            population_row.state_id = None
            population_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        population_row.state_id = state.id
                        population_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Area_name"][i]:
                        population_row.state_id = state.id
                        population_row.county_name = None
                        break
            population_row.county_code = int(sheet["STCOU"][i])
    population_data.append(population_row)
            


#for population_row in population_data:
#    population_row.database_manager = database_manager

#for population_row in population_data:
#    database_manager.insert(population_row)

database_manager.insert_many(population_data)




