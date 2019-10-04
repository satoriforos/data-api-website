
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2007",
        ],
        "basic": [
            "2007", "total"
        ],
        "standard":  [str(year) for year in range(2005, 2008)] + ["totals"],
        "business":  [str(year) for year in range(2005, 2008)] + ["totals"],
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