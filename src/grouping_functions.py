import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initial_data_clean import us_county_df

years = list(us_county_df['year'].unique().astype(int))
years.sort()

class GroupBy(object):
    '''
    Returns a dataframe with methods that allow for grouping by features for additional processing
    '''
    def __init__(self, df):
        self.self = self
        self.df = df.copy()

    def aggregate_county_stats(self, men_only=False):
        '''
        Features: 
        Male and female rates for each county, aggregated over time. 
        County urbanization code.

        '''
        if men_only == True:
            self.df = self.df[self.df['gender'] == 'Male']
            self.df = self.df.groupby(['county', 'urbanization_code'])['age_adjusted_rate'].mean()
            self.df = pd.DataFrame(self.df).reset_index() 
            self.df.drop('county', axis=1, inplace=True)
        else:
            self.df = self.df.groupby(['county', 'gender', 'urbanization_code'])['age_adjusted_rate'].mean()
            self.df = pd.DataFrame(self.df).reset_index() 
            self.df = pd.get_dummies(self.df, columns=['gender'])
            self.df.drop('county', axis=1, inplace=True)
        return self.df

    def metro_non_metro(self):
        metro_df = self.df[self.df['urbanization_code'] < 5]
        metro_df = metro_df.groupby('county')['age_adjusted_rate'].mean().reset_index()
        non_metro_df = self.df[self.df['urbanization_code'] >= 5]
        non_metro_df = non_metro_df.groupby('county')['age_adjusted_rate'].mean().reset_index()
        return metro_df, non_metro_df
    
    def state_county(self): ## figure this out
        self.df = self.df.groupby('county')
        return self.df
    
    def get_counts(self, col):  
        counts = {} 
        for x in self.df.col : 
            if x in counts : 
                counts [ x ] += 1 
            else : counts [ x ] = 1 
        return counts 



aggregate_county = GroupBy(us_county_df).aggregate_county_stats()
aggregate_county_males = GroupBy(us_county_df).aggregate_county_stats(men_only=True)

if __name__ == "__main__":
    # plt.style.use('fivethirtyeight')
    # fig, ax = plt.subplots(figsize=(10,10))
    # data = us_county_df['year']
    # bins = np.arange((len(years) + 1) - 0.5)
    # ax = plt.hist(data, bins)
    # plt.xticks(years)
    # plt.ylim((5000,9000))
    # plt.show()
    num_years = GroupBy(us_county_df).get_counts(col=year)
    print(num_years)