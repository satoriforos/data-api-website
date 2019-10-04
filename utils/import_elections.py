#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.VotesCounty import VotesCounty
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
    Path("~/Downloads/County Demographic Datasets/ELE01.xls"),
]

header_translations = {
    "Areaname": "city_state",
    "STCOU": "county_code",
    "ELE010180D": "total_1980",
    "ELE010184D": "total_1984",
    "ELE010188D": "total_1988",
    "ELE010192D": "total_1992",
    "ELE010196D": "total_1996",
    "ELE010200D": "total_2000",
    "ELE010204D": "total_2004",
    "ELE010208D": "total_2008",
    "ELE020180D": "democratic_1980",
    "ELE020184D": "democratic_1984",
    "ELE020188D": "democratic_1988",
    "ELE020192D": "democratic_1992",
    "ELE020196D": "democratic_1996",
    "ELE020200D": "democratic_2000",
    "ELE020204D": "democratic_2004",
    "ELE020208D": "democratic_2008",
    "ELE030180D": "republican_1980",
    "ELE030184D": "republican_1984",
    "ELE030188D": "republican_1988",
    "ELE030192D": "republican_1992",
    "ELE030196D": "republican_1996",
    "ELE030200D": "republican_2000",
    "ELE030204D": "republican_2004",
    "ELE030208D": "republican_2008",
    "ELE060180D": "other_1980",
    "ELE060184D": "other_1984",
    "ELE060188D": "other_1988",
    "ELE060192D": "other_1992",
    "ELE060196D": "other_1996",
    "ELE060200D": "other_2000",
    "ELE060204D": "other_2004",
    "ELE060208D": "other_2008",
}


    """
    "ELE010180D": "total_1980",
    "ELE010184D": "total_1984",
    "ELE010188D": "total_1988",
    "ELE010192D": "total_1992",
    "ELE010196D": "total_1996",
    "ELE010200D": "total_2000",
    "ELE010204D": "total_2004",
    "ELE010208D": "total_2008",
    "ELE020180D": "democrat_1980",
    "ELE020184D": "democrat_1984",
    "ELE020188D": "democrat_1988",
    "ELE020192D": "democrat_1992",
    "ELE020196D": "democrat_1996",
    "ELE020200D": "democrat_2000",
    "ELE020204D": "democrat_2004",
    "ELE020208D": "democrat_2008",
    "ELE030180D": "republican_1980",
    "ELE030184D": "republican_1984",
    "ELE030188D": "republican_1988",
    "ELE030192D": "republican_1992",
    "ELE030196D": "republican_1996",
    "ELE030200D": "republican_2000",
    "ELE030204D": "republican_2004",
    "ELE030208D": "republican_2008",
    "ELE060180D": "other_1980",
    "ELE060184D": "other_1984",
    "ELE060188D": "other_1988",
    "ELE060192D": "other_1992",
    "ELE060196D": "other_1996",
    "ELE060200D": "other_2000",
    "ELE060204D": "other_2004",
    "ELE060208D": "other_2008",
    """

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



votes_data = []
for i in range(0, sheets[0].shape[0]):
    votes_row = VotesCounty(database_manager)
    votes_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Areaname" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(votes_row, output_header, int(sheet[input_header][i]))
        if votes_row.county_code is None:
            votes_row.country_id = country_id
            city_state = sheet["Areaname"][i].split(", ")
            votes_row.county_name = city_state[0]
            votes_row.state_id = None
            votes_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        votes_row.state_id = state.id
                        votes_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Areaname"][i]:
                        votes_row.state_id = state.id
                        votes_row.county_name = None
                        break
            votes_row.county_code = int(sheet["STCOU"][i])
    votes_data.append(votes_row)

database_manager.insert_many(votes_data)

populations = database_manager.fetch_all(PopulationCounty(database_manager))

# must get the number of people living there at that time

