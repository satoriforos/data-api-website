
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2009",
        ],
        "basic": [
            "2009", "totals"
        ],
        "standard":  ["1980", "1990", "2000", "2009", "totals"],
        "business":  ["1980", "1990", "2000", "2009", "totals"],
    }
    is_eligible = False
    if subscription_plan is not None:
        if subscription_plan.name in pricing_eligibility:
            year = header[-4:]
            #if year in pricing_eligibility[subscription_plan.name]:
            #    if "totals" in header:
            #        #if "totals" in pricing_eligibility[subscription_plan.name]:
            #        is_eligible = False
            #    else:
            #        is_eligible = True
            if year in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
            if header in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
    return is_eligible


eligible_headers = {
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