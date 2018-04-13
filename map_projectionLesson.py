# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 18:28:26 2018
AutoGIS Lesson 2 Part 2
Map Projections
@author: harrisab2
"""
from fiona.crs import from_epsg
import geopandas as gpd
from shapely.geometry import Point

# filepath to Europe borders shapefile
fp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_2\data\Europe_borders.shp'

# read data in
data = gpd.read_file(fp)

# check current CRS from .crs attribute
data.crs

# make a copy of data
data_proj = data.copy()

# change projection to one reccomended by European commission (Lambert Azimuthal Equal Area)
data_proj = data_proj.to_crs(epsg=3035)

# add raw projection data from proj3
proj4text = '+proj=laea +lat_0=52 +lon_0=10 +x_0=4321000 +y_0=3210000 +ellps=GRS80 +units=m +no_defs '
data2_proj2 = data.to_crs(proj4text)

# generate ESRI azimuthal equal area  centered on Helsinki
proj4text_LAEA = '+proj=aeqd +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs'

# Helsinki coords
hki_lat = 60.1666
hki_lon = 24.9417

# use string modification
proj4text_LAEA_hki = '+proj=aeqd +lat_0={0} +lon_0={1} +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs'.format(hki_lat, hki_lon)

# write to file
data_wec = data.to_crs(proj4text_LAEA)

# calculate the centroids of countries 
data_wec['centroid'] = data_wec.centroid

# create a point for Helsinki
hki_Point = Point(hki_lon, hki_lat)

# calculate distance function
# 
def calculateDistance(row, dest_geom, src_col='geometry', target_col='distance'):
    """
    Calculates the distance between a single Shapely Point geometry and a GeoDataFrame with Point geometries.

    Parameters
    ----------
    dest_geom : shapely.Point
        A single Shapely Point geometry to which the distances will be calculated to.
    src_col : str
        A name of the column that has the Shapely Point objects from where the distances will be calculated from.
    target_col : str
        A name of the target column where the result will be stored.
    """
    # Calculate the distances
    dist = row[src_col].distance(dest_geom)
    # Tranform into kilometers
    dist_km = dist/1000
    # Assign the distance to the original data
    row[target_col] = dist_km
    return row
    
# Create a geoseries (column in geodataframe) of Helsinki point
hki_series = gpd.GeoSeries([hki_Point], crs=from_epsg(4326))

# reproject for other dataframe
hki_series = hki_series.to_crs(proj4text_LAEA_hki)

# get the shapely object from geoseries
hki_geo = hki_series.get(0)

# apply calculateDistance function to GeoDataFrame. after comma specify inputs. Axis=1 specifies to iterate row by row
data_wec = data_wec.apply(calculateDistance, dest_geom=hki_geo, src_col='centroid', target_col='dist_to_helsinki', axis=1)


