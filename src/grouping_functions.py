import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initial_data_clean import *

years = list(us_county_df['year'].unique().astype(int))
years.sort()

class GroupBy(object):
    '''
    Returns a dataframe with methods that allow for grouping by features for additional processing
    '''
    def __init__(self, df):
        self.self = self
        self.df = df.copy()

    def metro_non_metro(self):
        metro_df = self.df[self.df['urbanization_code'] < 5]
        non_metro_df = self.df[self.df['urbanization_code'] >= 5]
        return metro_df, non_metro_df
    
    def county_urbanization_age_rate(self): 
        self.df.drop('state', axis=1, inplace=True)
        self.df.drop('county', axis=1, inplace=True)
        self.df.drop('deaths', axis=1, inplace=True)
        self.df.drop('population', axis=1, inplace=True)
        self.df.drop('crude_rate', axis=1, inplace=True)
        self.df.drop('age_adj_95_lower_ci', axis=1, inplace=True)
        self.df.drop('age_adj_95_upper_ci', axis=1, inplace=True)
        return None

    def men_women_both_stats(self):
        '''
        Returns new dataframes with:
        Both Sexes,
        Male only,
        Female only.
        Ages: All, Race: All, injury_mech: All
        '''
        self.df = self.df.copy()
        self.df.drop('age_spec_lower_limit', axis=1, inplace=True)
        self.df.drop('age_spec_upper_limit', axis=1, inplace=True)
        self.df = self.df[self.df['age_group'] == 'All Ages']
        self.df.drop('age_group', axis=1, inplace=True)
        self.df = self.df[self.df['race'] == 'All races']
        self.df.drop('race', axis=1, inplace=True)
        self.df = self.df[self.df['injury_mechanism'] == 'All Mechanisms']
        self.df.drop('injury_mechanism', axis=1, inplace=True)
        both_sex_df = self.df[self.df['sex'] == 'Both sexes']
        male_df = self.df[self.df['sex'] == 'Male']
        female_df = self.df[self.df['sex'] == 'Female']
        #self.df.drop('sex', axis=1, inplace=True)

        return both_sex_df, male_df, female_df
    
    def age_group(self, group=0):
        '''
        0:'All Ages' 1:'< 15' 2:'15–24' 3:'25–44' 4:'45–64' 5:'65–74' 6:'75+'
        '''
        all_ages = self.df[self.df['age_group'] == 'All Ages']
        teen = self.df[self.df['age_group'] == '< 15']
        young_adult = self.df[self.df['age_group'] == '15-24']
        adult = self.df[self.df['age_group'] == '25-44']
        old_adult = self.df[self.df['age_group'] == '45-64']
        senior = self.df[self.df['age_group'] == '65-74']
        old_senior = self.df[self.df['age_group'] == '75+']
        if group == 0:
            return all_ages
        elif group == 1:
            return teen
        elif group== 2:
            return young_adult
        elif group== 3:
            return adult
        elif group== 4:
            return old_adult
        elif group== 5:
            return senior
        else:
            return old_senior

    def race(self):
        pass
        '''
        'All races' 'Hispanic' 'Non-Hispanic white' 'Non-Hispanic black'
        '''
        all_races = self.df[self.df['race'] == 'All races']
        hispanic = self.df[self.df['race'] == 'Hispanic']
        white = self.df[self.df['race'] == 'Non-Hispanic white']
        black = self.df[self.df['race'] == 'Non-Hispanic black']

    def injury_mech(self):
        '''
        'All Mechanisms' 'Cut/pierce' 'Drowning' 'Fall'
        'Fire/hot object or substance' 'Firearm' 'Poisoning'
        'All Other Transport' 'Unspecified' 'Suffocation' 'All Other Specified'
        '''
        pass



if __name__ == "__main__":
    gb = GroupBy(us_agg_df)
    both_sex, male, female = gb.men_women_both_stats()
    print(both_sex.head())
    # plt.style.use('fivethirtyeight')
    # fig, ax = plt.subplots(figsize=(10,10))
    # data = us_county_df['year']
    # bins = np.arange((len(years) + 1) - 0.5)
    # ax = plt.hist(data, bins)
    # plt.xticks(years)
    # plt.ylim((5000,9000))
    # plt.show()
