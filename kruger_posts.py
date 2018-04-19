# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:40:36 2018
AutoGIS Lesson 2 Problem 2

@author: harrisab2
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Read in data using pandas
dF = pd.read_csv('some_posts.csv')

# Iterate over dF rows and insert point objects into new column 'geometry'
dF['geometry'] = [Point(xy) for xy in zip(dF.lon, dF.lat)]

# drop uneeded columns
dFclean = dF.drop(['lon', 'lat'], axis=1)

# convert to GeoDataFrame with crs WGS84 (epsg 4326)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(dFclean, crs=crs, geometry=dF['geometry'])

# save shapefile
outshp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_2\Kruger_posts.shp'

# create a simple map of this points 
gdf.plot()

     
    