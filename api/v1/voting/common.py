
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2008",
        ],
        "basic": [
            "2009", "totals",
        ],
        "standard":  [str(year) for year in range(1980, 2009, 4)] + ["totals"],
        "business":  [str(year) for year in range(1980, 2009, 4)] + ["totals"],
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