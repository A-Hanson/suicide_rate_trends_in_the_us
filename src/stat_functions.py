import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from statsmodels.stats.multitest import multipletests


from initial_data_clean import us_county_df, us_county_agg_df, us_year_metro_race_df
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
    #print(bonf_correction)
    w_m_metro = []
    w_f_metro = []
    w_m_nonmetro = []
    w_f_nonmetro = []
    b_m_metro = []
    b_f_metro = []
    b_m_nonmetro = []
    b_f_nonmetro = []
    i_m_metro = []
    i_f_metro = []
    i_m_nonmetro = []
    i_f_nonmetro = []
    a_m_metro = []
    a_f_metro = []
    a_m_nonmetro = []
    a_f_nonmetro = []
    dataframe = us_year_metro_race_df
    for row in dataframe.iterrows():
        df = row[1]
        if df['gender'] == 'Male' and df['race'] == 'White' and df['metro_non_metro'] == 'Metro':
            w_m_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'White' and df.metro_non_metro == 'Metro':
            w_f_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Male' and df.race == 'White' and df.metro_non_metro == 'Nonmetro':
            w_m_nonmetro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'White' and df.metro_non_metro == 'Nonmetro':
            w_f_nonmetro.append(df.age_adjusted_rate)

        elif df.gender == 'Male' and df.race == 'Black or African American' and df.metro_non_metro == 'Metro':
            b_m_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'Black or African American' and df.metro_non_metro == 'Metro':
            b_f_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Male' and df.race == 'Black or African American' and df.metro_non_metro == 'Nonmetro':
            b_m_nonmetro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'Black or African American' and df.metro_non_metro == 'Nonmetro':
            b_f_nonmetro.append(df.age_adjusted_rate)

        elif df.gender == 'Male' and df.race == 'American Indian or Alaska Native' and df.metro_non_metro == 'Metro':
            i_m_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'American Indian or Alaska Native' and df.metro_non_metro == 'Metro':
            i_f_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Male' and df.race == 'American Indian or Alaska Native' and df.metro_non_metro == 'Nonmetro':
            i_m_nonmetro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'American Indian or Alaska Native' and df.metro_non_metro == 'Nonmetro':
            i_f_nonmetro.append(df.age_adjusted_rate)

        elif df.gender == 'Male' and df.race == 'Asian or Pacific Islander' and df.metro_non_metro == 'Metro':
            a_m_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'Asian or Pacific Islander' and df.metro_non_metro == 'Metro':
            a_f_metro.append(df.age_adjusted_rate)
        elif df.gender == 'Male' and df.race == 'Asian or Pacific Islander' and df.metro_non_metro == 'Nonmetro':
            a_m_nonmetro.append(df.age_adjusted_rate)
        elif df.gender == 'Female' and df.race == 'Asian or Pacific Islander' and df.metro_non_metro == 'Nonmetro':
            a_f_nonmetro.append(df.age_adjusted_rate)
    w_m_metro = np.array(w_m_metro)
    w_f_metro = np.array(w_f_metro)
    w_m_nonmetro = np.array(w_m_nonmetro)
    w_f_nonmetro = np.array(w_f_nonmetro)
    b_m_metro = np.array(b_m_metro)
    b_f_metro = np.array(b_f_metro)
    b_m_nonmetro = np.array(b_m_nonmetro)
    b_f_nonmetro = np.array(b_f_nonmetro)
    i_m_metro = np.array(i_m_metro)
    i_f_metro = np.array(i_f_metro)
    i_m_nonmetro = np.array(i_m_nonmetro)
    i_f_nonmetro = np.array(i_f_nonmetro)
    a_m_metro = np.array(a_m_metro)
    a_f_metro = np.array(a_f_metro)
    a_m_nonmetro = np.array(a_m_nonmetro)
    a_f_nonmetro = np.array(a_f_nonmetro)
    #left out b_f_nonmetro and a_f_nonmetro due to zero values
    lst_of_lst = [w_m_metro, w_f_metro, w_m_nonmetro, w_f_nonmetro, b_m_metro, b_f_metro, b_m_nonmetro, 
                i_m_metro, i_f_metro, i_m_nonmetro, i_f_nonmetro, a_m_metro, a_f_metro, a_m_nonmetro]
    labels = ('White Male Metro', 'White Female Metro', 'White Male Nonmetro', 'White Female Nonmetro', 
                'Black Male Metro', 'Black Female Metro', 'Black Male Nonmetro', 
                'Native American Male Metro', 'Native American Female Metro', 'Native American Male Nonmetro', 'Native American Female Nonmetro',
                'Asian Male Metro', 'Asian Female Metro', 'Asian Male Metro')
    simple_labels = ('White Male', 'White Female', 'White Male', 'White Female', 
                'Black Male', 'Black Female', 'Black Male', 
                'Native American Male', 'Native American Female', 'Native American Male', 'Native American Female',
                'Asian Male', 'Asian Female', 'Asian Male')
    y_pos = np.arange(len(labels))
    means = []
    for i in lst_of_lst:
        means.append(np.mean(i))
    means_sorted, label_sorted = zip(*sorted(zip(means, simple_labels)))
    # print(means)
    # print(type(means_sorted))
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(12,8))
    ax.barh(y_pos, means_sorted, align='center', color='tab:orange')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(label_sorted)
    ax.set_xlabel('Average of Age Adjusted Rate per 100,000')
    ax.set_title('Suicide Rates per 100,000')
    for i, v in enumerate(means_sorted):
        ax.text(v + 1, i - 0.25, str(np.around(v, decimals=1)), fontweight='bold')
    plt.tight_layout()
    plt.savefig('../images/group_metro.png')
    plt.show()
    
    
    F, p = stats.f_oneway(w_m_metro, w_f_metro, w_m_nonmetro, w_f_nonmetro, b_m_metro, b_f_metro, b_m_nonmetro, 
                i_m_metro, i_f_metro, i_m_nonmetro, i_f_nonmetro, a_m_metro, a_f_metro, a_m_nonmetro)
    # print(F)
    # print(p)

