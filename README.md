# Utah Opioid Prescriptions
## Data Analysis and Visualization

#### Motivation
Illicit opioid usage has spiked across the country. Much of this usage stems from what began as prescription usage. The [state of Utah](https://opendata.utah.gov/Public-Safety/Utah-Opioid-Prescription-Data-by-City-Zip-County-2/ivcs-mb6d) provides data on all opioid prescriptions written by healthcare providers across the state. The most recent data available are from 2015-2016. The [county-level](https://en.wikipedia.org/wiki/List_of_counties_in_Utah) and [municipality-level](https://en.wikipedia.org/wiki/List_of_municipalities_in_Utah) demographic data were scraped from Wikipedia. The geosjson file for the counties of Utah was obtained from the [Utah state mapserve](https://mapserv.utah.gov/arcgis/rest/services/PLSS/MapServer/layers).

I had two goals with this project:
1. Analyze the cities which had the most outsized prescription rates of opioids, and determine if any demographic factors influenced this rate.
2. Map the rate of opioid prescriptions by county, and visualize the largest per capita sources of opioids in the state

#### Methods
Much of the data cleaning and validation was done in Python, using the pandas library. This is where I merged in the population and demographic data.

I used R and the tidyverse library (primarily dplyr and ggplot2) to restructure, mutate, and visualize the data.

The choropleth map was created in Tableau, using a join on the geojson and the exported file from the Python script.

#### Outcomes
Salt Lake City has the bulk of the state's medical facilities, so it is not surprising that it is the largest source of opioid prescriptions, both in aggregate and per-capita. However, the data revealed that several smaller communities - for example Vernal, Utah, which has a population of only about 10,000 - are also large sources of these prescriptions. This information can be used to direct resources for potential monitoring and evaluation of the ongoing impacts of prescription usage of these drugs, as it relates to future illicit usage.

The choropleth helped visualize the counties with the highest per-capital prescription rates. Surprisingly, at the county level, Salt Lake no longer stood out as a particularly large source of opioids. Rather, Washington, Beaver, and Carbon Counties were the largest sources of these prescriptions. Additional analysis would be needed to find out the factors that impact these values. 
