import sys
import os
import rasterio
import pandas as pd
import matplotlib.pyplot as plt
import math

sys.path.append('../../../_Geocropper/geocropper')

from geocropper import *

#pathImgData = 'D:/Masterarbeit/_Geocropper/geocropper/data/croppedTiles/US/lat32.424911_lon-100.181007/w90_h90'

pathImgData = 'D:/Masterarbeit/_Geocropper/geocropper/data/croppedTiles/US/lat43.837593_lon-83.23599/w90_h90'



#get lat from path
start = pathImgData.find("lat") + len("lat")
end = pathImgData.find("_lon")
lat = pathImgData[start:end]

#get lon from path
start = pathImgData.find("_lon") + len("_lon")
end = pathImgData.find("/w")
lon = pathImgData[start:end]

#read the location file and search for the id
df_locations = pd.read_csv('../data/windturbineLocations.csv')

#df_locations =pd.read_csv('D:/Masterarbeit/Timeseries/Timeseries/data/windturbineLocations.csv')

id = df_locations

#find the location via lat long from file
abs_tol = 0.00001
id = id[((id['Lat'].astype(float) - float(lat)).abs() < abs_tol) & ((id['Long'].astype(float) - float(lon)).abs() < abs_tol) ]

case_id = str(int(id['case_id']))
p_year = str(int(id['p_year']))

#create dataFrames for the pixel_values
df = pd.DataFrame()
df_mean = pd.DataFrame()
df_center_meanbands = pd.DataFrame()
df_mean_meanbands = pd.DataFrame()

for folder in os.listdir(pathImgData):

    path_folder = pathImgData + '/' + folder

    for item in os.listdir(path_folder):

        # for each tif file
        if item.lower().endswith(".tif"):

            # set path of image file
            path = path_folder + '/' + item

            img = rasterio.open(str(path))

            #Get Band and year from folder- / filename
            band = item[41:43]
            year = folder[17:21]

            if(band == "B6"):
                band = item[41:50]

            center_x = int(img.width/2 - 1)
            center_y = int(img.height/2 - 1)

            if(band != "BQ"):
                df.loc[year, band] = img.read(1)[center_x ][center_y]
                df_mean.loc[year, band] = img.read(1).mean()




#save plot with center
df = df.sort_index()
df = df.loc[~(df == 0).all(axis=1)]
df.plot()
plt.savefig(str('../data/' + case_id + '_' + p_year + '.png'))
plt.clf()

df_center_meanbands['all bands'] = df.mean(axis = 1)
df_center_meanbands.plot()
plt.savefig(str('../data/' + case_id + '_' + p_year + '_center_meanbands.png'))
plt.clf()

#save plot with mean
df_mean = df_mean.sort_index()
df_mean = df_mean.loc[~(df_mean == 0).all(axis=1)]
df_mean.plot()
plt.savefig(str('../data/' + case_id  + '_' + p_year + '_mean.png'))
plt.clf()

df_mean_meanbands['all bands'] = df_mean.mean(axis = 1)
df_mean_meanbands.plot()
plt.savefig(str('../data/' + case_id  + '_' + p_year + '_mean_meanbands.png'))
plt.clf()