# Background
Suicide rates in the United States have steadily increased over the past 18 years. I use data from the CDC Wonder compressed mortality database.
Driving Question: What factors can be observed within national suicide data that would help develop a predictive model?
![National Suicide Rate](images/annual_national_rate.png)

### Raw Data
![Data Info](images/raw_data_info.png)
![Data Middle](images/raw_data_middle.png)


# Data
In analyzing my data I used two different rates provided by the datasets. When looking at National level data I used the Age-Specific rate. Whereas when comparing counties to each other I used the Age-Adjusted rate.  I chose to use the Age-Adjusted rate to normalize my data in terms of counties’ population having different age group rates.
Example of how Age-Adjusted Rates are calculated from New Jersey Department of Health:
![Calculating Age-Adjusted Rates](images/age_adjusted_rates_calculation_example.png)

## Two Approaches to looking for meaning
### Male vs Female Suicide rates
![Annual Male vs Female Suicide Rates Bar Chart](images/annual_m_f_rate.png)

### County Urbanization Classification
The National Center for Health Statistics 2013 Urban-Rural classification scheme groups counties in the following six categories by population
![US county classification visual](images/urbanization_classification_visual.png)

![US counties by urbanization map](images/us_county_urbanization_codes.png)

![US counties aggregate suicide rate](images/aggregated_county_data_mainland.png)
![Alaska counties](images/aggregated_county_data_alaska.png)

# Statistics

I set my significance level to 0.05 with the intention of doing a Bonferroni correction.

### Male vs Female
Null Hypothesis: "The national male suicide rate average will equal the national female suicide rate average."

![Male vs Female Box Plot](images/m_f_rate_box_plot.png)

![Male vs Female T-Test](images/male_female_t_test.png)


### Urbanization Areas
Null Hypothesis: "The average suicide rate in metropolitan areas will be equal to the average suicide rate in non-metropolitan areas."

![Six Urbanization Codes Box Plot](images/national_six_metro_areas_box_plot.png)

![Metropolitan vs Non-Metropolitan Box Plot](images/national_metro_non_metro_box_plot.png)

![Metropolitan vs Non-Metropolitan T-Test](images/metro_non_metro_t_test.png)


#### Bonferroni Correction
* Male vs Female T-Test p-value: 8.1e-22
* Metropolitan vs Non-Metro T-Test p-value: 1.4e-42
* Corrected alpha 0.025