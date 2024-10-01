def extract_all_coordinates_and_indices(pdb_file, coords_output_file, index_output_file, start_index=1):
    """
    Extracts all coordinates (ATOM and HETATM) from a PDB file and writes them to a specified output file.
    Also writes the corresponding indices to another output file.
    
    Parameters:
    pdb_file (str): The path to the PDB file.
    coords_output_file (str): The path to the output text file where coordinates will be saved.
    index_output_file (str): The path to the output text file where indices will be saved.
    start_index (int): The starting index for coordinates, used if outputting indices.
    """
    coordinates = []
    indexes = []

    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                try:
                    # Extract coordinates from the line
                    x = float(line[30:38].strip())
                    y = float(line[38:46].strip())
                    z = float(line[46:54].strip())

                    # Store the coordinates and index
                    coordinates.append((x, y, z))
                    indexes.append(start_index)

                    # Increment the index
                    start_index += 1
                except ValueError:
                    # If coordinates are not available or cannot be converted to float, skip the line
                    continue

    # Write coordinates to output file
    with open(coords_output_file, 'w') as out_f:
        for coord in coordinates:
            out_f.write(f"{coord[0]} {coord[1]} {coord[2]}\n")

    # Write indices to index output file
    with open(index_output_file, 'w') as index_f:
        for index in indexes:
            index_f.write(f"{index}\n")

    # Return the next available index
    return start_index


# Example usage:
# Extract coordinates from chain_A.pdb and write them to group1.txt and index1.txt
next_index = extract_all_coordinates_and_indices('../Input/chain_A.pdb', 'group1.txt', 'index1.txt')

# Extract coordinates from chain_B.pdb and write them to group2.txt and index2.txt
extract_all_coordinates_and_indices('../Input/chain_B.pdb', 'group2.txt', 'index2.txt', start_index=next_index)

import shutil
shutil.move('group1.txt', '../Registration/Groups/group1.txt')
shutil.move('group2.txt', '../Registration/Groups/group2.txt')
shutil.move('index1.txt', '../Registration/Indexes/index1.txt')
shutil.move('index2.txt', '../Registration/Indexes/index2.txt')

# move the localization result
shutil.copy('../DistanceBounds/solution.csv', '../Registration/Groups/group3.txt')
shutil.copy('../DistanceBounds/ca_atom_numbers.txt', '../Registration/Indexes/index3.txt')