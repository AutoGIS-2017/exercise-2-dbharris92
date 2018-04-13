# -*- coding: utf-8 -*-
"""
Spyder Editor
AutoGIS lesson 2 geopandas
This is a temporary script file.
"""

import geopandas as gpd

# set filepath
fp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_2\Data\DAMSELFISH_distributions.shp'

# read file using gpd.read_file()
data = gpd.read_file(fp)

# write first 50 rows to a new shapefile
out = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_2\Data\DAMSELFISH_distributions_SELECTION.shp'

# select first 50 rows
selection = data[0:50]

# write above rows into a new Shapefile (default output file format for geopandas)
selection.to_file(out)

# Select only specific columns with []
data['geometry'].head()

# make a selection of first five rows
selection = data[0:5]

# Iterate over the selected rows using .iterrows() MUST USE ITERROWS TO ITERATE OVER DATAFRAME
for index, row in selection.iterrows():
    # calculate area for row geometry only
    poly_area = row['geometry'].area
    # {0} and {1:.3f} are text formatting
    # curly brackets take .format inputs and print them
    print('Polygon area at index {0} is: {1:.2f}.'.format(index, poly_area))
    
# create a new column of individual polygon areas
selection['area'] = selection.area

# find maximum, mean or minimum area
#max_area = selection['area'].max()
#mean_area = selection['area'].mean()
#min_area = selection['area'].min()

# make a geodataframe from scratch 
# import necessary modules
from shapely.geometry import Point, Polygon
from fiona.crs import from_epsg

# create empty geodataframe and geometry column
newdata = gpd.GeoDataFrame()
newdata['geometry'] = None

# add coordinates and create polygon from coordinate-tuple list
coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coordinates)
                
# insert polygom data into geodataFrame using .loc
newdata.loc[0, 'geometry'] = poly

# add description
newdata.loc[0, 'location'] = 'Senaatintori'

# specify projection for newdata
newdata.crs = from_epsg(4326)

# export the data
outfp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_2'

# write data into new shapefie
newdata.to_file(outfp)

# HOW TO SAVE MULTIPLE SHAPEFILES

# Use .groupby() to group column BINOMIAL
grouped = data.groupby('BINOMIAL')

# output folder for multiple shapefiles
groupfp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_2/fishFolder'

# import os to parse
import os

# iterate over the dataframe (key = fish name) rows = all rows with that fish name
for key, rows in grouped:
    # create output with {0} (start at first index) and replace blank space with underscore
    output_name = "{0}.shp".format(key.replace(' ', '_'))
    # create a new folder in the groupfp file path
    output_path = os.path.join(groupfp, output_name)
    rows.to_file(output_path)
    
    


    



 
