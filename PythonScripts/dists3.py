# Load the necessary modules
from pymol import cmd
import csv

def visualize_ca_distances_from_csv(csv_file, output_file):
    # Load the PDB files
    cmd.load("../Flipping/flip1.chkref.pdb", "chain_A")
    cmd.load("../Flipping/flip2.chkref.pdb", "chain_B")

    # Open and read the input CSV file
    with open(csv_file, 'r') as f:
        lines = f.readlines()

    # Prepare to save distances in the output CSV file
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        # Write the header
        writer.writerow(['resi1', 'prot1', 'resi2', 'prot2', 'dist'])

        # Skip the header line
        for line in lines[1:]:
            res1, prot1, res2, prot2 = line.strip().split(',')
            
            # Create selection names for C-alpha atoms
            res1_sel = f"{prot1} and resi {res1} and name CA"
            res2_sel = f"{prot2} and resi {res2} and name CA"
            
            # Calculate and visualize distances
            distance_name = f"dist_{res1}_{res2}"
            cmd.distance(distance_name, res1_sel, res2_sel)

            # Get the distance value
            distance = cmd.get_distance(res1_sel, res2_sel)
            
            # Write the data to the CSV
            writer.writerow([res1, prot1, res2, prot2, distance])
            
            # Show sticks for the selected C-alpha atoms
            cmd.show("sticks", res1_sel)
            cmd.show("sticks", res2_sel)
            
            # Optionally, color the selections
            cmd.color("red", res1_sel)
            cmd.color("blue", res2_sel)

    # Zoom into all selections
    cmd.zoom("all")

# Execute the function with the specified CSV file and output file
visualize_ca_distances_from_csv("../Input/crosslinks_original.csv", "../DistanceBounds/crosslinks_satisfy_flip.csv")
