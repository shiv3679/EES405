# importing the required libraries

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy as cp
import cartopy.feature as cfeature
import cartopy.crs as ccrs

# taking the datasets of different regions and plotting them together to see if there are any visible differences

annual_files = ['global','tropics','poles','india']
winter_files = ['global_DJF','tropics_DJF','poles_DJF','india_DJF']
summer_files = ['global_JJAS','tropics_JJAS','poles_JJAS','india_JJAS']

annual_datasets = []
winter_datasets = []
summer_datasets = []
pressure_levels_annual = []
pressure_levels_winter = []
pressure_levels_summer = []

for i in annual_files:
    data = xr.open_dataset('/home/shiv/Documents/GitHub/EES405/lab_session_02/'+i+'.nc')
    data = data.air
    thermal = data.mean(dim=['lat','lon','time'])
    pressure_levels = data.level
    annual_datasets.append(thermal)
    pressure_levels_annual.append(pressure_levels)

for i in winter_files:
    data = xr.open_dataset('/home/shiv/Documents/GitHub/EES405/lab_session_02/'+i+'.nc')
    data = data.air
    thermal = data.mean(dim=['lat','lon','time'])
    pressure_levels = data.level
    winter_datasets.append(thermal)
    pressure_levels_winter.append(pressure_levels)

for i in summer_files:
    data = xr.open_dataset('/home/shiv/Documents/GitHub/EES405/lab_session_02/'+i+'.nc')
    data = data.air
    thermal = data.mean(dim=['lat','lon','time'])
    pressure_levels = data.level
    summer_datasets.append(thermal)
    pressure_levels_summer.append(pressure_levels)


# plotting the annual data for each region

plt.plot(annual_datasets[0],pressure_levels_annual[0],'r.-',label='Global')
plt.ylim(max(pressure_levels_annual[0]),min(pressure_levels_annual[0]))
plt.plot(annual_datasets[1],pressure_levels_annual[1],'b.-',label='Tropics')
plt.ylim(max(pressure_levels_annual[1]),min(pressure_levels_annual[1]))
plt.plot(annual_datasets[2],pressure_levels_annual[2],'g.-',label='Poles')
plt.ylim(max(pressure_levels_annual[2]),min(pressure_levels_annual[2]))
plt.plot(annual_datasets[3],pressure_levels_annual[3],'k.-',label='India')
plt.ylim(max(pressure_levels_annual[3]),min(pressure_levels_annual[3]))
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (hPa)')
plt.title('Annual Vertical thermal structure of different regions across seasons')
plt.legend()
plt.minorticks_on()
plt.grid(True)
plt.savefig('/home/shiv/Documents/GitHub/EES405/plots/assignment_1/annual_regions.png')
plt.show()


# plotting the summer data across the regions

plt.plot(summer_datasets[0],pressure_levels_summer[0],'r.-',label='Global')
plt.ylim(max(pressure_levels_summer[0]),min(pressure_levels_summer[0]))
plt.plot(summer_datasets[1],pressure_levels_summer[1],'b.-',label='Tropics')
plt.ylim(max(pressure_levels_summer[1]),min(pressure_levels_summer[1]))
plt.plot(summer_datasets[2],pressure_levels_summer[2],'g.-',label='Poles')
plt.ylim(max(pressure_levels_summer[2]),min(pressure_levels_summer[2]))
plt.plot(summer_datasets[3],pressure_levels_summer[3],'k.-',label='India')
plt.ylim(max(pressure_levels_summer[3]),min(pressure_levels_summer[3]))
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (hPa)')
plt.title('Summer Vertical thermal structure of different regions across seasons')
plt.legend()
plt.minorticks_on()
plt.grid(True)
plt.savefig('/home/shiv/Documents/GitHub/EES405/plots/assignment_1/summer_regions.png')
plt.show()


# plotting the winter data across the regions

plt.plot(winter_datasets[0],pressure_levels_winter[0],'r.-',label='Global')
plt.ylim(max(pressure_levels_winter[0]),min(pressure_levels_winter[0]))
plt.plot(winter_datasets[1],pressure_levels_winter[1],'b.-',label='Tropics')
plt.ylim(max(pressure_levels_winter[1]),min(pressure_levels_winter[1]))
plt.plot(winter_datasets[2],pressure_levels_winter[2],'g.-',label='Poles')
plt.ylim(max(pressure_levels_winter[2]),min(pressure_levels_winter[2]))
plt.plot(winter_datasets[3],pressure_levels_winter[3],'k.-',label='India')
plt.ylim(max(pressure_levels_winter[3]),min(pressure_levels_winter[3]))
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (hPa)')
plt.title('Winter Vertical thermal structure of different regions across seasons')
plt.legend()
plt.minorticks_on()
plt.grid(True)
plt.savefig('/home/shiv/Documents/GitHub/EES405/plots/assignment_1/winter_regions.png')
plt.show()

