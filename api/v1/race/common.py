import re


def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2010",
        ],
        "basic": [
            "2010", "totals"
        ],
        "standard":  [str(year) for year in range(2000, 2011)] + ["totals"],
        "business":  [str(year) for year in range(2000, 2011)] + ["totals"],
    }
    is_eligible = False
    if subscription_plan is not None:
        if subscription_plan.name in pricing_eligibility:
            year = header[-4:]
            if year in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
            if header in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
            matches = re.findall(r'white_[\d]{4}', header)
            if len(matches) > 0:
                is_eligible = False
    return is_eligible


eligible_headers = {
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
    "hawaiian_pacific_islander_2000": False,
    "hawaiian_pacific_islander_2001": False,
    "hawaiian_pacific_islander_2002": False,
    "hawaiian_pacific_islander_2003": False,
    "hawaiian_pacific_islander_2004": False,
    "hawaiian_pacific_islander_2005": False,
    "hawaiian_pacific_islander_2006": False,
    "hawaiian_pacific_islander_2007": False,
    "hawaiian_pacific_islander_2008": False,
    "hawaiian_pacific_islander_2009": False,
    "hawaiian_pacific_islander_2010": False,
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