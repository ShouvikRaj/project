import xarray as xr
import matplotlib.pyplot as plt

text_file = open('test.txt', 'w')
netcdf_file1 = 'ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc'
netcdf_file2 = 'ua_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc'
xrds1 = xr.open_dataset(netcdf_file1)
#xrds2 = xr.open_dataset(netcdf_file2)

plt.plot(xrds1.ta)
plt.show()



