#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import folium


# In[2]:


#read in the two csv files: ut_op is the opioid prescription data, and ut_counties is the county population data
ut_op = pd.read_csv("Utah_Opioid_Prescription_Data_by_City_Zip___County_2015_2016.csv")
ut_counties = pd.read_csv("ut_county_pops.csv")


# In[3]:


#find the total number of opioid prescriptions for each county using groupby method
cnty_op_claim = ut_op.groupby('County').OpioidClaimCount.sum()


# In[4]:


#merge the county level opioid data with the county population data. merge on county name.
cnty_op_claim = pd.merge(cnty_op_claim, ut_counties, how = 'left', on = 'County')


# In[5]:


#create a new column that shows the number of opioid perscriptions per person in the county
cnty_op_claim['op_scrip_rate'] = cnty_op_claim['OpioidClaimCount']/cnty_op_claim['Population']


# In[6]:


#rename the county column so it matches the attribute in the 
#geojson file, and change all strings in the dataframe to upper case
cnty_op_claim = cnty_op_claim.rename(columns={'County' : 'NAME'})
cnty_op_claim.columns = map(lambda x: str(x).upper(), cnty_op_claim.columns)
cnty_op_claim['NAME'] = cnty_op_claim['NAME'].str.upper()


# In[7]:


#make a choropleth map where color is determined based on op_scrip_rate
#use geojson file for county shape data
county_map = '051acb66-8e4b-4c24-9da8-057bfdb69dcf202041-1-1ikt18k.0n4a.geojson'

#establish features of final map (center and zoom)
m = folium.Map(location=[40,-111], zoom_start=7)

#create choropleth
m.choropleth(
 geo_data=county_map,
 name='choropleth',
 data=cnty_op_claim,
 columns=['NAME', 'OP_SCRIP_RATE'],
 key_on='feature.properties.NAME',
 fill_color='BuPu',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Opioid Prescriptions Per Person (2015-2016)'
)

#save choropleth as html file
m.save('UT_op_choropleth.html')

