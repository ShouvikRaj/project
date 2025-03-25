import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

data = Dataset(r'C:\Users\shouv\Downloads\project\ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc')
lat = data.variables['lat'][:]
pres = data.variables['plev'][:22]
time = data.variables['time'][:]
ta = data.variables['ta'][:, :22, :]


mean_temp = np.mean(ta, axis=0)
x, y = np.meshgrid(lat, np.log10(pres))

# Modify figure size and DPI for 1080p resolution (1920x1080)
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)  # 16:9 aspect ratio

# Use pcolormesh with improved quality
im = ax.pcolormesh(x, y, mean_temp, 
                   cmap='jet',
                   shading='gouraud')  # Gouraud shading for smooth color transitions

contour_levels = np.linspace(np.min(mean_temp), np.max(mean_temp), 24)
cs = ax.contour(x, y, mean_temp, levels=contour_levels, 
                colors='black', alpha=0.5, linewidths=0.5)
ax.clabel(cs, inline=True, fontsize=10, fmt='%1.0f')  # Increased font size

# Add colorbar with adjusted size
cbar = fig.colorbar(im, ax=ax, location='right', label='Temperature (K)')


log_ticks = np.log10(pres)
ax.set_yticks(log_ticks)
ax.set_yticklabels([f'{round(p, 1)}' for p in np.log10(pres)], fontsize=7)

# Adjust font sizes for better readability at 1080p
ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
ax.set_xticklabels(['90°S', '60°S', '30°S', '0°', '30°N', '60°N', '90°N'], fontsize=7)
ax.set_xlabel("Latitude (°S/°N)", fontsize=10)
ax.set_ylabel("Pressure (log₁₀Pa)", fontsize=10)
ax.set_title("Average Temperature Distribution (January 1958 to December 2019)", fontsize=14)

# Flip y-axis with log values
ax.set_ylim(np.log10(pres.max()), np.log10(pres.min()))

# Save the plot as a high-quality PNG image
plt.savefig('temperature_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