real_votes_data = []
for vote_row in votes_data:
    for population in populations:
        if population.county_code == vote_row.county_code and \
                population.county_name == vote_row.county_name:
            total_1980 = population.total_1980
            total_1984 = population.estimate_1984
            total_1988 = population.estimate_1988
            total_1992 = population.estimate_1992
            total_1996 = population.estimate_1996
            total_2000 = population.total_2000
            total_2004 = population.estimate_2004
            total_2008 = population.estimate_2008
    v = VotesCounty(database_manager)
    if total_1980 > 0:
        v.percent_voted_1980 = vote_row.total_1980 / total_1980
        v.percent_other_1980 = vote_row.other_1980 / total_1980
        v.percent_democrat_1980 = vote_row.democrat_1980 / total_1980
        v.percent_republican_1980 = vote_row.republican_1980 / total_1980
    else:
        v.percent_voted_1980 = 0
        v.percent_other_1980 = 0
        v.percent_democrat_1980 = 0
        v.percent_republican_1980 = 0
    if total_1984 > 0:
        v.percent_voted_1984 = vote_row.total_1984 / total_1984
        v.percent_other_1984 = vote_row.other_1984 / total_1984
        v.percent_democrat_1984 = vote_row.democrat_1984 / total_1984
        v.percent_republican_1984 = vote_row.republican_1984 / total_1984
    else:
        v.percent_voted_1984 = 0
        v.percent_other_1984 = 0
        v.percent_democrat_1984 = 0
        v.percent_republican_1984 = 0
    if total_1988 > 0:
        v.percent_voted_1988 = vote_row.total_1988 / total_1988
        v.percent_other_1988 = vote_row.other_1988 / total_1988
        v.percent_democrat_1988 = vote_row.democrat_1988 / total_1988
        v.percent_republican_1988 = vote_row.republican_1988 / total_1988
    else:
        v.percent_voted_1988 = 0
        v.percent_other_1988 = 0
        v.percent_democrat_1988 = 0
        v.percent_republican_1988 = 0
    if total_1992 > 0:
        v.percent_voted_1992 = vote_row.total_1992 / total_1992
        v.percent_other_1992 = vote_row.other_1992 / total_1992
        v.percent_democrat_1992 = vote_row.democrat_1992 / total_1992
        v.percent_republican_1992 = vote_row.republican_1992 / total_1992
    else:
        v.percent_voted_1992 = 0
        v.percent_other_1992 = 0
        v.percent_democrat_1992 = 0
        v.percent_republican_1992 = 0
    if total_1996 > 0:
        v.percent_voted_1996 = vote_row.total_1996 / total_1996
        v.percent_other_1996 = vote_row.other_1996 / total_1996
        v.percent_democrat_1996 = vote_row.democrat_1996 / total_1996
        v.percent_republican_1996 = vote_row.republican_1996 / total_1996
    else:
        v.percent_voted_1996 = 0
        v.percent_other_1996 = 0
        v.percent_democrat_1996 = 0
        v.percent_republican_1996 = 0
    if total_2000 > 0:
        v.percent_voted_2000 = vote_row.total_2000 / total_2000
        v.percent_other_2000 = vote_row.other_2000 / total_2000
        v.percent_democrat_2000 = vote_row.democrat_2000 / total_2000
        v.percent_republican_2000 = vote_row.republican_2000 / total_2000
    else:
        v.percent_voted_2000 = 0
        v.percent_other_2000 = 0
        v.percent_democrat_2000 = 0
        v.percent_republican_2000 = 0
    if total_2004 > 0:
        v.percent_voted_2004 = vote_row.total_2004 / total_2004
        v.percent_other_2004 = vote_row.other_2004 / total_2004
        v.percent_democrat_2004 = vote_row.democrat_2004 / total_2004
        v.percent_republican_2004 = vote_row.republican_2004 / total_2004
    else:
        v.percent_voted_2004 = 0
        v.percent_other_2004 = 0
        v.percent_democrat_2004 = 0
        v.percent_republican_2004 = 0
    if total_2008 > 0:
        v.percent_voted_2008 = vote_row.total_2008 / total_2008
        v.percent_other_2008 = vote_row.other_2008 / total_2008
        v.percent_democrat_2008 = vote_row.democrat_2008 / total_2008
        v.percent_republican_2008 = vote_row.republican_2008 / total_2008
    else:
        v.percent_voted_2008 = 0
        v.percent_other_2008 = 0
        v.percent_democrat_2008 = 0
        v.percent_republican_2008 = 0
    v.country_id = vote_row.country_id
    v.county_name = vote_row.county_name
    v.state_id = vote_row.state_id
    v.state_code = vote_row.state_code
    v.county_code = vote_row.county_code
    real_votes_data.append(v)

    # calculatte voting rates


#for votes_row in votes_data:
#    votes_row.database_manager = database_manager

#for votes_row in votes_data:
#    database_manager.insert(votes_row)

database_manager.insert_many(votes_data)














