import pandas as pd
import numpy as np
import pyproj
import csv

def load_species(data_file, species_name, inProj, outProj):
    with open(data_file) as f:
        data = []
        for line in f:
            line = line.split(",")[:10]

            #======= pyproj v>2.2

            # inProj = pyproj.Proj(init='epsg:3015')
            # outProj = pyproj.Proj(init='epsg:4326')
            # x1, y1 = (line[0], line[1])
            # x2, y2 = pyproj.transform(inProj, outProj, x1, y1)
            # line[0], line[1] = (x2, y2)

            #======= pyproj v<=2.2

            # proj = pyproj.Transformer.from_crs(3015, 4326, always_xy=True)
            # x1, y1 = (line[0], line[1])
            # x2, y2 = proj.transform(x1, y1)
            # line[0], line[1] = (x2, y2)

            #======= osgeo


            # pointX = float(line[0])
            # pointY = float(line[1])

            # # Spatial Reference System
            # inputEPSG = 3015
            # outputEPSG = 4326

            # point = ogr.Geometry(ogr.wkbPoint)
            # point.AddPoint(pointX, pointY)

            # # create coordinate transformation
            # inSpatialRef = osr.SpatialReference()
            # inSpatialRef.ImportFromEPSG(inputEPSG)

            # outSpatialRef = osr.SpatialReference()
            # outSpatialRef.ImportFromEPSG(outputEPSG)

            # coordTransform = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

            # # transform point
            # point.Transform(coordTransform)

            # # print point in EPSG 4326
            # print(point.GetX(), point.GetY())



            if(species_name == "ALL" or species_name == str(line[3])):
                data.append(line)
        data = np.array(data)
    return data
    
def df_to_file(df, target):
    data = np.array(df)
    np.savetxt(target, data, delimiter = ",", fmt = '%s')