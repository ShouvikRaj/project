import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.animation as animation

# Load the dataset
netcdf_file1 = 'ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc'
xrds1 = xr.open_dataset(netcdf_file1)

# Extract the temperature variable
ta = xrds1['ta']  # Shape: (time, plev, lat)
times = xrds1['time'].values  # Extract time coordinates

# Select a pressure level (Modify as needed)
plev_index = 0  # Use the first pressure level, adjust as necessary
ta_selected = ta.isel(plev=plev_index)  # Shape: (time, lat)

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 6))
cbar = None  # Placeholder for colorbar

# Create the initial frame
im = ax.imshow(ta_selected.isel(time=0), cmap='coolwarm', aspect='auto')

# Add colorbar
cbar = fig.colorbar(im, ax=ax)

def update(frame):
    global im
    im.set_array(ta_selected.isel(time=frame).values)  # Update image data
    ax.set_title(f"Temperature at {str(times[frame])}")

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(times), interval=200)

# Save as GIF or MP4 (optional)
# ani.save('temperature_animation.gif', writer='pillow', fps=5)

plt.show()
