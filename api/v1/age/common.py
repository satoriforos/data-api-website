
def get_is_eligible(subscription_plan, header):
    pricing_eligibility = {
        "free": [
            "2009",
        ],
        "basic": [
            "2009", "totals"
        ],
        "standard":  [str(year) for year in range(1980, 2011)] + ["totals"],
        "business":  [str(year) for year in range(1980, 2011)] + ["totals"],
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
    "total_1980": False,
    "total_1990": False,
    "total_2000": False,
    "total_2001": False,
    "total_2002": False,
    "total_2003": False,
    "total_2004": False,
    "total_2005": False,
    "total_2006": False,
    "total_2007": False,
    "total_2008": False,
    "total_2009": False,
    "total_2010": False,
    "median_age_1980": False,
    "median_age_1990": False,
    "median_age_2000": False,
    "median_age_2010": False,
    "under_5_1980": False,
    "under_5_1990": False,
    "under_5_2000": False,
    "under_5_2001": False,
    "under_5_2002": False,
    "under_5_2003": False,
    "under_5_2004": False,
    "under_5_2005": False,
    "under_5_2006": False,
    "under_5_2007": False,
    "under_5_2008": False,
    "under_5_2009": False,
    "under_5_2010": False,
    "age_5_to_9_2000": False,
    "age_5_to_9_2001": False,
    "age_5_to_9_2002": False,
    "age_5_to_9_2003": False,
    "age_5_to_9_2004": False,
    "age_5_to_9_2005": False,
    "age_5_to_9_2006": False,
    "age_5_to_9_2007": False,
    "age_5_to_9_2008": False,
    "age_5_to_9_2009": False,
    "age_5_to_9_2010": False,
    "age_5_to_14_1980": False,
    "age_5_to_14_1990": False,
    "age_5_to_14_2000": False,
    "age_5_to_14_2010": False,
    "age_5_to_17_1980": False,
    "age_5_to_17_1990": False,
    "age_5_to_17_2000": False,
    "age_5_to_17_2010": False,
    "age_10_to_14_2000": False,
    "age_10_to_14_2001": False,
    "age_10_to_14_2002": False,
    "age_10_to_14_2003": False,
    "age_10_to_14_2004": False,
    "age_10_to_14_2005": False,
    "age_10_to_14_2006": False,
    "age_10_to_14_2007": False,
    "age_10_to_14_2008": False,
    "age_10_to_14_2009": False,
    "age_10_to_14_2010": False,
    "age_15_to_19_2000": False,
    "age_15_to_19_2001": False,
    "age_15_to_19_2002": False,
    "age_15_to_19_2003": False,
    "age_15_to_19_2004": False,
    "age_15_to_19_2005": False,
    "age_15_to_19_2006": False,
    "age_15_to_19_2007": False,
    "age_15_to_19_2008": False,
    "age_15_to_19_2009": False,
    "age_15_to_19_2010": False,
    "under_18_1980": False,
    "under_18_1990": False,
    "under_18_2000": False,
    "under_18_2001": False,
    "under_18_2002": False,
    "under_18_2003": False,
    "under_18_2004": False,
    "under_18_2005": False,
    "under_18_2006": False,
    "under_18_2007": False,
    "under_18_2008": False,
    "under_18_2009": False,
    "under_18_2010": False,
    "age_18_to_44_2010": False,
    "age_18_and_over_1980": False,
    "age_18_and_over_1990": False,
    "age_18_and_over_2010": False,
    "age_20_to_24_1980": False,
    "age_20_to_24_1990": False,
    "age_20_to_24_2000": False,
    "age_20_to_24_2010": False,
    "age_20_to_24_2001": False,
    "age_20_to_24_2002": False,
    "age_20_to_24_2003": False,
    "age_20_to_24_2004": False,
    "age_20_to_24_2005": False,
    "age_20_to_24_2006": False,
    "age_20_to_24_2007": False,
    "age_20_to_24_2008": False,
    "age_20_to_24_2009": False,
    "age_25_to_29_1980": False,
    "age_25_to_29_1990": False,
    "age_25_to_29_2000": False,
    "age_25_to_29_2010": False,
    "age_25_to_29_2001": False,
    "age_25_to_29_2002": False,
    "age_25_to_29_2003": False,
    "age_25_to_29_2004": False,
    "age_25_to_29_2005": False,
    "age_25_to_29_2006": False,
    "age_25_to_29_2007": False,
    "age_25_to_29_2008": False,
    "age_25_to_29_2009": False,
    "age_25_to_34_1980": False,
    "age_25_to_34_1990": False,
    "age_25_to_34_2000": False,
    "age_25_to_34_2010": False,
    "age_30_to_34_1980": False,
    "age_30_to_34_1990": False,
    "age_30_to_34_2000": False,
    "age_30_to_34_2010": False,
    "age_30_to_34_2001": False,
    "age_30_to_34_2002": False,
    "age_30_to_34_2003": False,
    "age_30_to_34_2004": False,
    "age_30_to_34_2005": False,
    "age_30_to_34_2006": False,
    "age_30_to_34_2007": False,
    "age_30_to_34_2008": False,
    "age_30_to_34_2009": False,
    "age_35_to_39_1990": False,
    "age_35_to_39_2000": False,
    "age_35_to_39_2010": False,
    "age_35_to_39_2001": False,
    "age_35_to_39_2002": False,
    "age_35_to_39_2003": False,
    "age_35_to_39_2004": False,
    "age_35_to_39_2005": False,
    "age_35_to_39_2006": False,
    "age_35_to_39_2007": False,
    "age_35_to_39_2008": False,
    "age_35_to_39_2009": False,
    "age_35_to_44_1980": False,
    "age_35_to_44_1990": False,
    "age_35_to_44_2000": False,
    "age_35_to_44_2010": False,
    "age_40_to_44_1990": False,
    "age_40_to_44_2000": False,
    "age_40_to_44_2010": False,
    "age_40_to_44_2001": False,
    "age_40_to_44_2002": False,
    "age_40_to_44_2003": False,
    "age_40_to_44_2004": False,
    "age_40_to_44_2005": False,
    "age_40_to_44_2006": False,
    "age_40_to_44_2007": False,
    "age_40_to_44_2008": False,
    "age_40_to_44_2009": False,
    "age_45_to_49_1990": False,
    "age_45_to_49_2000": False,
    "age_45_to_49_2010": False,
    "age_45_to_49_2001": False,
    "age_45_to_49_2002": False,
    "age_45_to_49_2003": False,
    "age_45_to_49_2004": False,
    "age_45_to_49_2005": False,
    "age_45_to_49_2006": False,
    "age_45_to_49_2007": False,
    "age_45_to_49_2008": False,
    "age_45_to_49_2009": False,
    "age_45_to_54_1980": False,
    "age_45_to_54_1990": False,
    "age_45_to_54_2000": False,
    "age_45_to_54_2010": False,
    "age_45_to_64_2010": False,
    "age_50_to_54_1990": False,
    "age_50_to_54_2000": False,
    "age_50_to_54_2010": False,
    "age_50_to_54_2001": False,
    "age_50_to_54_2002": False,
    "age_50_to_54_2003": False,
    "age_50_to_54_2004": False,
    "age_50_to_54_2005": False,
    "age_50_to_54_2006": False,
    "age_50_to_54_2007": False,
    "age_50_to_54_2008": False,
    "age_50_to_54_2009": False,
    "age_55_to_59_1980": False,
    "age_55_to_59_1990": False,
    "age_55_to_59_2000": False,
    "age_55_to_59_2010": False,
    "age_55_to_59_2001": False,
    "age_55_to_59_2002": False,
    "age_55_to_59_2003": False,
    "age_55_to_59_2004": False,
    "age_55_to_59_2005": False,
    "age_55_to_59_2006": False,
    "age_55_to_59_2007": False,
    "age_55_to_59_2008": False,
    "age_55_to_59_2009": False,
    "age_60_to_64_1980": False,
    "age_60_to_64_1990": False,
    "age_60_to_64_2000": False,
    "age_60_to_64_2010": False,
    "age_60_to_64_2001": False,
    "age_60_to_64_2002": False,
    "age_60_to_64_2003": False,
    "age_60_to_64_2004": False,
    "age_60_to_64_2005": False,
    "age_60_to_64_2006": False,
    "age_60_to_64_2007": False,
    "age_60_to_64_2008": False,
    "age_60_to_64_2009": False,
    "age_65_to_69_1990": False,
    "age_65_to_69_2000": False,
    "age_65_to_69_2010": False,
    "age_65_to_69_2001": False,
    "age_65_to_69_2002": False,
    "age_65_to_69_2003": False,
    "age_65_to_69_2004": False,
    "age_65_to_69_2005": False,
    "age_65_to_69_2006": False,
    "age_65_to_69_2007": False,
    "age_65_to_69_2008": False,
    "age_65_to_69_2009": False,
    "age_65_to_74_1990": False,
    "age_65_to_74_2000": False,
    "age_65_to_74_2010": False,
    "age_65_and_over_1980": False,
    "age_65_and_over_1990": False,
    "age_65_and_over_2000": False,
    "age_65_and_over_2001": False,
    "age_65_and_over_2002": False,
    "age_65_and_over_2003": False,
    "age_65_and_over_2004": False,
    "age_65_and_over_2005": False,
    "age_65_and_over_2006": False,
    "age_65_and_over_2007": False,
    "age_65_and_over_2008": False,
    "age_65_and_over_2009": False,
    "age_65_and_over_2010": False,
    "age_70_to_74_1990": False,
    "age_70_to_74_2000": False,
    "age_70_to_74_2010": False,
    "age_70_to_74_2001": False,
    "age_70_to_74_2002": False,
    "age_70_to_74_2003": False,
    "age_70_to_74_2004": False,
    "age_70_to_74_2005": False,
    "age_70_to_74_2006": False,
    "age_70_to_74_2007": False,
    "age_70_to_74_2008": False,
    "age_70_to_74_2009": False,
    "age_75_to_79_1990": False,
    "age_75_to_79_2000": False,
    "age_75_to_79_2010": False,
    "age_75_to_79_2001": False,
    "age_75_to_79_2002": False,
    "age_75_to_79_2003": False,
    "age_75_to_79_2004": False,
    "age_75_to_79_2005": False,
    "age_75_to_79_2006": False,
    "age_75_to_79_2007": False,
    "age_75_to_79_2008": False,
    "age_75_to_79_2009": False,
    "age_75_to_84_1990": False,
    "age_75_to_84_2000": False,
    "age_75_to_84_2010": False,
    "age_80_to_84_1990": False,
    "age_80_to_84_2000": False,
    "age_80_to_84_2010": False,
    "age_80_to_84_2001": False,
    "age_80_to_84_2002": False,
    "age_80_to_84_2003": False,
    "age_80_to_84_2004": False,
    "age_80_to_84_2005": False,
    "age_80_to_84_2006": False,
    "age_80_to_84_2007": False,
    "age_80_to_84_2008": False,
    "age_80_to_84_2009": False,
    "age_75_and_over_2010": False,
    "age_85_and_over_1990": False,
    "age_85_and_over_2000": False,
    "age_85_and_over_2001": False,
    "age_85_and_over_2002": False,
    "age_85_and_over_2003": False,
    "age_85_and_over_2004": False,
    "age_85_and_over_2005": False,
    "age_85_and_over_2006": False,
    "age_85_and_over_2007": False,
    "age_85_and_over_2008": False,
    "age_85_and_over_2009": False,
    "age_85_and_over_2010": False,
}