import sys
import pandas as pd

import csv

df_locations = pd.read_csv('../data/windturbineLocations.csv')

id = df_locations

id = id[(id['t_rd'] > 100) & (id['p_year'] < 2012) & (id['p_year'] > 2008)]

print(id[['case_id' , 't_rd', 'p_year']])






