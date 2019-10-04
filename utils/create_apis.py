#!/usr/bin/env python3
from pathlib import Path
import json

master_template = 'ancestry'

endpoints = [
    #'age',
    #'ancestry',
    #'crime',
    'education',
    'elections',
    'health',
    'income',
    'population',
    'race'
]

templates = [
    'city',
    'country',
    'state',
    'zip'
]


header_translations = {}
header_translations["crime"] = {
    "violent_crimes_1981": False,
    "violent_crimes_1982": False,
    "violent_crimes_1983": False,
    "violent_crimes_1984": False,
    "violent_crimes_1985": False,
    "violent_crimes_1986": False,
    "violent_crimes_1987": False,
    "violent_crimes_1988": False,
    "violent_crimes_1989": False,
    "violent_crimes_1990": False,
    "violent_crimes_1991": False,
    "violent_crimes_1992": False,
    "violent_crimes_1993": False,
    "violent_crimes_1994": False,
    "violent_crimes_1995": False,
    "violent_crimes_1996": False,
    "violent_crimes_1997": False,
    "violent_crimes_1998": False,
    "violent_crimes_1999": False,
    "violent_crimes_2000": False,
    "violent_crimes_2001": False,
    "violent_crimes_2002": False,
    "violent_crimes_2003": False,
    "violent_crimes_2004": False,
    "violent_crimes_2005": False,
    "violent_crimes_2006": False,
    "violent_crimes_2007": False,
    "violent_crimes_2008": False,
    "murders_1990": False,
    "murders_1991": False,
    "murders_1992": False,
    "murders_1993": False,
    "murders_1994": False,
    "murders_1995": False,
    "murders_1996": False,
    "murders_1997": False,
    "murders_1998": False,
    "murders_1999": False,
    "murders_2000": False,
    "murders_2001": False,
    "murders_2002": False,
    "murders_2003": False,
    "murders_2004": False,
    "murders_2005": False,
    "murders_2006": False,
    "murders_2007": False,
    "murders_2008": False,
    "forcible_rapes_1990": False,
    "forcible_rapes_1991": False,
    "forcible_rapes_1992": False,
    "forcible_rapes_1993": False,
    "forcible_rapes_1994": False,
    "forcible_rapes_1995": False,
    "forcible_rapes_1996": False,
    "forcible_rapes_1997": False,
    "forcible_rapes_1998": False,
    "forcible_rapes_1999": False,
    "forcible_rapes_2000": False,
    "forcible_rapes_2001": False,
    "forcible_rapes_2002": False,
    "forcible_rapes_2003": False,
    "forcible_rapes_2004": False,
    "forcible_rapes_2005": False,
    "forcible_rapes_2006": False,
    "forcible_rapes_2007": False,
    "forcible_rapes_2008": False,
    "robberies_1981": False,
    "robberies_1982": False,
    "robberies_1983": False,
    "robberies_1984": False,
    "robberies_1985": False,
    "robberies_1986": False,
    "robberies_1987": False,
    "robberies_1988": False,
    "robberies_1989": False,
    "robberies_1990": False,
    "robberies_1991": False,
    "robberies_1992": False,
    "robberies_1993": False,
    "robberies_1994": False,
    "robberies_1995": False,
    "robberies_1996": False,
    "robberies_1997": False,
    "robberies_1998": False,
    "robberies_1999": False,
    "robberies_2000": False,
    "robberies_2001": False,
    "robberies_2002": False,
    "robberies_2003": False,
    "robberies_2004": False,
    "robberies_2005": False,
    "robberies_2006": False,
    "robberies_2007": False,
    "robberies_2008": False,
    "aggravated_assaults_1981": False,
    "aggravated_assaults_1982": False,
    "aggravated_assaults_1983": False,
    "aggravated_assaults_1984": False,
    "aggravated_assaults_1985": False,
    "aggravated_assaults_1986": False,
    "aggravated_assaults_1987": False,
    "aggravated_assaults_1988": False,
    "aggravated_assaults_1989": False,
    "aggravated_assaults_1990": False,
    "aggravated_assaults_1991": False,
    "aggravated_assaults_1992": False,
    "aggravated_assaults_1993": False,
    "aggravated_assaults_1994": False,
    "aggravated_assaults_1995": False,
    "aggravated_assaults_1996": False,
    "aggravated_assaults_1997": False,
    "aggravated_assaults_1998": False,
    "aggravated_assaults_1999": False,
    "aggravated_assaults_2000": False,
    "aggravated_assaults_2001": False,
    "aggravated_assaults_2002": False,
    "aggravated_assaults_2003": False,
    "aggravated_assaults_2004": False,
    "aggravated_assaults_2005": False,
    "aggravated_assaults_2006": False,
    "aggravated_assaults_2007": False,
    "aggravated_assaults_2008": False,
    "property_crimes_1981": False,
    "property_crimes_1982": False,
    "property_crimes_1983": False,
    "property_crimes_1984": False,
    "property_crimes_1985": False,
    "property_crimes_1986": False,
    "property_crimes_1987": False,
    "property_crimes_1988": False,
    "property_crimes_1989": False,
    "property_crimes_1990": False,
    "property_crimes_1991": False,
    "property_crimes_1992": False,
    "property_crimes_1993": False,
    "property_crimes_1994": False,
    "property_crimes_1995": False,
    "property_crimes_1996": False,
    "property_crimes_1997": False,
    "property_crimes_1998": False,
    "property_crimes_1999": False,
    "property_crimes_2000": False,
    "property_crimes_2001": False,
    "property_crimes_2002": False,
    "property_crimes_2003": False,
    "property_crimes_2004": False,
    "property_crimes_2005": False,
    "property_crimes_2006": False,
    "property_crimes_2007": False,
    "property_crimes_2008": False,
    "burglaries_1981": False,
    "burglaries_1982": False,
    "burglaries_1983": False,
    "burglaries_1984": False,
    "burglaries_1985": False,
    "burglaries_1986": False,
    "burglaries_1987": False,
    "burglaries_1988": False,
    "burglaries_1989": False,
    "burglaries_1990": False,
    "burglaries_1991": False,
    "burglaries_1992": False,
    "burglaries_1993": False,
    "burglaries_1994": False,
    "burglaries_1995": False,
    "burglaries_1996": False,
    "burglaries_1997": False,
    "burglaries_1998": False,
    "burglaries_1999": False,
    "burglaries_2000": False,
    "burglaries_2001": False,
    "burglaries_2002": False,
    "burglaries_2003": False,
    "burglaries_2004": False,
    "burglaries_2005": False,
    "burglaries_2006": False,
    "burglaries_2007": False,
    "burglaries_2008": False,
    "larceny_thefts_1981": False,
    "larceny_thefts_1982": False,
    "larceny_thefts_1983": False,
    "larceny_thefts_1984": False,
    "larceny_thefts_1985": False,
    "larceny_thefts_1986": False,
    "larceny_thefts_1987": False,
    "larceny_thefts_1988": False,
    "larceny_thefts_1989": False,
    "larceny_thefts_1990": False,
    "larceny_thefts_1991": False,
    "larceny_thefts_1992": False,
    "larceny_thefts_1993": False,
    "larceny_thefts_1994": False,
    "larceny_thefts_1995": False,
    "larceny_thefts_1996": False,
    "larceny_thefts_1997": False,
    "larceny_thefts_1998": False,
    "larceny_thefts_1999": False,
    "larceny_thefts_2000": False,
    "larceny_thefts_2001": False,
    "larceny_thefts_2002": False,
    "larceny_thefts_2003": False,
    "larceny_thefts_2004": False,
    "larceny_thefts_2005": False,
    "larceny_thefts_2006": False,
    "larceny_thefts_2007": False,
    "larceny_thefts_2008": False,
    "motor_vehicle_thefts_1981": False,
    "motor_vehicle_thefts_1982": False,
    "motor_vehicle_thefts_1983": False,
    "motor_vehicle_thefts_1984": False,
    "motor_vehicle_thefts_1985": False,
    "motor_vehicle_thefts_1986": False,
    "motor_vehicle_thefts_1987": False,
    "motor_vehicle_thefts_1988": False,
    "motor_vehicle_thefts_1989": False,
    "motor_vehicle_thefts_1990": False,
    "motor_vehicle_thefts_1991": False,
    "motor_vehicle_thefts_1992": False,
    "motor_vehicle_thefts_1993": False,
    "motor_vehicle_thefts_1994": False,
    "motor_vehicle_thefts_1995": False,
    "motor_vehicle_thefts_1996": False,
    "motor_vehicle_thefts_1997": False,
    "motor_vehicle_thefts_1998": False,
    "motor_vehicle_thefts_1999": False,
    "motor_vehicle_thefts_2000": False,
    "motor_vehicle_thefts_2001": False,
    "motor_vehicle_thefts_2002": False,
    "motor_vehicle_thefts_2003": False,
    "motor_vehicle_thefts_2004": False,
    "motor_vehicle_thefts_2005": False,
    "motor_vehicle_thefts_2006": False,
    "motor_vehicle_thefts_2007": False,
    "motor_vehicle_thefts_2008": False
}

