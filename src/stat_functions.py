import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from statsmodels.stats.multitest import multipletests

from initial_data_clean import us_county_df, us_county_agg_df
from grouping_functions import GroupBy

def get_norm_coef(df):
    # This Returns the coef. of Normal dist
    # passing in data frame
    df = df.copy()
    mean_df = df['age_adjusted_rate'].mean()
    sqrt_df = np.sqrt(len(df['age_adjusted_rate']))
    std = (df['age_adjusted_rate'].std())/sqrt_df
    return mean_df, std

def normal_dist(mean, std):
    # This returns Normal dist with desired coefs
    return stats.norm(loc=mean, scale=std)

def metro_non_metro_box_plot_df(df):
    # Creates a list of the age_ajusted rates for 
    # Metropolitan areas (1-4)
    # Non-Metropolitan areas (5 & 6)
    metro = df[df['urbanization_code'] < 5]['age_adjusted_rate'].tolist()
    non_metro = df[df['urbanization_code'] >= 5]['age_adjusted_rate'].tolist()
    data = [metro, non_metro]
    return data

def urbanization_areas_box_plot_df(df):
    # Creates a list of the age_ajusted rates for each of the urbanization codes
    l1 = df[df['urbanization_code'] == 1]['age_adjusted_rate'].tolist()
    l2 = df[df['urbanization_code'] == 2]['age_adjusted_rate'].tolist()
    l3 = df[df['urbanization_code'] == 3]['age_adjusted_rate'].tolist()
    l4 = df[df['urbanization_code'] == 4]['age_adjusted_rate'].tolist()
    l5 = df[df['urbanization_code'] == 5]['age_adjusted_rate'].tolist()
    l6 = df[df['urbanization_code'] == 6]['age_adjusted_rate'].tolist()
    data = [l1, l2, l3, l4, l5, l6]
    return data

def male_female_box_plot_df(df1, df2):
    male = df1['age_specific_rate'].tolist()
    female = df2['age_specific_rate'].tolist()
    data = [male, female]
    return data
    
bonf_correction = multipletests([7.159569963932792e-43, 1.3309587747817716e-42, 4.056464310171394e-22],
                    alpha=0.05, method='bonferroni')

if __name__ == "__main__":
    # gb = GroupBy(us_county_agg_df)
    # gb.county_urbanization_age_rate()
    # agg_county_metro, agg_county_non_metro = gb.metro_non_metro()
    # metro_mean, metro_std = get_norm_coef(agg_county_metro)
    # non_metro_mean, non_metro_std = get_norm_coef(agg_county_non_metro)
    # metro_norm = normal_dist(metro_mean, metro_std)
    # non_metro_norm = normal_dist(non_metro_mean, non_metro_std)
    # t_test = stats.ttest_ind(agg_county_metro['age_adjusted_rate'], agg_county_non_metro['age_adjusted_rate'], equal_var=False)
    # test = metro_non_metro_box_plot_df(us_county_agg_df)
    # print(t_test)
    print(bonf_correction)