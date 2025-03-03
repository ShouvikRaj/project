import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs 

netcdf_file1 = 'ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc'
netcdf_file2 = 'ua_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc'
xrds1 = xr.open_dataset(netcdf_file1)

date = '2019-12-16T12:00:00.000000000'
data_date = xrds1.sel(time=date)

data_date['ta'].plot()
plt.show()




