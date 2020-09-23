# Background
Suicide rates in the United States have steadily increased over the past 18 years. I use data from the CDC Wonder compressed mortality database.
<br>
**Driving Question:** What factors can be observed within national suicide data that would help develop strong story points that can be visualized graphically?
<p align='center'>
<img src ='images/annual_national_rate.png' height='600'><br>
<kbd>Note: y-axis starts at a rate of 6 suicides per 100,000</kbd>
</p>

## Raw Data

County Level Info              | County Level Snapshot
:-----------------------------:|:-----------------------------:
<img src='images/raw_data_info.png' width=400>  | <img src='images/raw_data_middle.png' width=400> 
<br>
<br>
<br>

---
<br>

In analyzing my data, I used two different rates provided by the datasets. When looking at National level data I used the Age-Specific rate. Whereas when comparing counties to each other, I used the Age-Adjusted rate.  I chose to use the Age-Adjusted rate to normalize my data in terms of counties’ population having different age group rates.

<br>

<p align='center'>
<kbd>Example of how Age-Adjusted Rates are calculated for Diabetes Mellitus, courtesy of New Jersey Department of Health:</kbd>
<img src ='images/age_adjusted_rates_calculation_example.png' height='600'>
</p>
<br>
<br>

---
<br>
<br>

# Data Dive

<br>
<br>

## Two Approaches on the Data
### Male vs Female Suicide rates
When thinking about larger scale trends, I first looked into the annual Age-Specific rates for Males and Females within the United States. Looking at the data for the years given, there was an immediate visual difference between the rates. 

<p align='center'>
<img src ='images/annual_m_f_rate.png' height='600'><br>
<kbd>Note: y-axis starts at a rate of 10 suicides per 100,000</kbd>
</p>


---

### County Urbanization Classification
My second approach to the data was to use the Age-Adjusted suicide rates for the counties to see if there was a difference between types of urban classifications. I used the CDC's National Center for Health Statistics (NCHS) 2013 Urban-Rural classification scheme to categorize the counties.

<p align='center'>
<kbd>2013 NCHS Urban-Rural classification scheme for counties:</kbd>
<img src ='images/urbanization_classification_visual.png' width='700'>
</p>

#### Examples of each type of county:
1. Large Central Metro - Denver County
1. Large Fringe Metro - Arapahoe County
1. Medium Metro - Boulder County
1. Small Metro - Pueblo County
1. Micropolitan - Summit County
1. Non-Core - Gunnison County

<br>
<br>

<p align='center'>
<kbd>United States counties by urbanization codes:</kbd>

![US counties by urbanization map](images/us_county_urbanization_codes.png) 
</p>
<br>
<p align='center'>
<kbd>United States counties by aggregate age-adjusted suicide rate:</kbd>

![US counties aggregate suicide rate](images/aggregated_county_data_mainland.png)
</p>
<br>
<br>
<p align='center'>
<kbd> Alaskan counties by aggregate age-adjusted suicide rate:</kbd>
<br>
<br>
<img src='images/aggregated_county_data_alaska.png' height='500'>

</p>

<br>
<br>

<br>
<br>

---

<br>
<br>
Seeing how much of the higher rates were concentrated in Alaska, I filled in the rates based just on the range seen within the continental United States. 

County Urbanization Codes      | Continental Counties Suicide Rates
:-----------------------------:|:-----------------------------:
<img src='images/us_county_urbanization_codes.png' width=400>  | <img src='images/continental_counties.png' width=400> 
<br>
<br>

<img src='images/continental_counties.png'>
<br>
<br>


---

# Statistics

I set my significance level to 0.05 and did a Bonferroni Correction after I ran my tests.
I ran T-Tests comparing the rates of Male vs Female suicide, and Metropolitan vs Non-Metropolitan County suicide. 

### Male vs Female
**Null Hypothesis: "The national male suicide rate average will be equal to the national female suicide rate average."**

<br>

<p align='center'>
<img src='images/m_f_rate_box_plot.png' width=700></p>
<br>
<br>
<p align='center'>
<img src='images/male_female_t_test.png' width=700>
</p>

---

### Metropolitan vs Non-Metropolitan Counties
**Null Hypothesis: "The average suicide rate in metropolitan areas will be equal to the average suicide rate in non-metropolitan areas."**
<br>
<br>
First, I visualized each of the six different county classification codes by the age-adjusted rates. What stood out to me was the outliers seen in the Non-Core classification. This was in line with what what I was seeing on my mapping with the counties in Alaska.  
<br>
<p align='center'>
<img src='images/national_six_metro_areas_box_plot.png'></p>
<br>

Next, I combined the four metropolitan codes (1-4) and the two non-metropolitan codes (5 & 6) to visualize the data before I ran my t-test.

<br>

<p align='center'>
<img src='images/national_metro_non_metro_box_plot.png' width=700></p>
<br>
<p align='center'>
<img src='images/metro_non_metro_t_test.png' width=700></p>
<br>

---

Thinking about outliers, my thoughts immediately went to how Alaska looked on the map. I decided to re-run my tests excluding the data from Alaska to see if there was a difference between the Metropolitan and Non-metropolitan counties in the continental United States.

<br>

<p align='center'>
<img src='images/no_alaska_metro_non_metro_box_plot.png' width=700></p>
<br>
<p align='center'>
<img src='images/no_ak_metro_non_metro_t_test.png' width=700></p>
<br>

#### Bonferroni Correction
* Male vs Female T-Test p-value: **1.2e-21**
* Metropolitan vs Non-Metro T-Test p-value: **2.1e-42**
* Metropolitan vs Non-Metro (No Alaska) T-Test p-value: **3.9e-42**
* Corrected alpha **0.017**

I rejected all my null hypothesis.

<br>

---

<br>

## Next Steps
* Analyze the mechanisms used to commit suicide
* Analyze the distribution of the age-groups committing suicide
* Create an interactive display that would allow user to:
    * Display the change in county level data over time
    * Zoom in on specific states
* Add county economic data to county age-adjusted rates and run KMeans to look for different ways to groups counties
    