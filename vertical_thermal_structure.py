# importing the required libraries

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy as cp
import cartopy.feature as cfeature
import cartopy.crs as ccrs

# Opening the file with xarray

data = xr.open_dataset('air.mon.ltm.nc')

# Interested only in 'air' variable

data = data.air

# taking mean of lat,lon and time 
data = data.mean(dim=['lat','lon','time'])

# getting pressure level
pressure_levels = data.level

#plotting the data

plt.plot(data,pressure_levels,'r.-')
plt.ylim(max(pressure_levels),min(pressure_levels))
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (hPa)')
plt.title('Annual Vertical thermal structure of globe')
plt.show()
