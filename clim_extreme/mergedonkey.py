# Open the file for writing
with open('donkey-merge.txt', 'w') as f:
    # Initialize an empty string to hold the full command
    full_command = 'cdo -mergetime '
    # Loop over the years from 1940 to 2022
    for year in range(1940, 2023):
        # Construct the filename for the current year
        filename = f'eca_r20mm-{year}.nc '
        # Add the filename to the full command
        full_command += filename
    # Add the output filename to the full command
    full_command += 'eca_r20mm-year.nc\n'
    # Write the full command to the file
    f.write(full_command)
