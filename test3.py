from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

# Open the netCDF file
f = Dataset('ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc', 'r')
pres = f.variables['plev'][:22]

print(pres)