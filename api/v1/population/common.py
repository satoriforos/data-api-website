
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2009",
        ],
        "basic": [
            "2009",
        ],
        "standard":  [str(year) for year in range(1930, 2011)],
        "business":  [str(year) for year in range(1930, 2011)],
    }
    exclusions = [
        "total_2000",
        "total_1990",
        "total_1980"
    ]
    is_eligible = False
    if subscription_plan is not None:
        if subscription_plan.name in pricing_eligibility:
            year = header[-4:]
            if year in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
            if header in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
    if header in exclusions:
        is_eligible = False
    return is_eligible


eligible_headers = {
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