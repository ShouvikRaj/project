from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

# Load both datasets
#temp_data = Dataset('ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
wind_data = Dataset('ua_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')

print(wind_data.variables["ua"])