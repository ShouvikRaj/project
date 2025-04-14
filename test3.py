import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset, num2date

# Load data
data = Dataset(r'C:\Users\shouv\Downloads\project\ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][36:]
pres = data.variables['plev'][:22]
time = data.variables['time'][:]
ta = data.variables['ta'][:, :22, 36:]

# Convert time to datetime objects
time_units = data.variables['time'].units
calendar = data.variables['time'].calendar
dates = num2date(time[:], units=time_units, calendar=calendar)

# Create mask for summer months (June=6, July=7, August=8)
summer_mask = np.array([date.month in [6, 7, 8] for date in dates])
ta_summer = ta[summer_mask]

# Calculate mean temperature for summer months
mean_temp_summer = np.mean(ta_summer, axis=0)
x, y = np.meshgrid(lat, np.log10(pres))

# Modify figure size and DPI for 1080p resolution (1920x1080)
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)  # 16:9 aspect ratio

# Use pcolormesh with improved quality
im = ax.pcolormesh(x, y, mean_temp_summer, 
                   cmap='jet',
                   shading='gouraud')  # Gouraud shading for smooth color transitions

contour_levels = np.linspace(np.min(mean_temp_summer), np.max(mean_temp_summer), 24)
cs = ax.contour(x, y, mean_temp_summer, levels=contour_levels, 
                colors='black', alpha=0.5, linewidths=0.5)
ax.clabel(cs, inline=True, fontsize=10, fmt='%1.0f')  # Increased font size

# Add colorbar with adjusted size
cbar = fig.colorbar(im, ax=ax, location='right', label='Temperature (K)')


log_ticks = np.log10(pres)
ax.set_yticks(log_ticks)
ax.set_yticklabels([f'{round(p, 1)}' for p in np.log10(pres)], fontsize=7)

# Adjust font sizes for better readability at 1080p
ax.set_xticks([0, 30, 60, 90])
ax.set_xticklabels(['0°', '30°N', '60°N', '90°N'], fontsize=7)
ax.set_xlabel("Latitude (°S/°N)", fontsize=10)
ax.set_ylabel("Pressure (log₁₀Pa)", fontsize=10)
ax.set_title("Mean NH Summer Temperature Distribution (JJA 1958-2019)", fontsize=14)

# Flip y-axis with log values
ax.set_ylim(np.log10(pres.max()), np.log10(pres.min()))

# Save the plot as a high-quality PNG image
plt.savefig('summerNH_temperature_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Create mask for winter months (December=12, January=1, February=2)
winter_mask = np.array([date.month in [12, 1, 2] for date in dates])
ta_winter = ta[winter_mask]

# Calculate mean temperature for winter months
mean_temp_winter = np.mean(ta_winter, axis=0)
x, y = np.meshgrid(lat, np.log10(pres))

# Modify figure size and DPI for 1080p resolution (1920x1080)
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)  # 16:9 aspect ratio

# Use pcolormesh with improved quality
im = ax.pcolormesh(x, y, mean_temp_winter, 
                   cmap='jet',
                   shading='gouraud')

contour_levels = np.linspace(np.min(mean_temp_winter), np.max(mean_temp_winter), 24)
cs = ax.contour(x, y, mean_temp_winter, levels=contour_levels, 
                colors='black', alpha=0.5, linewidths=0.5)
ax.clabel(cs, inline=True, fontsize=10, fmt='%1.0f')

# Add colorbar with adjusted size
cbar = fig.colorbar(im, ax=ax, location='right', label='Temperature (K)')

log_ticks = np.log10(pres)
ax.set_yticks(log_ticks)
ax.set_yticklabels([f'{round(p, 1)}' for p in np.log10(pres)], fontsize=7)

# Adjust font sizes for better readability at 1080p
ax.set_xticks([0, 30, 60, 90])
ax.set_xticklabels(['0°', '30°N', '60°N', '90°N'], fontsize=7)
ax.set_xlabel("Latitude (°S/°N)", fontsize=10)
ax.set_ylabel("Pressure (log₁₀Pa)", fontsize=10)
ax.set_title("Mean NH Winter Temperature Distribution (DJF 1958-2019)", fontsize=14)

# Flip y-axis with log values
ax.set_ylim(np.log10(pres.max()), np.log10(pres.min()))

# Save the plot as a high-quality PNG image
plt.savefig('winterNH_temperature_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