header_translations["education"] = {
    "num_adults_1980": False,
    "num_adults_1990": False,
    "num_adults_2000": False,
    "num_adults_2005_2009": False,
    "less_than_grade_9_1990": False,
    "less_than_grade_9_2000": False,
    "less_than_grade_9_2005_2009": False,
    "grade_9_to_12_no_diploma_1990": False,
    "grade_9_to_12_no_diploma_2000": False,
    "grade_9_to_12_no_diploma_2005_2009": False,
    "high_school_graduate_1990": False,
    "high_school_graduate_2000": False,
    "high_school_graduate_2005_2009": False,
    "some_college_or_associate_degree_1990": False,
    "some_college_or_associate_degree_2000": False,
    "incomplete_college_2000": False,
    "incomplete_college_2005_2009": False,
    "associate_degree_2000": False,
    "associate_degree_2005_2009": False,
    "any_college_degree_1990": False,
    "any_college_degree_2000": False,
    "bachelors_degree_2000": False,
    "bachelors_degree_2005_2009": False,
    "graduate_degree_2000": False,
    "graduate_degree_2005_2009": False
}

header_translations["elections"] = {
    "total_1980": False,
    "total_1984": False,
    "total_1988": False,
    "total_1992": False,
    "total_1996": False,
    "total_2000": False,
    "total_2004": False,
    "total_2008": False,
    "democrat_1980": False,
    "democrat_1984": False,
    "democrat_1988": False,
    "democrat_1992": False,
    "democrat_1996": False,
    "democrat_2000": False,
    "democrat_2004": False,
    "democrat_2008": False,
    "republican_1980": False,
    "republican_1984": False,
    "republican_1988": False,
    "republican_1992": False,
    "republican_1996": False,
    "republican_2000": False,
    "republican_2004": False,
    "republican_2008": False,
    "other_1980": False,
    "other_1984": False,
    "other_1988": False,
    "other_1992": False,
    "other_1996": False,
    "other_2000": False,
    "other_2004": False,
    "other_2008": False
}

