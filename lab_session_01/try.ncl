begin
	f = addfile("air.mon.ltm.nc","r")
	air_data = f->air(0,:,:,{10})
	printVarSummary(u) ; structure of the data frame
end
