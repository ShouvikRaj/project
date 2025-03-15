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

# Create figure and initial plot
fig, ax = plt.subplots(figsize=(12, 9))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# Set up the axis labels and ticks
ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
ax.set_xticklabels(['90°S', '60°S', '30°S', '0°', '30°N', '60°N', '90°N'])
ax.set_xlabel("Latitude (°N/°S)")
ax.set_ylabel("Pressure (Log₁₀Pa)")

# Initialize list to store frames
frames = []

# Create frames using a for loop
for frame in range(len(time)):
    data_to_plot = np.flipud(np.squeeze(ta[frame,:,:]))
    
    # Clear previous plot
    ax.clear()
    
    # Recreate the plot for each frame
    cax = ax.imshow(data_to_plot, 
                    extent=[lat.min(), lat.max(), np.log10(pres).min(), np.log10(pres).max()],
                    aspect='auto', 
                    cmap='jet', 
                    origin='upper',
                    interpolation='bilinear')
    
    # Reset the ticks and labels for each frame
    ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
    ax.set_xticklabels(['90°S', '60°S', '30°S', '0°', '30°N', '60°N', '90°N'])
    ax.set_xlabel("Latitude (°N/°S)")
    ax.set_ylabel("Pressure (Log₁₀Pa)")
    ax.set_title(f"Temperature for {dates[frame].strftime('%Y-%m-%d')}")
    
    # Add colorbar (only for the first frame)
    if frame == 0:
        cbar = fig.colorbar(cax, ax=ax, location='right', label='Temperature (K)')
    
    # Save the frame
    plt.savefig(f'frame_{frame:04d}.png')
    frames.append(f'frame_{frame:04d}.png')

# Use ffmpeg to combine frames into video
import os
os.system('ffmpeg -framerate 10 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p temperature_animation.mp4')

# Clean up frame files
for frame in frames:
    os.remove(frame)

plt.show()






