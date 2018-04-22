# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:40:36 2018
AutoGIS Lesson 2 Problem 2, 3

@author: harrisab2
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString

###################
#### Problem 2 ####
################### 

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
# gdf.plot()

###################
#### Problem 3 ####
###################   
"""
In this problem the aim is to calculate the distance in meters that the 
individuals have travelled according the social media posts 
(Euclidian distances between points).
"""
# Reproject data from WGS84 to EPSG:32735 (UTM Zone 35S, South Africa)
gdf = gdf.to_crs(epsg=32735)

# group data based on userid 
grouped = gdf.groupby('userid')

# Create an empty geodataframe movements
movements = gpd.GeoDataFrame()

"""
For each user:
sort the rows by timestamp
create LineString objects based on the points
add the geometry and the userid into the GeoDataFrame you created in the last step
Determine the CRS of the movements GeoDataFrame to EPSG:32735 (epsg code: 32735)
"""
# sort rows by timestamp (AttributeError)
# grouped.sort_values(['timestamp'])

# create linestring objects based on points (ValueError)
grouped['geometry'].apply(lambda x : LineString(list(x)))
    
# add geometry     


    
    
    
    
    
    

 