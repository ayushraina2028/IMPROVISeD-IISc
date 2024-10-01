import pandas as pd
import shutil
import random
import numpy as np

# Step 1: Read the CSV files
distances_path = '../DistanceBounds/distances.csv'  # Path for distances.csv
equality1_path = '../DistanceBounds/equality1.csv'  # Path for equality1.csv
equality2_path = '../DistanceBounds/equality2.csv'  # Path for equality2.csv

# Read the distances CSV
data_distances = pd.read_csv(distances_path)

# Read the equality CSVs
data_equality1 = pd.read_csv(equality1_path)
data_equality2 = pd.read_csv(equality2_path)

# Step 2: Extract unique indices from distances
unique_indices_A = data_distances['resi1'].unique()
unique_indices_B = data_distances['resi2'].unique()

# Extract unique indices from equality1 and equality2
unique_indices_A_eq1 = data_equality1['resi1'].unique()  # Resi1 for chain_A in equality1
unique_indices_A_eq1_resi2 = data_equality1['resi2'].unique()  # Resi2 for chain_A in equality1

unique_indices_B_eq2 = data_equality2['resi1'].unique()  # Resi1 for chain_B in equality2
unique_indices_B_eq2_resi2 = data_equality2['resi2'].unique()  # Resi2 for chain_B in equality2

# Combine unique indices for chain_A and chain_B
all_unique_indices_A = set(unique_indices_A) | set(unique_indices_A_eq1) | set(unique_indices_A_eq1_resi2)
all_unique_indices_B = set(unique_indices_B) | set(unique_indices_B_eq2) | set(unique_indices_B_eq2_resi2)

# Step 3: Map indices
map_A = {old_index: new_index for new_index, old_index in enumerate(all_unique_indices_A, start=1)}
map_B = {old_index: new_index + len(all_unique_indices_A) for new_index, old_index in enumerate(all_unique_indices_B, start=1)}

# Step 4: Create constraint data for distances.csv
constraint_data_distances = []

for _, row in data_distances.iterrows():
    temp_index_A = map_A[row['resi1']]
    temp_index_B = map_B[row['resi2']]
    constraint_data_distances.append([temp_index_A, temp_index_B])

# Step 5: Randomly sample 50% of crosslinks and add Gaussian noise
num_samples = int(len(constraint_data_distances) * 1)
random_indices = random.sample(range(len(constraint_data_distances)), num_samples)

# Create a new list for sampled crosslinks with Gaussian noise
constraint_data_sampled = []

for idx in random_indices:
    temp_index_A, temp_index_B = constraint_data_distances[idx]
    # Apply Gaussian noise with mean 0 and standard deviation 2 to the distance of 35
    distance = 32 + np.random.normal(1, 1)
    constraint_data_sampled.append([temp_index_A, temp_index_B, distance])

# Step 6: Create constraint data for equality1.csv and equality2.csv
constraint_data_equality = []

# From equality1.csv
for _, row in data_equality1.iterrows():
    temp_index_A = map_A[row['resi1']]
    temp_index_B = map_A[row['resi2']]  # Both are from chain_A
    distance = row['dist']
    constraint_data_equality.append([temp_index_A, temp_index_B, distance])

# From equality2.csv
for _, row in data_equality2.iterrows():
    temp_index_A = map_B[row['resi1']]  # Both are from chain_B
    temp_index_B = map_B[row['resi2']]
    distance = row['dist']
    constraint_data_equality.append([temp_index_A, temp_index_B, distance])

# Step 7: Write distances constraints to distances_constraints.txt
with open('distances_constraints.txt', 'w') as f_dist:
    for entry in constraint_data_sampled:
        f_dist.write(f"{entry[0]} {entry[1]} {entry[2]}\n")

# Step 8: Write equality constraints to equality_constraints.txt
with open('equality_constraints.txt', 'w') as f_eq:
    for entry in constraint_data_equality:
        f_eq.write(f"{entry[0]} {entry[1]} {entry[2]}\n")

# Save mapping in a csv file with chain_A and chain_B
mapping_data = []
for old_index, new_index in map_A.items():
    mapping_data.append(['chain_A', old_index, new_index])
    
for old_index, new_index in map_B.items():
    mapping_data.append(['chain_B', old_index, new_index])
    
mapping_df = pd.DataFrame(mapping_data, columns=['Chain', 'Old Index', 'New Index'])
mapping_df.to_csv('mapping.csv', index=False)

#Append equality_constraints.txt to distances_constraints.txt
with open('equality_constraints.txt', 'r') as f_eq:
    with open('distances_constraints.txt', 'a') as f_dist:
        f_dist.write(f_eq.read())

# Move the generated files to the Output folder
shutil.move('distances_constraints.txt', '../DistanceBounds/distances_constraints.txt')
shutil.move('equality_constraints.txt', '../DistanceBounds/equality_constraints.txt')
shutil.move('mapping.csv', '../DistanceBounds/mapping.csv')
