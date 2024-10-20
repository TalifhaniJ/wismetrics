# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:21:55 2024

@author: Talifhani Khomola
"""

import folium
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import re
import scipy
from scipy import signal
from scipy import interpolate
from datetime import datetime
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
Projects = pd.read_csv('Active Projects.csv')
map_center = [Projects['Y'].mean(), Projects['X'].mean()]
m = folium.Map(location=map_center, zoom_start=6, crs='EPSG3857')
def add_marker(row):
    folium.Marker(
        location=[row['Y'], row['X']],
                  popup=folium.Popup(f"Name:{row['Active Projects']}<br>Contribution: {row['Contribution']}", max_width=300),
                  tooltip=row['Active Projects'], label=['Active Projects']
    ).add_to(m)
Projects.apply(add_marker, axis=1)    
m.save('projects.html')