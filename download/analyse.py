import sys
import os
import rasterio
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


path_data = '../data/locations'

df_center_meanbands = pd.DataFrame()

for folder in os.listdir(path_data):
    path_csv = path_data + '/' + folder


    for item in os.listdir(path_csv):

        if item.lower().endswith("_center_meanbands.csv"):
            path = path_csv + '/' + item

            data = pd.read_csv(path, sep=';')
            min = int(data['MIN'])
            max = int(data['MAX'])

            start = item.find("_") + len("_")
            end = item.find("_center_meanbands")
            year = int(item[start:end])

            df_temp = pd.DataFrame([[min, max, year]])
            df_center_meanbands = df_center_meanbands.append(df_temp, ignore_index=True)


count_min_smaller = 0
count_min_bigger = 0

count_max_smaller = 0
count_max_bigger = 0

for location in df_center_meanbands.itertuples():
    print(location)
    if (location[1] < location[3]):
        count_min_smaller = count_min_smaller + 1

    if (location[1] > location[3]):
        count_min_bigger = count_min_bigger + 1


    if (location[2] < location[3]):
        count_max_smaller = count_max_smaller + 1

    if (location[2] > location[3]):
        count_max_bigger = count_max_bigger + 1


print(count_min_smaller, count_min_bigger)
print(count_max_smaller, count_max_bigger)