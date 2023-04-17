# Define the start and end year
start_year = 1960
end_year = 2020

# Open the text file in write mode
with open('eca_tn10p_commands.txt', 'w') as f:
    # Loop over the years and write the commands to the file
    for year in range(start_year, end_year + 1):
        command = f"cdo -sub -eca_tn10p tmin_{year}.nc tmin.1960.1990 tn10p.ref.nc eca_tn10p-{year}.nc\n"
        # cdo -sub -eca_tn10p tmin_1963.nc tmin.1960.1990.nc tn10p.ref.nc eca_tn10p-1963.nc
        f.write(command)
f.close()

with open('mergetime_commands.txt','w') as f:
    for year in range(start_year,end_year +1):
        command = f"eca_tn10p-{year}.nc "
        f.write(command)