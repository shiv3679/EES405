# Open the file for writing
with open('donkey.txt', 'w') as f:
    # Loop over the years from 1940 to 2022
    for year in range(1940, 2023):
        # Construct the string with the current year
        line = f'cdo -eca_r20mm era5_{year}.nc eca_r20mm-{year}.nc\n'
        # Write the line to the file
        f.write(line)
