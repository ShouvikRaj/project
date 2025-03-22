from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

data = Dataset('ua_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][:]
pres = data.variables['plev'][:]
time = data.variables['time'][:]
ua = data.variables['ua'][:]
#print(data)

mean_air_speed = np.mean(ua, axis=0)
x, y = np.meshgrid(lat, np.log10(pres))

# Modify figure size and DPI for 1080p resolution (1920x1080)
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)  # 16:9 aspect ratio
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# Use pcolormesh with improved quality
im = ax.pcolormesh(x, y, np.flipud(mean_air_speed), 
                   cmap='rainbow',
                   shading='gouraud')  

contour_levels = np.linspace(np.min(mean_air_speed), np.max(mean_air_speed), 24)
cs = ax.contour(x, y, np.flipud(mean_air_speed), levels=contour_levels, 
                colors='black', alpha=0.5, linewidths=0.5)
ax.clabel(cs, inline=True, fontsize=10, fmt='%1.0f')  # Increased font size

# Add colorbar with adjusted size
cbar = fig.colorbar(im, ax=ax, location='right', label='Wind Speed (m/s)')

# Adjust font sizes for better readability at 1080p
ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
ax.set_xticklabels(['90°S', '60°S', '30°S', '0°', '30°N', '60°N', '90°N'], fontsize=10)
ax.set_xlabel("Latitude (°N/°S)", fontsize=12)
ax.set_ylabel("Pressure (Log₁₀Pa)", fontsize=12)
ax.set_title("Average Eastward Wind Speed Distribution (1958-01-16 to 2019-03-16)", fontsize=14)

# Save with high resolution
plt.savefig('Wind_speed_distribution_1080p.png', dpi=120, bbox_inches='tight')
plt.show()
