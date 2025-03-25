from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

# Load both datasets
temp_data = Dataset('ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
wind_data = Dataset('ua_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')

# Extract variables
lat = temp_data.variables['lat'][:]
pres = temp_data.variables['plev'][:]
mean_temp = np.mean(temp_data.variables['ta'][:], axis=0)
mean_wind = np.mean(wind_data.variables['ua'][:], axis=0)

# Create meshgrid
x, y = np.meshgrid(lat, np.log10(pres))

# Create figure with 1080p resolution
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
plt.subplots_adjust(left=0.1, right=0.85, bottom=0.1, top=0.9)  # Adjusted right margin for two 

im = ax.pcolormesh(x, y, np.flipud(mean_temp), 
                   cmap='jet',
                   shading='gouraud', alpha=0.9)  # Adjusted alpha for better visibility
im2 = ax.pcolormesh(x, y, np.flipud(mean_wind), 
                   cmap='cool',
                   shading='gouraud', alpha=0.4)  # Adjusted alpha for better visibility
# Add contour lines for both
temp_levels = np.linspace(np.min(mean_temp), np.max(mean_temp), 15)
wind_levels = np.linspace(np.min(mean_wind), np.max(mean_wind), 15)

cs1 = ax.contour(x, y, np.flipud(mean_temp), levels=temp_levels,
                 colors='Black', alpha=0.9, linewidths=0.5)
cs2 = ax.contour(x, y, np.flipud(mean_wind), levels=wind_levels,
                 colors='Black', alpha=0.9, linewidths=0.5, linestyles='dashed')

# Add labels to both contours
ax.clabel(cs1, inline=True, fontsize=8, fmt='%1.0f')
ax.clabel(cs2, inline=True, fontsize=8, fmt='%1.0f')

plt.show()