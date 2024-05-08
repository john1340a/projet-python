# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:23:04 2022

@author: SGJ2994A
"""
# importation of libraries
import os
import geopandas as gpd
import pandas as pd
import rasterio
from rasterstats import zonal_stats

# add path to files

path=""

os.chdir(path) # changing the working environment

# reading raster and vector files

raster=rasterio.open("zip://"+path+"projects.zip!/FUSION_DEC_2154.tif")

vectors=gpd.read_file("zip://"+path+"projects.zip!/project_layers.shp")

# path to raster and vectors in the zip file

tif="zip://"+path+"projects.zip!/FUSION_DEC_2154.tif"
vec="zip://"+path+"projects.zip!/project_layers.shp"
 
# checking CRS with a condition to reproject the layer if CRS are not identical

if raster.crs == vectors.crs.srs :
    print("Correct CRS!")
else : vectors.to_crs(epsg=2154)

# creating a function to extract the mean value within a polygon or a point
# and export it to CSV keeping only the id and mean columns

def mean_csv():
    
    # mean by zone in geojson specifying the band number because there are multiple bands and one band = one date
    
    geojson=zonal_stats(vec, 
                     tif, band=1,
                geojson_out=True,
                stats="mean")
    
    
    # creating a dataframe from the geojson
    json = gpd.GeoDataFrame.from_features(geojson)

    # geojson to csv with columns id(index), id_lot and mean(means)

    json[{'ID_LOT','mean'}].to_csv('test.csv', index=True)

# testing the function 
mean_csv()


# opening csv file
csv=pd.read_csv('test.csv')
