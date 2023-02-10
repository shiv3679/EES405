# importing the required libraries

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy as cp
import cartopy.feature as cfeature
import cartopy.crs as ccrs

# loading the cru datasets 

t_min_mam = xr.open_dataset('/home/shiv/Documents/GitHub/EES405/lab_session_02/cru_tmn.1981.2020_MAM.nc')
t_max_mam = xr.open_dataset('/home/shiv/Documents/GitHub/EES405/lab_session_02/cru_tmx.1981.2020_MAM.nc')
# t_max_dataset

t_min_mam = t_min_mam.tmn
t_max_mam = t_max_mam.tmx

lon = t_min_mam.lon
lat = t_min_mam.lat


t_min_mam_mean = t_min_mam.mean(dim='time')
t_max_mam_mean = t_max_mam.mean(dim='time')

# difference between t_min_mam and t_max_mam to get the diurnal temperature range for mam months

t_dtr_mam = t_max_mam_mean - t_min_mam_mean



fig = plt.figure(figsize=(32,32))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree(central_longitude=0.0, globe=None))

mp = ax.imshow(t_dtr_mam,extent=(lon.min(),lon.max(),lat.min(),lat.max()),cmap='jet',origin='lower')
plt.title('Diurnal temperature range for MAM months (degC)')
# plt.legend(['Temp'])

states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')
# ax.add_feature(cfeature.BORDERS,edgecolor='blue')
# ax.add_feature(states_provinces, edgecolor='blue')

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)


cbar = fig.colorbar(mp, shrink=0.3,label='Temperature (degC)')
cbar.minorticks_on()

#adding the long lat grids and enabling the tick labels
gl = ax.gridlines(draw_labels=True,alpha=0.1)
gl.top_labels = False
gl.right_labels = False

plt.savefig("/home/shiv/Documents/GitHub/EES405/plots/assignment_1/Diurnal temperature range 1981-2020 for MAM months",dpi=600)
