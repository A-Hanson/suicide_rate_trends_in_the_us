import pandas as pd

three_county_df = pd.read_excel('../data/suicide_occurances_15_19_edited.xlsx', index_col=0)
us_mortality_df = pd.read_csv('../data/NCHS_Injury_Mortality_United_States.csv')
us_county_agg_df = pd.read_csv('../data/both_genders_all_states.txt', sep="\t")

files = ['../data/al_ak_az_ar_by_year.txt',\
        '../data/ca_co_ct_de_dc_by_year.txt',\
        '../data/fl_ga_hi_id_il_in_ia.txt',\
        '../data/ks_ky_la_me_md_ma_mi_by_year.txt',\
        '../data/mn_ms_mo_mt_ne_nv_nh_by_year.txt',\
        '../data/nj_nm_ny_nc_nd_oh_ok_by_year.txt',\
        '../data/or_pa_ri_sc_sd_tn_tx_by_year.txt',\
        '../data/ut_vt_va_wa_wv_wi_wy_by_year.txt']

def merge_us_counties(lst_of_files, num_files):
    frames = []
    for i in range(num_files):
        for j in lst_of_files:
            i = pd.read_csv(j, sep="\t")
            frames.append(i)
    return pd.concat(frames)


us_county_df = merge_us_counties(files, len(files))

def clean_counties(df):
    df = df.copy()
    df.drop('Notes', axis=1, inplace=True)
    df.drop('State Code', axis=1, inplace=True)
    df.drop('County Code', axis=1, inplace=True)
    df.drop('2013 Urbanization', axis=1, inplace=True)
    df.drop('Year Code', axis=1, inplace=True)
    df.drop('Gender Code', axis=1, inplace=True)
    df.dropna(axis=0, thresh=1, inplace=True)
    df.rename(columns={
        'State': 'state',
        'County': 'county',
        '2013 Urbanization Code': 'urbanization_code',
        'Year': 'year',
        'Gender': 'sex',
        'Deaths': 'deaths',
        'Population': 'population',
        'Crude Rate': 'crude_rate',
        'Age Adjusted Rate': 'age_adjusted_rate',
        'Age Adjusted Rate Lower 95% Confidence Interval': 'age_adj_95_lower_ci',
        'Age Adjusted Rate Upper 95% Confidence Interval': 'age_adj_95_upper_ci',
        'Age Adjusted Rate Standard Error': 'age_adj_95_se'}, inplace=True)
    df = df[df['deaths'] != 'Missing']
    df['deaths'] = df['deaths'].astype(int)
    df['population'] = df['population'].astype(int)
    df['crude_rate'] = df['crude_rate'].str.replace(r"\(.*\)", "")
    df['crude_rate'] = df['crude_rate'].astype(float)
    df['age_adjusted_rate'] = df['age_adjusted_rate'].str.replace(r"\(.*\)", "")
    df['age_adjusted_rate'] = df['age_adjusted_rate'].astype(float)
    df['age_adj_95_lower_ci'] = df['age_adj_95_lower_ci'].str.replace(r"\(.*\)", "")
    df['age_adj_95_lower_ci'] = df['age_adj_95_lower_ci'].astype(float)
    df['age_adj_95_upper_ci'] = df['age_adj_95_upper_ci'].str.replace(r"\(.*\)", "")
    df['age_adj_95_upper_ci'] = df['age_adj_95_upper_ci'].astype(float)
    df['age_adj_95_se'] = df['age_adj_95_se'].str.replace(r"\(.*\)", "")
    df['age_adj_95_se'] = df['age_adj_95_se'].astype(float)
    return df

us_county_df = clean_counties(us_county_df)

def clean_agg_counties(df):
    df = df.copy()
    df.drop('Notes', axis=1, inplace=True)
    df.drop('State Code', axis=1, inplace=True)
    df.drop('County Code', axis=1, inplace=True)
    df.drop('2013 Urbanization', axis=1, inplace=True)
    df.drop("% of Total Deaths", axis=1, inplace=True)
    df.dropna(axis=0, thresh=1, inplace=True)

    df.rename(columns={
        'State': 'state',
        'County': 'county',
        '2013 Urbanization Code': 'urbanization_code',
        'Deaths': 'deaths',
        'Population': 'population',
        'Crude Rate': 'crude_rate',
        'Age Adjusted Rate': 'age_adjusted_rate',
        'Age Adjusted Rate Lower 95% Confidence Interval': 'age_adj_95_lower_ci',
        'Age Adjusted Rate Upper 95% Confidence Interval': 'age_adj_95_upper_ci',
        'Age Adjusted Rate Standard Error': 'age_adj_95_se'}, inplace=True)
    df = df[df['deaths'] != 'Missing']
    df['deaths'] = df['deaths'].astype(int)
    df['population'] = df['population'].astype(int)
    df['crude_rate'] = df['crude_rate'].str.replace(r"\(.*\)", "")
    df['crude_rate'] = df['crude_rate'].astype(float)
    df['age_adjusted_rate'] = df['age_adjusted_rate'].str.replace(r"\(.*\)", "")
    df['age_adjusted_rate'] = df['age_adjusted_rate'].astype(float)
    return df

us_county_agg_df = clean_agg_counties(us_county_agg_df)

def clean_us_mortality(df):
    df = df[df['Injury Intent'] == 'Suicide']
    df.drop('Injury Intent', axis=1, inplace=True)
    df.drop('Age Adjusted Rate', axis=1, inplace=True)
    df.drop('Age Adjusted Rate Standard Error', axis=1, inplace=True)
    df.drop('Age Adjusted Rate Lower Confidence Limit', axis=1, inplace=True)
    df.drop('Age Adjusted Rate Upper Confidence Limit', axis=1, inplace=True)
    df.dropna(axis=0, thresh=1, inplace=True)
    df.rename(columns={
        'Year': 'year',
        'Sex': 'sex',
        'Age Group (Years)': 'age_group',
        'Race': 'race',
        'Injury Mechanism': 'injury_mechanism',
        'Deaths': 'deaths',
        'Population': 'population',
        'Age Specific Rate': 'age_specific_rate',
        'Age Specific Rate Lower Confidence Limit': 'age_spec_lower_limit',
        'Age Specific Rate Upper Confidence Limit': 'age_spec_upper_limit',
        'Age Specific Rate Standard Error': 'age_spec_se'}, inplace=True)
    df = df[df.deaths != 0]
    return df

us_agg_df = clean_us_mortality(us_mortality_df)

if __name__ == "__main__":
    #print(three_county_df.head)
    us_agg_df = clean_us_mortality(us_mortality_df)
    print(us_agg_df['injury_mechanism'][:10])



