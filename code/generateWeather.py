import csv
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from dask import dataframe as dd

from dataset import load_species
from dataset import load_weather
from dataset import df_to_file
from dataset import clean_file

# Global Variables
data_file = "data/weather/rr.csv"
location_data = "../data/weather/clean_rr.csv"
inCoords = "'espg:3035'"
outCoords = "'espg:4326'"

dask_df = dd.read_csv(data_file)
print(dask_df[4.84986])
