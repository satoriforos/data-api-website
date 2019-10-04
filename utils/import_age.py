#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.AgeCounty import AgeCounty


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
    Path("~/Downloads/County Demographic Datasets/AGE/AGE01.xls"),
    Path("~/Downloads/County Demographic Datasets/AGE/AGE02.xls"),
    Path("~/Downloads/County Demographic Datasets/AGE/AGE03.xls"),
    Path("~/Downloads/County Demographic Datasets/AGE01/AGE01.xls"),
    Path("~/Downloads/County Demographic Datasets/AGE01/AGE02.xls"),
    Path("~/Downloads/County Demographic Datasets/AGE01/AGE03.xls"),
    Path("~/Downloads/County Demographic Datasets/AGE01/AGE04.xls"),
]

header_translations = {
    "Areaname": "city_state",
    "STCOU": "county_code",
    "AGE010180D": "total_1980",
    "AGE010190D": "total_1990",
    "AGE040200D": "total_2000",
    "AGE040201D": "total_2001",
    "AGE040202D": "total_2002",
    "AGE040203D": "total_2003",
    "AGE040204D": "total_2004",
    "AGE040205D": "total_2005",
    "AGE040206D": "total_2006",
    "AGE040207D": "total_2007",
    "AGE040208D": "total_2008",
    "AGE040209D": "total_2009",
    "AGE010210D": "total_2010",
    "AGE050180D": "median_age_1980",
    "AGE050190D": "median_age_1990",
    "AGE050200D": "median_age_2000",
    "AGE050210D": "median_age_2010",
    "AGE110180D": "under_5_1980",
    "AGE110190D": "under_5_1990",
    "AGE130200D": "under_5_2000",
    "AGE130201D": "under_5_2001",
    "AGE130202D": "under_5_2002",
    "AGE130203D": "under_5_2003",
    "AGE130204D": "under_5_2004",
    "AGE130205D": "under_5_2005",
    "AGE130206D": "under_5_2006",
    "AGE130207D": "under_5_2007",
    "AGE130208D": "under_5_2008",
    "AGE130209D": "under_5_2009",
    "AGE110210D": "under_5_2010",
    "AGE160200D": "age_5_to_9_2000",
    "AGE160201D": "age_5_to_9_2001",
    "AGE160202D": "age_5_to_9_2002",
    "AGE160203D": "age_5_to_9_2003",
    "AGE160204D": "age_5_to_9_2004",
    "AGE160205D": "age_5_to_9_2005",
    "AGE160206D": "age_5_to_9_2006",
    "AGE160207D": "age_5_to_9_2007",
    "AGE160208D": "age_5_to_9_2008",
    "AGE160209D": "age_5_to_9_2009",
    "AGE140210D": "age_5_to_9_2010",
    "AGE170180D": "age_5_to_14_1980",
    "AGE170190D": "age_5_to_14_1990",
    "AGE170210D": "age_5_to_14_2010",
    "AGE180180D": "age_5_to_17_1980",
    "AGE180190D": "age_5_to_17_1990",
    "AGE180200D": "age_5_to_17_2000",
    "AGE180210D": "age_5_to_17_2010",
    "AGE230200D": "age_10_to_14_2000",
    "AGE230201D": "age_10_to_14_2001",
    "AGE230202D": "age_10_to_14_2002",
    "AGE230203D": "age_10_to_14_2003",
    "AGE230204D": "age_10_to_14_2004",
    "AGE230205D": "age_10_to_14_2005",
    "AGE230206D": "age_10_to_14_2006",
    "AGE230207D": "age_10_to_14_2007",
    "AGE230208D": "age_10_to_14_2008",
    "AGE230209D": "age_10_to_14_2009",
    "AGE210210D": "age_10_to_14_2010",
    "AGE260200D": "age_15_to_19_2000",
    "AGE260201D": "age_15_to_19_2001",
    "AGE260202D": "age_15_to_19_2002",
    "AGE260203D": "age_15_to_19_2003",
    "AGE260204D": "age_15_to_19_2004",
    "AGE260205D": "age_15_to_19_2005",
    "AGE260206D": "age_15_to_19_2006",
    "AGE260207D": "age_15_to_19_2007",
    "AGE260208D": "age_15_to_19_2008",
    "AGE260209D": "age_15_to_19_2009",
    "AGE240210D": "age_15_to_19_2010",
    "AGE270180D": "under_18_1980",
    "AGE270190D": "under_18_1990",
    "AGE290200D": "under_18_2000",
    "AGE290201D": "under_18_2001",
    "AGE290202D": "under_18_2002",
    "AGE290203D": "under_18_2003",
    "AGE290204D": "under_18_2004",
    "AGE290205D": "under_18_2005",
    "AGE290206D": "under_18_2006",
    "AGE290207D": "under_18_2007",
    "AGE290208D": "under_18_2008",
    "AGE290209D": "under_18_2009",
    "AGE270210D": "under_18_2010",
    "AGE305210D": "age_18_to_44_2010",
    "AGE310180D": "age_18_and_over_1980",
    "AGE310190D": "age_18_and_over_1990",
    "AGE310210D": "age_18_and_over_2010",
    "AGE320180D": "age_20_to_24_1980",
    "AGE320190D": "age_20_to_24_1990",
    "AGE320210D": "age_20_to_24_2010",
    "AGE340200D": "age_20_to_24_2000",
    "AGE340201D": "age_20_to_24_2001",
    "AGE340202D": "age_20_to_24_2002",
    "AGE340203D": "age_20_to_24_2003",
    "AGE340204D": "age_20_to_24_2004",
    "AGE340205D": "age_20_to_24_2005",
    "AGE340206D": "age_20_to_24_2006",
    "AGE340207D": "age_20_to_24_2007",
    "AGE340208D": "age_20_to_24_2008",
    "AGE340209D": "age_20_to_24_2009",
    "AGE350180D": "age_25_to_29_1980",
    "AGE350190D": "age_25_to_29_1990",
    "AGE350210D": "age_25_to_29_2010",
    "AGE370200D": "age_25_to_29_2000",
    "AGE370201D": "age_25_to_29_2001",
    "AGE370202D": "age_25_to_29_2002",
    "AGE370203D": "age_25_to_29_2003",
    "AGE370204D": "age_25_to_29_2004",
    "AGE370205D": "age_25_to_29_2005",
    "AGE370206D": "age_25_to_29_2006",
    "AGE370207D": "age_25_to_29_2007",
    "AGE370208D": "age_25_to_29_2008",
    "AGE370209D": "age_25_to_29_2009",
    "AGE380180D": "age_25_to_34_1980",
    "AGE380190D": "age_25_to_34_1990",
    "AGE380200D": "age_25_to_34_2000",
    "AGE380210D": "age_25_to_34_2010",
    "AGE410180D": "age_30_to_34_1980",
    "AGE410190D": "age_30_to_34_1990",
    "AGE410210D": "age_30_to_34_2010",
    "AGE430200D": "age_30_to_34_2000",
    "AGE430201D": "age_30_to_34_2001",
    "AGE430202D": "age_30_to_34_2002",
    "AGE430203D": "age_30_to_34_2003",
    "AGE430204D": "age_30_to_34_2004",
    "AGE430205D": "age_30_to_34_2005",
    "AGE430206D": "age_30_to_34_2006",
    "AGE430207D": "age_30_to_34_2007",
    "AGE430208D": "age_30_to_34_2008",
    "AGE430209D": "age_30_to_34_2009",
    "AGE440190D": "age_35_to_39_1990",
    "AGE440210D": "age_35_to_39_2010",
    "AGE460200D": "age_35_to_39_2000",
    "AGE460201D": "age_35_to_39_2001",
    "AGE460202D": "age_35_to_39_2002",
    "AGE460203D": "age_35_to_39_2003",
    "AGE460204D": "age_35_to_39_2004",
    "AGE460205D": "age_35_to_39_2005",
    "AGE460206D": "age_35_to_39_2006",
    "AGE460207D": "age_35_to_39_2007",
    "AGE460208D": "age_35_to_39_2008",
    "AGE460209D": "age_35_to_39_2009",
    "AGE470180D": "age_35_to_44_1980",
    "AGE470190D": "age_35_to_44_1990",
    "AGE470200D": "age_35_to_44_2000",
    "AGE470210D": "age_35_to_44_2010",
    "AGE510190D": "age_40_to_44_1990",
    "AGE510210D": "age_40_to_44_2010",
    "AGE530200D": "age_40_to_44_2000",
    "AGE530201D": "age_40_to_44_2001",
    "AGE530202D": "age_40_to_44_2002",
    "AGE530203D": "age_40_to_44_2003",
    "AGE530204D": "age_40_to_44_2004",
    "AGE530205D": "age_40_to_44_2005",
    "AGE530206D": "age_40_to_44_2006",
    "AGE530207D": "age_40_to_44_2007",
    "AGE530208D": "age_40_to_44_2008",
    "AGE530209D": "age_40_to_44_2009",
    "AGE540190D": "age_45_to_49_1990",
    "AGE540200D": "age_45_to_49_2000",
    "AGE540210D": "age_45_to_49_2010",
    "AGE560200D": "age_45_to_49_2000",
    "AGE560201D": "age_45_to_49_2001",
    "AGE560202D": "age_45_to_49_2002",
    "AGE560203D": "age_45_to_49_2003",
    "AGE560204D": "age_45_to_49_2004",
    "AGE560205D": "age_45_to_49_2005",
    "AGE560206D": "age_45_to_49_2006",
    "AGE560207D": "age_45_to_49_2007",
    "AGE560208D": "age_45_to_49_2008",
    "AGE560209D": "age_45_to_49_2009",
    "AGE570180D": "age_45_to_54_1980",
    "AGE570190D": "age_45_to_54_1990",
    "AGE570200D": "age_45_to_54_2000",
    "AGE570210D": "age_45_to_54_2010",
    "AGE580210D": "age_45_to_64_2010",
    "AGE610190D": "age_50_to_54_1990",
    "AGE610210D": "age_50_to_54_2010",
    "AGE630200D": "age_50_to_54_2000",
    "AGE630201D": "age_50_to_54_2001",
    "AGE630202D": "age_50_to_54_2002",
    "AGE630203D": "age_50_to_54_2003",
    "AGE630204D": "age_50_to_54_2004",
    "AGE630205D": "age_50_to_54_2005",
    "AGE630206D": "age_50_to_54_2006",
    "AGE630207D": "age_50_to_54_2007",
    "AGE630208D": "age_50_to_54_2008",
    "AGE630209D": "age_50_to_54_2009",
    "AGE640180D": "age_55_to_59_1980",
    "AGE640190D": "age_55_to_59_1990",
    "AGE640210D": "age_55_to_59_2010",
    "AGE660200D": "age_55_to_59_2000",
    "AGE660201D": "age_55_to_59_2001",
    "AGE660202D": "age_55_to_59_2002",
    "AGE660203D": "age_55_to_59_2003",
    "AGE660204D": "age_55_to_59_2004",
    "AGE660205D": "age_55_to_59_2005",
    "AGE660206D": "age_55_to_59_2006",
    "AGE660207D": "age_55_to_59_2007",
    "AGE660208D": "age_55_to_59_2008",
    "AGE660209D": "age_55_to_59_2009",
    "AGE670180D": "age_60_to_64_1980",
    "AGE670190D": "age_60_to_64_1990",
    "AGE670210D": "age_60_to_64_2010",
    "AGE690200D": "age_60_to_64_2000",
    "AGE690201D": "age_60_to_64_2001",
    "AGE690202D": "age_60_to_64_2002",
    "AGE690203D": "age_60_to_64_2003",
    "AGE690204D": "age_60_to_64_2004",
    "AGE690205D": "age_60_to_64_2005",
    "AGE690206D": "age_60_to_64_2006",
    "AGE690207D": "age_60_to_64_2007",
    "AGE690208D": "age_60_to_64_2008",
    "AGE690209D": "age_60_to_64_2009",
    "AGE710190D": "age_65_to_69_1990",
    "AGE710210D": "age_65_to_69_2010",
    "AGE730200D": "age_65_to_69_2000",
    "AGE730201D": "age_65_to_69_2001",
    "AGE730202D": "age_65_to_69_2002",
    "AGE730203D": "age_65_to_69_2003",
    "AGE730204D": "age_65_to_69_2004",
    "AGE730205D": "age_65_to_69_2005",
    "AGE730206D": "age_65_to_69_2006",
    "AGE730207D": "age_65_to_69_2007",
    "AGE730208D": "age_65_to_69_2008",
    "AGE730209D": "age_65_to_69_2009",
    "AGE750190D": "age_65_to_74_1990",
    "AGE750200D": "age_65_to_74_2000",
    "AGE750210D": "age_65_to_74_2010",
    "AGE760180D": "age_65_and_over_1980",
    "AGE760190D": "age_65_and_over_1990",
    "AGE770200D": "age_65_and_over_2000",
    "AGE770201D": "age_65_and_over_2001",
    "AGE770202D": "age_65_and_over_2002",
    "AGE770203D": "age_65_and_over_2003",
    "AGE770204D": "age_65_and_over_2004",
    "AGE770205D": "age_65_and_over_2005",
    "AGE770206D": "age_65_and_over_2006",
    "AGE770207D": "age_65_and_over_2007",
    "AGE770208D": "age_65_and_over_2008",
    "AGE770209D": "age_65_and_over_2009",
    "AGE760210D": "age_65_and_over_2010",
    "AGE780190D": "age_70_to_74_1990",
    "AGE780210D": "age_70_to_74_2010",
    "AGE800200D": "age_70_to_74_2000",
    "AGE800201D": "age_70_to_74_2001",
    "AGE800202D": "age_70_to_74_2002",
    "AGE800203D": "age_70_to_74_2003",
    "AGE800204D": "age_70_to_74_2004",
    "AGE800205D": "age_70_to_74_2005",
    "AGE800206D": "age_70_to_74_2006",
    "AGE800207D": "age_70_to_74_2007",
    "AGE800208D": "age_70_to_74_2008",
    "AGE800209D": "age_70_to_74_2009",
    "AGE810190D": "age_75_to_79_1990",
    "AGE810210D": "age_75_to_79_2010",
    "AGE830200D": "age_75_to_79_2000",
    "AGE830201D": "age_75_to_79_2001",
    "AGE830202D": "age_75_to_79_2002",
    "AGE830203D": "age_75_to_79_2003",
    "AGE830204D": "age_75_to_79_2004",
    "AGE830205D": "age_75_to_79_2005",
    "AGE830206D": "age_75_to_79_2006",
    "AGE830207D": "age_75_to_79_2007",
    "AGE830208D": "age_75_to_79_2008",
    "AGE830209D": "age_75_to_79_2009",
    "AGE840190D": "age_75_to_84_1990",
    "AGE840200D": "age_75_to_84_2000",
    "AGE840210D": "age_75_to_84_2010",
    "AGE850190D": "age_80_to_84_1990",
    "AGE850210D": "age_80_to_84_2010",
    "AGE870200D": "age_80_to_84_2000",
    "AGE870201D": "age_80_to_84_2001",
    "AGE870202D": "age_80_to_84_2002",
    "AGE870203D": "age_80_to_84_2003",
    "AGE870204D": "age_80_to_84_2004",
    "AGE870205D": "age_80_to_84_2005",
    "AGE870206D": "age_80_to_84_2006",
    "AGE870207D": "age_80_to_84_2007",
    "AGE870208D": "age_80_to_84_2008",
    "AGE870209D": "age_80_to_84_2009",
    "AGE845210D": "age_75_and_over_2010",
    "AGE880190D": "age_85_and_over_1990",
    "AGE900200D": "age_85_and_over_2000",
    "AGE900201D": "age_85_and_over_2001",
    "AGE900202D": "age_85_and_over_2002",
    "AGE900203D": "age_85_and_over_2003",
    "AGE900204D": "age_85_and_over_2004",
    "AGE900205D": "age_85_and_over_2005",
    "AGE900206D": "age_85_and_over_2006",
    "AGE900207D": "age_85_and_over_2007",
    "AGE900208D": "age_85_and_over_2008",
    "AGE900209D": "age_85_and_over_2009",
    "AGE880210D": "age_85_and_over_2010",
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



age_data = []
for i in range(0, sheets[0].shape[0]):
    age_row = AgeCounty(database_manager)
    age_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Areaname" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(age_row, output_header, int(sheet[input_header][i]))
        if age_row.county_code is None:
            age_row.country_id = country_id
            city_state = sheet["Areaname"][i].split(", ")
            age_row.county_name = city_state[0]
            age_row.state_id = None
            age_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        age_row.state_id = state.id
                        age_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Areaname"][i]:
                        age_row.state_id = state.id
                        age_row.county_name = None
                        break
            age_row.county_code = int(sheet["STCOU"][i])
    age_data.append(age_row)
            


#for age_row in age_data:
#    age_row.database_manager = database_manager

#for age_row in age_data:
#    database_manager.insert(age_row)

database_manager.insert_many(age_data)


