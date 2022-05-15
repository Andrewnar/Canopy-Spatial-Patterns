import pandas as pd
import numpy as np
import pyproj
import csv

def load_species(data_file, species_name, inProj, outProj):
    with open(data_file) as f:
        data = []
        for line in f:
            line = line.split(",")[:9]
            if(species_name != "ALL" and species_name != str(line[3])):
                continue

            #======= pyproj v>2.2

            # inProj = pyproj.Proj(init='epsg:3015')
            # outProj = pyproj.Proj(init='epsg:4326')
            # x1, y1 = (line[0], line[1])
            # x2, y2 = pyproj.transform(inProj, outProj, x1, y1)
            # line[0], line[1] = (x2, y2)

            #======= pyproj v<=2.2

            proj = pyproj.Transformer.from_crs(3035, 4326, always_xy=True)
            x1, y1 = (line[0], line[1])
            x2, y2 = proj.transform(x1, y1)
            line[1], line[0] = (x2, y2)

            data.append(line)
        data = np.array(data)
    return data
    
def load_weather(data_file):
    with open(data_file) as f:
        data = []
        for line in f:
            data.append(line)
        data = np.array(data)
    return data

def df_to_file(df, target):
    data = np.array(df)
    np.savetxt(target, data, delimiter = ",", fmt = '%s')

def clean_file(data_file, target):
    with open(data_file) as f:
        data = []
        data.append(["X","Y","COUNTRY","SPECIES NAME", "DBH-1","DBH-2","NFI","FF","BS"])
        for line in f:
            if(line[0] == '\n'):
                continue
            line = line.split(",")[:9]
            data.append(line)
        data = np.array(data, dtype=object)
    df_to_file(data, target)