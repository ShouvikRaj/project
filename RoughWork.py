import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from netCDF4 import Dataset


data = Dataset(r'C:\Users\shouv\Downloads\project\ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][:]
pres = data.variables['plev'][:]
time = data.variables['time'][:]
ta = data.variables['ta'][:]

x, y = np.meshgrid(lat, np.log10(pres)) 
"""
data_to_plot = np.flipud(np.squeeze(ta[0,:,:]))

plt.imshow(data_to_plot, extent=[x.min(), x.max(), y.min(), y.max()],
            aspect='auto', cmap='rainbow', origin='upper')

cbar = plt.colorbar(location= 'right', label = 'Temperature')
 """

fig, ax = plt.subplots()
cax = ax.imshow(np.flipud(np.squeeze(ta[:,:,:])),
                 extent=[x.min(), x.max(), y.min(),
                          y.max()], aspect='auto', 
                          cmap='rainbow', origin='upper')
cbar = fig.colorbar(cax, ax=ax, location='right', label='Temperature')

def update(frame):
    data_to_plot = np.flipud(np.squeeze(ta[frame,:,:]))
    cax.set_data(data_to_plot)
    ax.set_title(f"Average temp - Time step {frame}")
    return cax,

ani = animation.FuncAnimation(fig, update, 
                              frames=len(time), blit=True)
ani.save('temperature_animation.mp4', writer='ffmpeg')
plt.title("Average temp")
plt.xlabel("Latitude (degrees N)")
plt.ylabel("Pressure (hPa)")
plt.show()

#print(data.variables['ta'])
