import sys
import pandas as pd
from datetime import date

# This file creates a dataframe for the download function to work with
# run this with your conditions before you start the download
# works at the moment only with the US Windturbine Database https://eerscmap.usgs.gov/uswtdb/

df_locations = pd.read_csv('../data/windturbineLocations.csv')
id = df_locations
id = id[(id['t_rd'] > 100) & (id['p_year'] < 2012) & (id['p_year'] > 2008)]

print(id)

id.to_pickle('../data/currentProjekt.pkl')
