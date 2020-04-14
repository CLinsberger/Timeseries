import sys
import pandas as pd
sys.path.append('../../../_Geocropper/geocropper')

from geocropper import *
from datetime import date


df_locations = pd.read_csv('../data/windturbineLocations.csv')
id = df_locations
id = id[(id['t_rd'] > 100) & (id['p_year'] < 2012) & (id['p_year'] > 2008)]

#load case_id of last tile
f = open("../data/lastTile.txt", "r")
last_turbine_case_id = f.read()
f.close()

if(last_turbine_case_id != ''):
    id = id.loc[last_turbine_case_id:]
    print("Dataset to continue found!")

for location in id.itertuples():

    long = round(location[26], 6)
    lat = round(location[27], 6)

    geoc = geocropper.init(lat,long)

    for i in range(14):
        year = 2006 + i
        start_date = date(year, 8, 1)
        end_date = date(year, 10, 31)
        geoc.downloadAndCrop(str(start_date), str(end_date), "LANDSAT_ETM_C1", 90, 90, tileLimit=1, cloudcoverpercentage=10)

    f = open("../data/lastTile.txt", "w")
    f.write(str(location[0]))
    f.close()



def download (dataframe, start_date, end_date):
    df = dataframe

