'reinit'
'sdfopen /home/shiv/Documents/GitHub/EES405/datasets/prate.1980.2020.jjas.timmean.nc'
'set gxout shaded'
'a = prate*86400'
'd a'
'run cbar'
'sdfopen /home/shiv/Documents/GitHub/EES405/datasets/uwnd.1980.2020.jjas.nc'
'set dfile 2'
'set lev 1000'
'sdfopen /home/shiv/Documents/GitHub/EES405/datasets/vwnd.1980.2020.jjas.nc'
'set dfile 3'
'set lev 1000' 
'd skip(uwnd.2,3,3);vwnd'
'draw title ITCZ JJAS with prate and (u,v)'
'printim /home/shiv/Documents/GitHub/EES405/datasets/itcz.jjas.prate.uv.png'