header_translations["health"] = {
    "no_insurance_under_18_2005": False,
    "no_insurance_under_18_2006": False,
    "no_insurance_under_18_2007": False,
    "no_insurance_under_18_to_16_2005": False,
    "no_insurance_under_18_to_16_2006": False,
    "no_insurance_under_18_to_16_2007": False,
    "no_insurance_under_40_to_64_2005": False,
    "no_insurance_under_40_to_64_2006": False,
    "no_insurance_under_40_to_64_2007": False,
    "no_insurance_under_65_2005": False,
    "no_insurance_under_65_2006": False,
    "no_insurance_under_65_2007": False
}


header_translations["income"] = {
    "median_1979": False,
    "median_1989": False,
    "median_1999": False,
    "less_than_10000_1979": False,
    "less_than_10000_1989": False,
    "less_than_10000_1999": False,
    "between_10000_and_14999_1979": False,
    "between_10000_and_14999_1989": False,
    "between_10000_and_14999_1999": False,
    "between_15000_and_19999_1979": False,
    "between_15000_and_19999_1989": False,
    "between_15000_and_19999_1999": False,
    "between_20000_and_24999_1979": False,
    "between_20000_and_24999_1989": False,
    "between_20000_and_24999_1999": False,
    "between_25000_and_29999_1979": False,
    "between_25000_and_29999_1989": False,
    "between_25000_and_29999_1999": False,
    "between_30000_and_34999_1979": False,
    "between_30000_and_34999_1989": False,
    "between_30000_and_34999_1999": False,
    "between_35000_and_39999_1979": False,
    "between_35000_and_39999_1989": False,
    "between_35000_and_39999_1999": False,
    "between_40000_and_49999_1979": False,
    "between_40000_and_49999_1989": False,
    "between_40000_and_49999_1999": False,
    "between_40000_and_44999_1989": False,
    "between_40000_and_44999_1999": False,
    "between_45000_and_49999_1989": False,
    "between_45000_and_49999_1999": False,
    "between_50000_and_74999_1979": False,
    "between_50000_and_74999_1989": False,
    "between_50000_and_74999_1999": False,
    "between_50000_and_59999_1989": False,
    "between_50000_and_59999_1999": False,
    "between_60000_and_74999_1989": False,
    "between_60000_and_74999_1999": False,
    "over_75000_1979": False,
    "over_75000_1989": False,
    "over_75000_1999": False,
    "between_75000_and_99999_1989": False,
    "between_75000_and_99999_1999": False,
    "between_100000_and_124999_1989": False,
    "between_100000_and_124999_1999": False,
    "between_125000_and_149999_1989": False,
    "between_125000_and_149999_1999": False,
    "over_150000_1989": False,
    "over_150000_1999": False,
    "between_150000_and_199999_1999": False,
    "over_200000_1999": False
}

