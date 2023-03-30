# Open the file for writing
with open('del.txt', 'w') as f:
    # Loop over the years from 1940 to 2022
    years = range(1940, 2023)
    filenames = [f'eca_r20mm-{year}.nc' for year in years]
    # Construct the command string
    command = f'rm -rf {" ".join(filenames)}\n'
    # Write the command to the file
    f.write(command)
