
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2010",
        ],
        "basic": [
            "2010", "totals"
        ],
        "standard":  [str(year) for year in range(2000, 2010)] + ["totals"],
        "business":  [str(year) for year in range(2000, 2010)] + ["totals"],
    }
    is_eligible = False
    if subscription_plan is not None:
        if subscription_plan.name in pricing_eligibility:
            year = header[-4:]
            if year in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
            if header in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
    return is_eligible


eligible_headers = {
    "males_2000": False,
    "males_2001": False,
    "males_2002": False,
    "males_2003": False,
    "males_2004": False,
    "males_2005": False,
    "males_2006": False,
    "males_2007": False,
    "males_2008": False,
    "males_2009": False,
    "females_2000": False,
    "females_2001": False,
    "females_2002": False,
    "females_2003": False,
    "females_2004": False,
    "females_2005": False,
    "females_2006": False,
    "females_2007": False,
    "females_2008": False,
    "females_2009": False,
}



