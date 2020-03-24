import sys
import pandas as pd
sys.path.append('../../../_Geocropper/geocropper')

from geocropper import *
from datetime import date


df_locations = pd.read_csv('../data/windturbineLocations.csv')
id = df_locations
id = id[(id['t_rd'] > 100) & (id['p_year'] < 2012) & (id['p_year'] > 2008)]

#geoc = geocropper.init(32.424911, -100.181007) #id3088504
#geoc = geocropper.init(35.055496, -118.351585) #id3048564
#geoc = geocropper.init(35.03509, -118.370285) #id3036492
#geoc = geocropper.init(35.044594, -118.380585)
#geoc = geocropper.init(43.837593, -83.23599)



for location in id.itertuples():

    long = round(location[26], 6)
    lat = round(location[27], 6)

    geoc = geocropper.init(lat,long)

    for i in range(14):
        year = 2006 + i
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        geoc.downloadAndCrop(str(start_date), str(end_date), "LANDSAT_ETM_C1", 90, 90, tileLimit=1, cloudcoverpercentage=5)



#downloads data for years specified in range

#for i in range(20):
    #year = 2000 + i
    #start_date = date(year, 1, 1)
    #end_date = date(year, 12, 31)
    #geoc.downloadAndCrop(str(start_date), str(end_date), "LANDSAT_ETM_C1", 90, 90, tileLimit=1, cloudcoverpercentage=5)



