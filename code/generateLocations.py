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

# df_to_file [data, file_target_location]
df_to_file(df, "models/test.csv")