header_translations["population"] = {
    "total_1930": False,
    "total_1940": False,
    "total_1950": False,
    "total_1960": False,
    "total_1970": False,
    "total_1980": False,
    "total_1990": False,
    "total_2000": False,
    "total_2010": False,
    "estimate_1971": False,
    "estimate_1972": False,
    "estimate_1973": False,
    "estimate_1974": False,
    "estimate_1975": False,
    "estimate_1976": False,
    "estimate_1977": False,
    "estimate_1978": False,
    "estimate_1979": False,
    "estimate_1981": False,
    "estimate_1982": False,
    "estimate_1983": False,
    "estimate_1984": False,
    "estimate_1985": False,
    "estimate_1986": False,
    "estimate_1987": False,
    "estimate_1988": False,
    "estimate_1989": False,
    "estimate_1990": False,
    "estimate_1991": False,
    "estimate_1992": False,
    "estimate_1993": False,
    "estimate_1994": False,
    "estimate_1995": False,
    "estimate_1996": False,
    "estimate_1997": False,
    "estimate_1998": False,
    "estimate_1999": False,
    "estimate_2000": False,
    "estimate_2001": False,
    "estimate_2002": False,
    "estimate_2003": False,
    "estimate_2004": False,
    "estimate_2005": False,
    "estimate_2006": False,
    "estimate_2007": False,
    "estimate_2008": False,
    "estimate_2009": False
}


