import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy as cp
import cartopy.feature as cfeature
import cartopy.crs as ccrs
from pylab import *

data = xr.open_dataset('/home/shiv/Documents/GitHub/EES405/lab_session_03/tmp.MAM.yearmean.CIR.fldmean.stddiv.nc',decode_times=False)

data = data.tmp
data = data.squeeze(dim=['lat','lon'],drop=True)


fig, ax = plt.subplots()

ax.plot(data.time,data, 'k.-')


# calc the trendline
z = np.polyfit(data.time,data, 1)
p = np.poly1d(z)
ax.plot(data.time,p(data.time),"r--")
# ax.set_xticks([1990,2009])
plt.minorticks_on
plt.grid(True)

fig.canvas.draw()
plt.xlabel("Year (1990-2010) (Arbitrary Units)")
plt.ylabel("Standardized temperature anomaly")
plt.title("Standardized temperature anomaly for 1990-2010")
plt.legend(['Datapoints','Trendline (y=0.000294x+(-10.759578))'])
plt.savefig("/home/shiv/Documents/GitHub/EES405/plots/assignment_1/Standardized temperature anomaly for 1990-2010",dpi=600)
plt.show()

# the line equation:
print ("y=%.6fx+(%.6f)"%(z[0],z[1]))