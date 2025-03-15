import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

data = Dataset(r'C:\Users\shouv\Downloads\project\ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][:]
pres = data.variables['plev'][:]
time = data.variables['time'][:]
ta = data.variables['ta'][:]


# Calculate the mean temperature across all time steps
mean_temp = np.mean(ta, axis=0)
x, y = np.meshgrid(lat, np.log10(pres))

fig, ax = plt.subplots(figsize=(12, 12))

# Create proper coordinate arrays for pcolormesh
# We need to specify the cell edges rather than centers for pcolormes

# Use pcolormesh with vertex coordinates
im = ax.pcolormesh(x, y, np.flipud(mean_temp), 
                   cmap='coolwarm',
                   shading='gouraud')  # Using cell vertices for gouraud shading

# Add contour lines with correct orientation
contour_levels = np.linspace(np.min(mean_temp), np.max(mean_temp), 24)
cs = ax.contour(x, y, np.flipud(mean_temp), levels=contour_levels, 
                colors='black', alpha=0.5, linewidths=0.5)
ax.clabel(cs, inline=True, fontsize=8, fmt='%1.0f')

# Add colorbar
cbar = fig.colorbar(im, ax=ax, location='right', label='Temperature (K)')


# Customize axes
ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
ax.set_xticklabels(['90°S', '60°S', '30°S', '0°', '30°N', '60°N', '90°N'])
ax.set_xlabel("Latitude (°N/°S)")
ax.set_ylabel("Pressure (Log₁₀Pa)")
ax.set_title("Average Temperature Distribution (1958-01-16 to 2019-03-16)")

plt.show()