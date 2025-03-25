from netCDF4 import Dataset, num2date
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load data
data = Dataset('ua_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][:]
pres = data.variables['plev'][:22]
time = data.variables['time'][:]
ua = data.variables['ua'][:, :22, :]

# Get dates for titles
time_units = data.variables['time'].units
time_calendar = data.variables['time'].calendar
dates = num2date(time[:], units=time_units, calendar=time_calendar)

# Create meshgrid
x, y = np.meshgrid(lat, np.log10(pres))

# Create figure
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# Initial plot
data_to_plot = np.squeeze(ua[0,:,:])
im = ax.pcolormesh(x, y, data_to_plot, 
                   cmap='rainbow',
                   shading='gouraud')

contour_levels = np.linspace(np.min(ua), np.max(ua), 24)
cs = ax.contour(x, y, data_to_plot, levels=contour_levels, 
                colors='black', alpha=0.5, linewidths=0.5)
ax.clabel(cs, inline=True, fontsize=10, fmt='%1.0f')

# Add colorbar
cbar = fig.colorbar(im, ax=ax, location='right', label='Wind Speed (m/s)')

# Set up axes
ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
ax.set_xticklabels(['90°S', '60°S', '30°S', '0°', '30°N', '60°N', '90°N'], fontsize=7)
ax.set_xlabel("Latitude (°S/°N)", fontsize=12)
ax.set_ylabel("Pressure (log₁₀Pa)", fontsize=12)

# Set up y-axis
log_ticks = np.log10(pres)
ax.set_yticks(log_ticks)
ax.set_yticklabels([f'{round(p, 1)}' for p in np.log10(pres)], fontsize=7)
ax.set_ylim(np.log10(pres.max()), np.log10(pres.min()))

def update(frame):
    # Clear previous contours
    for coll in ax.collections[1:]:
        coll.remove()
    
    # Update data
    data_to_plot = np.squeeze(ua[frame,:,:])
    im.set_array(data_to_plot.ravel())
    
    # Update contours
    cs = ax.contour(x, y, data_to_plot, levels=contour_levels, 
                    colors='black', alpha=0.5, linewidths=0.5)
    ax.clabel(cs, inline=True, fontsize=10, fmt='%1.0f')
    
    # Update title
    ax.set_title(f"Eastward Wind Speed Distribution - {dates[frame].strftime('%Y-%m-%d')}", 
                 fontsize=14)
    
    return [im] + cs.collections

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(time),
                            interval=100, blit=True)

# Save animation
ani.save('wind_speed_animation.mp4', writer='ffmpeg', fps=10)
plt.show()