
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2009",
        ],
        "basic": [
            "2009", "totals"
        ],
        "standard":  ["1990", "2000", "2009"] + ["totals"],
        "business":  ["1990", "2000", "2009"] + ["totals"],
    }
    is_eligible = False
    if subscription_plan is not None:
        if subscription_plan.name in pricing_eligibility:
            year = header[-4:]
            if year in pricing_eligibility[subscription_plan.name]:
                if "total_" in header:
                    #if "totals" in pricing_eligibility[subscription_plan.name]:
                    is_eligible = False
                else:
                    is_eligible = True
            if header in pricing_eligibility[subscription_plan.name]:
                is_eligible = True
    return is_eligible


eligible_headers = {
    "total_1990": False,
    "total_2000": False,
    "total_2009": False,
    "american_1990": False,
    "american_2000": False,
    "american_2009": False,
    "arab_1990": False,
    "arab_2000": False,
    "arab_2009": False,
    "british_2009": False,
    "czech_1990": False,
    "czech_2000": False,
    "czech_2009": False,
    "danish_1990": False,
    "danish_2000": False,
    "danish_2009": False,
    "dutch_1990": False,
    "dutch_2000": False,
    "dutch_2009": False,
    "english_1990": False,
    "english_2000": False,
    "english_2009": False,
    "european_2009": False,
    "french_1990": False,
    "french_2000": False,
    "french_2009": False,
    "french_canadian_1990": False,
    "french_canadian_2000": False,
    "french_canadian_2009": False,
    "german_1990": False,
    "german_2000": False,
    "german_2009": False,
    "greek_1990": False,
    "greek_2000": False,
    "greek_2009": False,
    "hungarian_1990": False,
    "hungarian_2000": False,
    "hungarian_2009": False,
    "irish_1990": False,
    "irish_2000": False,
    "irish_2009": False,
    "italian_1990": False,
    "italian_2000": False,
    "italian_2009": False,
    "lithuanian_1990": False,
    "lithuanian_2000": False,
    "lithuanian_2009": False,
    "norwegian_1990": False,
    "norwegian_2000": False,
    "norwegian_2009": False,
    "polish_1990": False,
    "polish_2000": False,
    "polish_2009": False,
    "portuguese_1990": False,
    "portuguese_2000": False,
    "portuguese_2009": False,
    "russian_1990": False,
    "russian_2000": False,
    "russian_2009": False,
    "scotch_irish_1990": False,
    "scotch_irish_2000": False,
    "scotch_irish_2009": False,
    "scottish_1990": False,
    "scottish_2000": False,
    "scottish_2009": False,
    "slovak_1990": False,
    "slovak_2000": False,
    "slovak_2009": False,
    "subsaharan_african_1990": False,
    "subsaharan_african_2000": False,
    "subsaharan_african_2009": False,
    "swedish_1990": False,
    "swedish_2000": False,
    "swedish_2009": False,
    "swiss_1990": False,
    "swiss_2000": False,
    "swiss_2009": False,
    "ukrainian_1990": False,
    "ukrainian_2000": False,
    "ukrainian_2009": False,
    "welsh_1990": False,
    "welsh_2000": False,
    "welsh_2009": False,
    "west_indian_1990": False,
    "west_indian_2000": False,
    "west_indian_2009": False,
    "other_1990": False,
    "other_2000": False,
    "other_groups_2009": False
}