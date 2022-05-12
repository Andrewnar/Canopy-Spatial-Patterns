import csv
import pandas as pd
import numpy as np
# import geopandas as gpd

from dataset import load_species
from dataset import df_to_file

# Global Variables
data_file = "data\EUForestspecies.csv"
inCoords = "'espg:3035'"
outCoords = "'espg:4326'"

# load_species [file_name, Species Name] if ALL type "ALL"

df = load_species(data_file, "Abies alba", inCoords, outCoords)

# get in Europ borders shapefile
fp = "data/borders/Europe_borders.shp"
# border_data = gpd.read_file(fp)

# border_data_proj = border_data.copy()

# import matplotlib.pyplot as plt
# border_data.plot(facecolor='gray')
# plt.title("ESPG:3015");
# # Remove empty white space around the plot
# plt.tight_layout()
# # Plot the one with ETRS-LAEA projection
# print(border_data_proj.plot(facecolor='blue'))




# df_to_file [data, file_target_location]
df_to_file(df, "models/test.csv")


