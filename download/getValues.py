import sys
import os
import rasterio
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.append('../../../_Geocropper/geocropper')

from geocropper import *

def save_values(df: pd.DataFrame, mode: str, case_id: str, p_year: str, lat: str, lon: str):

    #creates a new folder with case Id, built year, latitude and longitude to save the files there
    full_data_path = '../data/' + case_id + '_' + p_year + '_' + 'lat' + lat + '_' + 'lon' + lon
    Path(full_data_path).mkdir(parents=True, exist_ok=True)

    df_mm = pd.DataFrame()
    df.plot()

    if(mode == 'center'):
        df_mm['MIN'] = df[df.gt(0)].idxmin(axis=0)
        df_mm['MAX'] = df[df.gt(0)].idxmax(axis=0)
        df_mm.to_csv(str(full_data_path + '/' + case_id + '_' + p_year + '_center.csv'), sep=';')
        plt.savefig(str(full_data_path + '/' + case_id + '_' + p_year + '.png'))

    if (mode == 'mean'):
        df_mm['MIN'] = df[df.gt(0)].idxmin(axis=0)
        df_mm['MAX'] = df[df.gt(0)].idxmax(axis=0)
        df_mm.to_csv(str(full_data_path + '/' + case_id + '_' + p_year + '_mean.csv'), sep=';')
        plt.savefig(str(full_data_path + '/' + case_id + '_' + p_year + '_mean.png'))

    if (mode == 'center_meanbands'):
        df_mm['MIN'] = df[df.gt(0)].idxmin(axis=0)
        df_mm['MAX'] = df[df.gt(0)].idxmax(axis=0)
        df_mm.to_csv(str(full_data_path + '/' + case_id + '_' + p_year + '_center_meanbands.csv'), sep=';')
        plt.savefig(str(full_data_path + '/' + case_id + '_' + p_year + '_center_meanbands.png'))

    if (mode == 'mean_meanbands'):
        df_mm['MIN'] = df[df.gt(0)].idxmin(axis=0)
        df_mm['MAX'] = df[df.gt(0)].idxmax(axis=0)
        df_mm.to_csv(str(full_data_path + '/' + case_id + '_' + p_year + '_mean_meanbands.csv'), sep=';')
        plt.savefig(str(full_data_path + '/' + case_id + '_' + p_year + '_mean_meanbands.png'))

    plt.clf()
    plt.cla()
    plt.close()

croppedImagePath = 'D:/Masterarbeit/_Geocropper/geocropper/data/croppedTiles/US'

#creates the plots and csvs for every croppedTile Folder in the data geocropper directory

for location in os.listdir(croppedImagePath):
    pathImgData = croppedImagePath + '/' + location + '/w90_h90'
    print(pathImgData)

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
                    df.loc[year, band] = img.read(1)[center_x][center_y]
                    df_mean.loc[year, band] = img.read(1).mean()


    #save plot with center
    df = df.sort_index()
    df = df.loc[~(df == 0).all(axis=1)]
    save_values(df, 'center', case_id, p_year, lat, lon)

    #center and mean over all bands
    df_center_meanbands['all bands'] = df.mean(axis = 1)
    save_values(df_center_meanbands, 'center_meanbands', case_id, p_year, lat, lon)

    #save plot with mean
    df_mean = df_mean.sort_index()
    df_mean = df_mean.loc[~(df_mean == 0).all(axis=1)]
    save_values(df_mean, 'mean', case_id, p_year, lat, lon)

    #mean and mean over all bands
    df_mean_meanbands['all bands'] = df_mean.mean(axis = 1)
    save_values(df_mean_meanbands, 'mean_meanbands', case_id, p_year, lat, lon)




