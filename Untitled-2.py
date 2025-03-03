from manim import *
import xarray as xr
import numpy as np

class NetCDFVisualization(Scene):
    def construct(self):
        # Open the NetCDF file
        dataset = xr.open_dataset("ta_Amon_reanalysis_JRA-55_195801-201912.2D.cg.nc")  # Replace with your actual file
        
        # Extract some data (assuming we have a 2D variable like temperature)
        var_name = list(dataset.data_vars)[0]  # Get the first variable
        data = dataset[var_name].values  # Convert to numpy array
        
        # Get dimensions
        time_steps = data.shape[0] if len(data.shape) > 2 else 1  # Adjust based on data
        
        # Create a grid of dots to represent data points
        rows, cols = data.shape[-2], data.shape[-1]  # Assume last two dimensions are spatial
        dots = VGroup(*[Dot(point=RIGHT * j + UP * i) for i in range(rows) for j in range(cols)])
        
        self.play(FadeIn(dots))  # Show initial data points

        # Animate changes in data over time
        for t in range(min(time_steps, 50)):  # Limit frames to 50 for performance
            colors = [interpolate_color(BLUE, RED, (data[t, i, j] - np.min(data)) / 
                                        (np.max(data) - np.min(data) + 1e-6)) 
                      for i in range(rows) for j in range(cols)]
            
            self.play(*[dots[i].animate.set_color(colors[i]) for i in range(len(dots))], run_time=0.3)

        self.wait(1)

