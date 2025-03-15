import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from netCDF4 import Dataset, num2date

data = Dataset(r'C:\Users\shouv\Downloads\project\ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][:]
pres = data.variables['plev'][:]
time = data.variables['time'][:]
ta = data.variables['ta'][:]

time_units = data.variables['time'].units
time_calendar = data.variables['time'].calendar
dates = num2date(time[:], units=time_units, calendar=time_calendar)

x, y = np.meshgrid(lat, np.log10(pres)) 

# Adjust figure size and add padding
fig, ax = plt.subplots(figsize=(12, 9))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

data_to_plot = np.flipud(np.squeeze(ta[0,:,:]))
cax = ax.imshow(data_to_plot, extent=[x.min(), x.max(), y.min(), y.max()],
                aspect='auto', cmap='jet', origin='upper',
                interpolation='bilinear')
cbar = fig.colorbar(cax, ax=ax, location='right', label='Temperature')

def update(frame):
    data_to_plot = np.flipud(np.squeeze(ta[frame,:,:]))
    cax.set_data(data_to_plot)
    ax.set_title(f"Temperature for {dates[frame].strftime('%Y-%m-%d')}")
    return cax, ax.title


ani = animation.FuncAnimation(fig, update, frames=len(time), interval=50, blit=False)

# Move tight_layout() after all plot elements are added
plt.title("Temperature (K)")
plt.xlabel("Latitude (°N)")
plt.ylabel("Pressure (hPa)")
plt.tight_layout()

# Save with higher resolution and bitrate
ani.save('temperature_animation_logarithmic_faster.mp4', 
         writer='ffmpeg',
         #dpi=100,  # Reduced DPI for reasonable file size
         #fps=10
         )
plt.show()
