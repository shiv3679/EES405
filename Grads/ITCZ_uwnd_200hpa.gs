'reinit'
'sdfopen /home/shiv/Documents/GitHub/EES405/datasets/uwnd.annual.timmean.nc'
'set lev 200'
'set gxout shaded'
'd uwnd'
'run cbar'
'set gxout vector'
'd skip(uwnd,5,5);uwnd'
'draw title ITCZ ANNUAL uwind at 200hPa'
'printim itcz.uwnd.200hpa.png'