#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from settings.settings import settings
from modules.databasemanager.DatabaseManager import DatabaseManager
from modules.geolocation.UsCounty import UsCounty
from modules.geolocation.City import City
from modules.geolocation.UsState import UsState
from modules.geolocation.Country import Country
from modules.usdemographics.CrimeCounty import CrimeCounty


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
    Path("~/Downloads/County Demographic Datasets/CRM/CRM01.xls"),
    Path("~/Downloads/County Demographic Datasets/CRM/CRM02.xls"),
    Path("~/Downloads/County Demographic Datasets/CRM/CRM03.xls"),
]

header_translations = {
    "Areaname": "city_state",
    "STCOU": "county_code",
    "CRM110181D": "violent_crimes_1981",
    "CRM110182D": "violent_crimes_1982",
    "CRM110183D": "violent_crimes_1983",
    "CRM110184D": "violent_crimes_1984",
    "CRM110185D": "violent_crimes_1985",
    "CRM110186D": "violent_crimes_1986",
    "CRM110187D": "violent_crimes_1987",
    "CRM110188D": "violent_crimes_1988",
    "CRM110189D": "violent_crimes_1989",
    "CRM110190D": "violent_crimes_1990",
    "CRM110191D": "violent_crimes_1991",
    "CRM110192D": "violent_crimes_1992",
    "CRM110193D": "violent_crimes_1993",
    "CRM110194D": "violent_crimes_1994",
    "CRM110195D": "violent_crimes_1995",
    "CRM110196D": "violent_crimes_1996",
    "CRM110197D": "violent_crimes_1997",
    "CRM110198D": "violent_crimes_1998",
    "CRM110199D": "violent_crimes_1999",
    "CRM110200D": "violent_crimes_2000",
    "CRM110201D": "violent_crimes_2001",
    "CRM110202D": "violent_crimes_2002",
    "CRM110203D": "violent_crimes_2003",
    "CRM110204D": "violent_crimes_2004",
    "CRM110205D": "violent_crimes_2005",
    "CRM110206D": "violent_crimes_2006",
    "CRM110207D": "violent_crimes_2007",
    "CRM110208D": "violent_crimes_2008",
    "CRM140190D": "murders_1990",
    "CRM140191D": "murders_1991",
    "CRM140192D": "murders_1992",
    "CRM140193D": "murders_1993",
    "CRM140194D": "murders_1994",
    "CRM140195D": "murders_1995",
    "CRM140196D": "murders_1996",
    "CRM140197D": "murders_1997",
    "CRM140198D": "murders_1998",
    "CRM140199D": "murders_1999",
    "CRM140200D": "murders_2000",
    "CRM140201D": "murders_2001",
    "CRM140202D": "murders_2002",
    "CRM140203D": "murders_2003",
    "CRM140204D": "murders_2004",
    "CRM140205D": "murders_2005",
    "CRM140206D": "murders_2006",
    "CRM140207D": "murders_2007",
    "CRM140208D": "murders_2008",
    "CRM150190D": "forcible_rapes_1990",
    "CRM150191D": "forcible_rapes_1991",
    "CRM150192D": "forcible_rapes_1992",
    "CRM150193D": "forcible_rapes_1993",
    "CRM150194D": "forcible_rapes_1994",
    "CRM150195D": "forcible_rapes_1995",
    "CRM150196D": "forcible_rapes_1996",
    "CRM150197D": "forcible_rapes_1997",
    "CRM150198D": "forcible_rapes_1998",
    "CRM150199D": "forcible_rapes_1999",
    "CRM150200D": "forcible_rapes_2000",
    "CRM150201D": "forcible_rapes_2001",
    "CRM150202D": "forcible_rapes_2002",
    "CRM150203D": "forcible_rapes_2003",
    "CRM150204D": "forcible_rapes_2004",
    "CRM150205D": "forcible_rapes_2005",
    "CRM150206D": "forcible_rapes_2006",
    "CRM150207D": "forcible_rapes_2007",
    "CRM150208D": "forcible_rapes_2008",
    "CRM160181D": "robberies_1981",
    "CRM160182D": "robberies_1982",
    "CRM160183D": "robberies_1983",
    "CRM160184D": "robberies_1984",
    "CRM160185D": "robberies_1985",
    "CRM160186D": "robberies_1986",
    "CRM160187D": "robberies_1987",
    "CRM160188D": "robberies_1988",
    "CRM160189D": "robberies_1989",
    "CRM160190D": "robberies_1990",
    "CRM160191D": "robberies_1991",
    "CRM160192D": "robberies_1992",
    "CRM160193D": "robberies_1993",
    "CRM160194D": "robberies_1994",
    "CRM160195D": "robberies_1995",
    "CRM160196D": "robberies_1996",
    "CRM160197D": "robberies_1997",
    "CRM160198D": "robberies_1998",
    "CRM160199D": "robberies_1999",
    "CRM160200D": "robberies_2000",
    "CRM160201D": "robberies_2001",
    "CRM160202D": "robberies_2002",
    "CRM160203D": "robberies_2003",
    "CRM160204D": "robberies_2004",
    "CRM160205D": "robberies_2005",
    "CRM160206D": "robberies_2006",
    "CRM160207D": "robberies_2007",
    "CRM160208D": "robberies_2008",
    "CRM170181D": "aggravated_assaults_1981",
    "CRM170182D": "aggravated_assaults_1982",
    "CRM170183D": "aggravated_assaults_1983",
    "CRM170184D": "aggravated_assaults_1984",
    "CRM170185D": "aggravated_assaults_1985",
    "CRM170186D": "aggravated_assaults_1986",
    "CRM170187D": "aggravated_assaults_1987",
    "CRM170188D": "aggravated_assaults_1988",
    "CRM170189D": "aggravated_assaults_1989",
    "CRM170190D": "aggravated_assaults_1990",
    "CRM170191D": "aggravated_assaults_1991",
    "CRM170192D": "aggravated_assaults_1992",
    "CRM170193D": "aggravated_assaults_1993",
    "CRM170194D": "aggravated_assaults_1994",
    "CRM170195D": "aggravated_assaults_1995",
    "CRM170196D": "aggravated_assaults_1996",
    "CRM170197D": "aggravated_assaults_1997",
    "CRM170198D": "aggravated_assaults_1998",
    "CRM170199D": "aggravated_assaults_1999",
    "CRM170200D": "aggravated_assaults_2000",
    "CRM170201D": "aggravated_assaults_2001",
    "CRM170202D": "aggravated_assaults_2002",
    "CRM170203D": "aggravated_assaults_2003",
    "CRM170204D": "aggravated_assaults_2004",
    "CRM170205D": "aggravated_assaults_2005",
    "CRM170206D": "aggravated_assaults_2006",
    "CRM170207D": "aggravated_assaults_2007",
    "CRM170208D": "aggravated_assaults_2008",
    "CRM210181D": "property_crimes_1981",
    "CRM210182D": "property_crimes_1982",
    "CRM210183D": "property_crimes_1983",
    "CRM210184D": "property_crimes_1984",
    "CRM210185D": "property_crimes_1985",
    "CRM210186D": "property_crimes_1986",
    "CRM210187D": "property_crimes_1987",
    "CRM210188D": "property_crimes_1988",
    "CRM210189D": "property_crimes_1989",
    "CRM210190D": "property_crimes_1990",
    "CRM210191D": "property_crimes_1991",
    "CRM210192D": "property_crimes_1992",
    "CRM210193D": "property_crimes_1993",
    "CRM210194D": "property_crimes_1994",
    "CRM210195D": "property_crimes_1995",
    "CRM210196D": "property_crimes_1996",
    "CRM210197D": "property_crimes_1997",
    "CRM210198D": "property_crimes_1998",
    "CRM210199D": "property_crimes_1999",
    "CRM210200D": "property_crimes_2000",
    "CRM210201D": "property_crimes_2001",
    "CRM210202D": "property_crimes_2002",
    "CRM210203D": "property_crimes_2003",
    "CRM210204D": "property_crimes_2004",
    "CRM210205D": "property_crimes_2005",
    "CRM210206D": "property_crimes_2006",
    "CRM210207D": "property_crimes_2007",
    "CRM210208D": "property_crimes_2008",
    "CRM240181D": "burglaries_1981",
    "CRM240182D": "burglaries_1982",
    "CRM240183D": "burglaries_1983",
    "CRM240184D": "burglaries_1984",
    "CRM240185D": "burglaries_1985",
    "CRM240186D": "burglaries_1986",
    "CRM240187D": "burglaries_1987",
    "CRM240188D": "burglaries_1988",
    "CRM240189D": "burglaries_1989",
    "CRM240190D": "burglaries_1990",
    "CRM240191D": "burglaries_1991",
    "CRM240192D": "burglaries_1992",
    "CRM240193D": "burglaries_1993",
    "CRM240194D": "burglaries_1994",
    "CRM240195D": "burglaries_1995",
    "CRM240196D": "burglaries_1996",
    "CRM240197D": "burglaries_1997",
    "CRM240198D": "burglaries_1998",
    "CRM240199D": "burglaries_1999",
    "CRM240200D": "burglaries_2000",
    "CRM240201D": "burglaries_2001",
    "CRM240202D": "burglaries_2002",
    "CRM240203D": "burglaries_2003",
    "CRM240204D": "burglaries_2004",
    "CRM240205D": "burglaries_2005",
    "CRM240206D": "burglaries_2006",
    "CRM240207D": "burglaries_2007",
    "CRM240208D": "burglaries_2008",
    "CRM250181D": "larceny_thefts_1981",
    "CRM250182D": "larceny_thefts_1982",
    "CRM250183D": "larceny_thefts_1983",
    "CRM250184D": "larceny_thefts_1984",
    "CRM250185D": "larceny_thefts_1985",
    "CRM250186D": "larceny_thefts_1986",
    "CRM250187D": "larceny_thefts_1987",
    "CRM250188D": "larceny_thefts_1988",
    "CRM250189D": "larceny_thefts_1989",
    "CRM250190D": "larceny_thefts_1990",
    "CRM250191D": "larceny_thefts_1991",
    "CRM250192D": "larceny_thefts_1992",
    "CRM250193D": "larceny_thefts_1993",
    "CRM250194D": "larceny_thefts_1994",
    "CRM250195D": "larceny_thefts_1995",
    "CRM250196D": "larceny_thefts_1996",
    "CRM250197D": "larceny_thefts_1997",
    "CRM250198D": "larceny_thefts_1998",
    "CRM250199D": "larceny_thefts_1999",
    "CRM250200D": "larceny_thefts_2000",
    "CRM250201D": "larceny_thefts_2001",
    "CRM250202D": "larceny_thefts_2002",
    "CRM250203D": "larceny_thefts_2003",
    "CRM250204D": "larceny_thefts_2004",
    "CRM250205D": "larceny_thefts_2005",
    "CRM250206D": "larceny_thefts_2006",
    "CRM250207D": "larceny_thefts_2007",
    "CRM250208D": "larceny_thefts_2008",
    "CRM260181D": "motor_vehicle_thefts_1981",
    "CRM260182D": "motor_vehicle_thefts_1982",
    "CRM260183D": "motor_vehicle_thefts_1983",
    "CRM260184D": "motor_vehicle_thefts_1984",
    "CRM260185D": "motor_vehicle_thefts_1985",
    "CRM260186D": "motor_vehicle_thefts_1986",
    "CRM260187D": "motor_vehicle_thefts_1987",
    "CRM260188D": "motor_vehicle_thefts_1988",
    "CRM260189D": "motor_vehicle_thefts_1989",
    "CRM260190D": "motor_vehicle_thefts_1990",
    "CRM260191D": "motor_vehicle_thefts_1991",
    "CRM260192D": "motor_vehicle_thefts_1992",
    "CRM260193D": "motor_vehicle_thefts_1993",
    "CRM260194D": "motor_vehicle_thefts_1994",
    "CRM260195D": "motor_vehicle_thefts_1995",
    "CRM260196D": "motor_vehicle_thefts_1996",
    "CRM260197D": "motor_vehicle_thefts_1997",
    "CRM260198D": "motor_vehicle_thefts_1998",
    "CRM260199D": "motor_vehicle_thefts_1999",
    "CRM260200D": "motor_vehicle_thefts_2000",
    "CRM260201D": "motor_vehicle_thefts_2001",
    "CRM260202D": "motor_vehicle_thefts_2002",
    "CRM260203D": "motor_vehicle_thefts_2003",
    "CRM260204D": "motor_vehicle_thefts_2004",
    "CRM260205D": "motor_vehicle_thefts_2005",
    "CRM260206D": "motor_vehicle_thefts_2006",
    "CRM260207D": "motor_vehicle_thefts_2007",
    "CRM260208D": "motor_vehicle_thefts_2008"
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



crime_data = []
for i in range(0, sheets[0].shape[0]):
    crime_row = CrimeCounty(database_manager)
    crime_row.country_id = country_id
    for sheet in sheets:
        for input_header, output_header in header_translations.items():
            if input_header != "Areaname" and input_header != "STCOU":
                if input_header in sheet.keys():
                    setattr(crime_row, output_header, float(sheet[input_header][i]))
        if crime_row.county_code is None:
            crime_row.country_id = country_id
            city_state = sheet["Areaname"][i].split(", ")
            crime_row.county_name = city_state[0]
            crime_row.state_id = None
            crime_row.state_code = None
            if len(city_state) > 1:
                for state in us_states:
                    if state.code == city_state[1].upper():
                        crime_row.state_id = state.id
                        crime_row.state_code = state.code
                        break
            else:
                for state in us_states:
                    if state.code.upper() == sheet["Areaname"][i]:
                        crime_row.state_id = state.id
                        crime_row.county_name = None
                        break
            crime_row.county_code = int(sheet["STCOU"][i])
    crime_data.append(crime_row)
            


for crime_row in crime_data:
    crime_row.database_manager = database_manager

for crime_row in crime_data:
    database_manager.insert(crime_row)

database_manager.insert_many(crime_data)