header_translations["race"] = {
    "white_2000": False,
    "white_2001": False,
    "white_2002": False,
    "white_2003": False,
    "white_2004": False,
    "white_2005": False,
    "white_2006": False,
    "white_2007": False,
    "white_2008": False,
    "white_2009": False,
    "white_2010": False,
    "black_2000": False,
    "black_2001": False,
    "black_2002": False,
    "black_2003": False,
    "black_2004": False,
    "black_2005": False,
    "black_2006": False,
    "black_2007": False,
    "black_2008": False,
    "black_2009": False,
    "black_2010": False,
    "aboriginal_alaskan_2000": False,
    "aboriginal_alaskan_2001": False,
    "aboriginal_alaskan_2002": False,
    "aboriginal_alaskan_2003": False,
    "aboriginal_alaskan_2004": False,
    "aboriginal_alaskan_2005": False,
    "aboriginal_alaskan_2006": False,
    "aboriginal_alaskan_2007": False,
    "aboriginal_alaskan_2008": False,
    "aboriginal_alaskan_2009": False,
    "aboriginal_alaskan_2010": False,
    "asian_2000": False,
    "asian_2001": False,
    "asian_2002": False,
    "asian_2003": False,
    "asian_2004": False,
    "asian_2005": False,
    "asian_2006": False,
    "asian_2007": False,
    "asian_2008": False,
    "asian_2009": False,
    "asian_2010": False,
    "hawaiian_pacific_islander2000": False,
    "hawaiian_pacific_islander2001": False,
    "hawaiian_pacific_islander2002": False,
    "hawaiian_pacific_islander2003": False,
    "hawaiian_pacific_islander2004": False,
    "hawaiian_pacific_islander2005": False,
    "hawaiian_pacific_islander2006": False,
    "hawaiian_pacific_islander2007": False,
    "hawaiian_pacific_islander2008": False,
    "hawaiian_pacific_islander2009": False,
    "hawaiian_pacific_islander2010": False,
    "mixed_2000": False,
    "mixed_2001": False,
    "mixed_2002": False,
    "mixed_2003": False,
    "mixed_2004": False,
    "mixed_2005": False,
    "mixed_2006": False,
    "mixed_2007": False,
    "mixed_2008": False,
    "mixed_2009": False,
    "mixed_2010": False,
    "hispanic_latino_2000": False,
    "hispanic_latino_2001": False,
    "hispanic_latino_2002": False,
    "hispanic_latino_2003": False,
    "hispanic_latino_2004": False,
    "hispanic_latino_2005": False,
    "hispanic_latino_2006": False,
    "hispanic_latino_2007": False,
    "hispanic_latino_2008": False,
    "hispanic_latino_2009": False,
    "hispanic_latino_2010": False,
    "white_non_hispanic_2000": False,
    "white_non_hispanic_2001": False,
    "white_non_hispanic_2002": False,
    "white_non_hispanic_2003": False,
    "white_non_hispanic_2004": False,
    "white_non_hispanic_2005": False,
    "white_non_hispanic_2006": False,
    "white_non_hispanic_2007": False,
    "white_non_hispanic_2008": False,
    "white_non_hispanic_2009": False,
    "white_non_hispanic_2010": False
}


eligibility_function = """
def get_is_eligible(subscription_plan, account, header):
    pricing_eligibility = {
        "free": [
            "2009",
        ],
        "basic": [
            "2009",
        ],
        "standard":  [str(year) for year in range(1980, 2010)],
        "business":  [str(year) for year in range(1980, 2010)],
    }
    is_eligible = False
    if subscription_plan is not None:
        if subscription_plan.name in pricing_eligibility:
            year = header[-4:]
            if year in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
    return is_eligible
"""

print("READING ")
print("========")
# import templates
file_contents = {}
file_mode = None
p = Path('api/v1/{}'.format(master_template))
for template in templates:
    file_path = p / Path("{}.py".format(template))
    print("reading {}".format(file_path.as_posix()))
    text = file_path.read_text()
    file_contents[template] = text
    if file_mode is None:
        file_mode = file_path.stat().st_mode

print("WRITING")
print("========")
for endpoint in endpoints:
    endpoint_path = Path("api/v1/{}".format(endpoint))
    print("creating {}".format(endpoint_path.as_posix()))
    if endpoint_path.exists() is False:
        endpoint_path.mkdir()
    for template in templates:
        file_path = endpoint_path / Path("{}.py".format(template))
        print("    {}".format(file_path.as_posix()))
        text = file_contents[template]
        text = text.replace('ancestry', endpoint.lower())
        text = text.replace('Ancestry', endpoint.capitalize())
        file_path.write_text(text)
        file_path.chmod(file_mode)
    file_path = endpoint_path / Path("common.py")
    print("    {}".format(file_path.as_posix()))
    headers = json.dumps(header_translations[endpoint], indent=4)
    headers = headers.replace("false", "False")
    headers = "eligible_headers = {}".format(headers)
    common_text = "{}\n\n{}".format(eligibility_function, headers)
    file_path.write_text(common_text)
    print("--------------------------------------------")

