import csv
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

from dataset import load_species
from dataset import df_to_file
from dataset import clean_file

# Global Variables
data_file = "data\EUForestspecies.csv"
location_data = "models/test.csv"
tree_data = "models/abiesAlba.csv"
fp = "data/borders/Europe_borders.shp"
inCoords = "'espg:3035'"
outCoords = "'espg:4326'"

border_data = gpd.read_file(fp)
border_data_proj = border_data.copy()

fig, ax = plt.subplots(figsize = (15,15))
border_data.plot(ax = ax)


# clean_file(location_data, "models/abiesAlba.csv")

# border_data.plot(facecolor='gray')
# plt.title("ESPG:3015");
# # Remove empty white space around the plot
# plt.tight_layout()
# # # Plot the one with ETRS-LAEA projection
# print(border_data_proj.plot(facecolor='blue'))
