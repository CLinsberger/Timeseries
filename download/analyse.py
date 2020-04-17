import sys
import os
import rasterio
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


path_data = '../data/locations'

for folder in os.listdir(path_data):
    path_csv = path_data + '/' + folder

    df_center_meanbands = pd.DataFrame(columns=['MIN', 'MAX'])
    i = 0
    for item in os.listdir(path_csv):

        if item.lower().endswith("_center_meanbands.csv"):
            path = path_csv + '/' + item

            data = pd.read_csv(path, sep=';')
            df_center_meanbands = df_center_meanbands.append(pd.Series([data['MIN'], data['MAX']], index = i), )
            i = i + 1


print(df_center_meanbands)