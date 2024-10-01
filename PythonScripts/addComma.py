def process_coordinates(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()

        # Skip the first line
        data_lines = lines[1:]

        # Process each line and convert to x, y, z coordinates
        for line in data_lines:
            # Split the line by spaces (handling multiple spaces)
            coordinates = line.split()

            # Join the coordinates with commas
            formatted_line = ','.join(coordinates)

            # Write the formatted line to the output file
            outfile.write(formatted_line + '\n')

# File paths
input_file = '../Registration/CodeFiles/coordinates.txt'  # Your input file
output_file = '../Output/output.csv'  # File to store the result

# Call the function
process_coordinates(input_file, output_file)

print(f"Processed data saved to {output_file}.")
