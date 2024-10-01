import pandas as pd   
import sys

offset = sys.argv[1]

df = pd.read_csv("../DistanceBounds/solution.csv")
maps = pd.read_csv("../DistanceBounds/mapping.csv")

# Create index column
maps["index"] = -1


def get_ca_atom_numbers(pdb_file):
    """Extract CA atom numbers and their corresponding residue indices from a PDB file."""
    ca_atom_numbers = {}
    
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith("ATOM") and line[12:16].strip() == "CA":  # Ensure it's a CA atom
                residue_index = int(line[22:26].strip())
                atom_number = int(line[6:11].strip())
                ca_atom_numbers[residue_index] = atom_number
    
    return ca_atom_numbers

# Step 1: Read the mappings from the CSV file
mapping_csv_path = '../DistanceBounds/mapping.csv'  # Update this path as needed
mappings_df = pd.read_csv(mapping_csv_path)

# Step 2: Get CA atom numbers from PDB files
ca_atoms_chain_A = get_ca_atom_numbers('../Input/chain_A.pdb')
ca_atoms_chain_B = get_ca_atom_numbers('../Input/chain_B.pdb')

# Step 3: Replace the indices in the DataFrame
def replace_indices(row):
    if row['Chain'] == 'chain_A':
        return ca_atoms_chain_A.get(row['Old Index'], 'NA')  # Use 'NA' if not found
    elif row['Chain'] == 'chain_B':
        return ca_atoms_chain_B.get(row['Old Index'], 'NA')  + int(offset) # Use 'NA' if not found
    return row['Old Index']  # Fallback

# Create a new column with replaced indices
mappings_df['CA Atom Number'] = mappings_df.apply(replace_indices, axis=1)

# Step 4: Save the updated DataFrame to a new CSV file
output_csv_path = 'updated_mappings.csv'  # Update this path as needed
mappings_df.to_csv(output_csv_path, index=False)

print("Mapping indices replaced with CA atom numbers and saved to", output_csv_path)

# Save last column to a txt file
mappings_df['CA Atom Number'].to_csv('ca_atom_numbers.txt', index=False, header=False)

print(mappings_df)

# move the ca_atom_numbers.txt, updated_mappings.csv to ../DistanceBounds/
import shutil
shutil.move('ca_atom_numbers.txt', '../DistanceBounds/ca_atom_numbers.txt')
shutil.move('updated_mappings.csv', '../DistanceBounds/updated_mappings.csv')