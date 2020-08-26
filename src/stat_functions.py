import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

from initial_data_clean import us_county_df
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

def metro_box_plot_df(df):
    metro = df[df['urbanization_code'] < 5]['age_adjusted_rate'].tolist()
    non_metro = df[df['urbanization_code'] >= 5]['age_adjusted_rate'].tolist()
    data = [metro, non_metro]
    return data
    

if __name__ == "__main__":
    metro, non_metro = GroupBy(us_county_df).metro_non_metro()
    metro_mean, metro_std = get_norm_coef(metro)
    non_metro_mean, non_metro_std = get_norm_coef(non_metro)
    metro_norm = normal_dist(metro_mean, metro_std)
    non_metro_norm = normal_dist(non_metro_mean, non_metro_std)
    t_test = stats.ttest_ind(metro['age_adjusted_rate'], non_metro['age_adjusted_rate'], equal_var=False)
    metro_df = metro_box_plot_df(us_county_df)
    #print(metro_df.head())