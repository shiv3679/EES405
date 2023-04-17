from matplotlib.colors import TwoSlopeNorm
import netCDF4
import numpy as np 
from scipy import stats
import xarray as xr
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs
import cartopy.feature as cfeature


nc = netCDF4.Dataset('/home/shiv/Documents/GitHub/EES405/assignment_4/datasets/tx10p.india.nc')


# extract the dataset for tx10pETCCDI

tx10p = nc.variables['tx10pETCCDI'][:] 

# dimensions of the data
time_dim,lat_dim,lon_dim = tx10p.shape

# arrays to store the trend and p-values
trend = np.zeros((lat_dim,lon_dim))
p_values = np.zeros((lat_dim,lon_dim))

# loop over each grid point 

for lat_idx in range(lat_dim):
    for lon_idx in range(lon_dim):
        
        # calculate data at each grid point
        data = tx10p[:,lat_idx,lon_idx]
        
        # fit a linear regression model to the data
        slope,intercept,r_value,p_value,std_error = stats.linregress(np.arange(time_dim),data)
        
        # append the slope (trend) and p-values in the arrays
        trend[lat_idx,lon_idx] = slope
        p_values[lat_idx,lon_idx] = p_value
        
# visualising the trend using a heatmap or contour 


lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]


# Normalize the colorbar
max_abs_value = np.max(np.abs(trend))
norm = TwoSlopeNorm(vmin=-max_abs_value, vcenter=0, vmax=max_abs_value)




fig = plt.figure(figsize=(32, 32))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0.0, globe=None))



mp = ax.imshow(trend, extent=(lon.min(), lon.max(), lat.min(), lat.max()), cmap='coolwarm', origin='lower', norm=norm)

plt.title('Spatial trend data for tx10p historical', fontsize=20)

states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')
ax.add_feature(cfeature.BORDERS,edgecolor='black')
ax.add_feature(states_provinces, edgecolor='black')

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)


cbar = fig.colorbar(mp, shrink=0.3,label='Frequency')
cbar.minorticks_on()

#adding the long lat grids and enabling the tick labels
gl = ax.gridlines(draw_labels=True,alpha=0.1)
gl.top_labels = False
gl.right_labels = False

# plt.savefig('historical-spatial-climatology.png', dpi=1200, bbox_inches='tight')
plt.show()
