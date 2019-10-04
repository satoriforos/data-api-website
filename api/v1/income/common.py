
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "1999",
        ],
        "basic": [
            "1999", "totals",
        ],
        "standard":  [str(year) for year in range(1979, 2000, 10)] + ["totals"],
        "business":  [str(year) for year in range(1979, 2000, 10)] + ["totals"],
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