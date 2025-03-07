import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


netcdf_file1 = 'ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc'
xrds1 = xr.open_dataset(netcdf_file1)


time_steps = xrds1.time.sel(time=slice('1958-01-16T12:00:00.000000000', '2019-12-16T12:00:00.000000000'))


fig, ax = plt.subplots()
cbar = None  


def update(frame):
    global cbar
    ax.clear()
    
    data_date = xrds1.sel(time=time_steps[frame])  
    im = data_date['ta'].plot(ax=ax, add_colorbar=False)  
    
    
    if cbar is None:
        cbar = fig.colorbar(im, ax=ax)
    
    ax.set_title(f"Temperature at time {str(time_steps[frame].values)[:16]}")


ani = animation.FuncAnimation(fig, update, frames=len(time_steps), interval=200)


ani.save('temperature_animation.mp4', writer='ffmpeg')  
plt.show()  
