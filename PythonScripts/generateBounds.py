from pymol import cmd
import csv
import sys

chain_A = sys.argv[1]
chain_B = sys.argv[2]
crosslink_output = sys.argv[3]
equality1_output = sys.argv[4]
equality2_output = sys.argv[5]

def calculate_distances(csv_file, output_file):
    """Calculate distances between chain_A and chain_B based on input CSV."""
    # Load the PDB files
    cmd.load(chain_A, "chain_A")
    cmd.load(chain_B, "chain_B")
    
    
    # Get and print the number of atoms in each chain
    num_atoms_chain_A = cmd.count_atoms('chain_A')
    num_atoms_chain_B = cmd.count_atoms('chain_B')

    # Write num_atoms_chain_A, num_atoms_chain_B to a file
    with open('../Input/natoms.txt', 'w') as f:
        f.write(f"{num_atoms_chain_A}\n")
        f.write(f"{num_atoms_chain_B}\n")
        
        
    # Open and read the input CSV file
    with open(csv_file, 'r') as f:
        lines = f.readlines()
        

    # Prepare to save distances in the output CSV file
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['resi1', 'prot1', 'resi2', 'prot2', 'dist'])

        for line in lines[1:]:
            res1, prot1, res2, prot2 = line.strip().split(',')
            res1_sel = f"{prot1} and resi {res1} and name CA"
            res2_sel = f"{prot2} and resi {res2} and name CA"
            distance = cmd.get_distance(res1_sel, res2_sel)
            writer.writerow([res1, prot1, res2, prot2, distance])

            # Visualize only crosslink distances with sticks and colors
            cmd.distance(f"dist_{res1}_{res2}", res1_sel, res2_sel)
            cmd.show("sticks", res1_sel)
            cmd.show("sticks", res2_sel)
            cmd.color("red", res1_sel)
            cmd.color("blue", res2_sel)
    
    # Zoom into crosslink selections only
    cmd.zoom("chain_A or chain_B")


def calculate_equality_chain_A(csv_file, equality1_file):
    """Calculate pairwise distances for residues within chain_A."""
    with open(csv_file, 'r') as f:
        lines = f.readlines()

    with open(equality1_file, 'w', newline='') as eq1_csv:
        writer = csv.writer(eq1_csv)
        writer.writerow(['prot1', 'resi1', 'prot2', 'resi2', 'dist'])

        # Extract all residues for chain_A
        chain_a_residues = sorted(set([line.split(',')[0] for line in lines[1:] if line.split(',')[1] == "chain_A"]))
        
        # Calculate pairwise distances within chain_A without visualization
        for i in range(len(chain_a_residues)):
            for j in range(i + 1, len(chain_a_residues)):
                res1, res2 = chain_a_residues[i], chain_a_residues[j]
                res1_sel = f"chain_A and resi {res1} and name CA"
                res2_sel = f"chain_A and resi {res2} and name CA"
                distance = cmd.get_distance(res1_sel, res2_sel)
                writer.writerow(['chain_A', res1, 'chain_A', res2, distance])


def calculate_equality_chain_B(csv_file, equality2_file):
    """Calculate pairwise distances for residues within chain_B."""
    with open(csv_file, 'r') as f:
        lines = f.readlines()

    with open(equality2_file, 'w', newline='') as eq2_csv:
        writer = csv.writer(eq2_csv)
        writer.writerow(['prot1', 'resi1', 'prot2', 'resi2', 'dist'])

        # Extract all residues for chain_B
        chain_b_residues = sorted(set([line.split(',')[2] for line in lines[1:] if line.split(',')[3] == "chain_B\n"]))
        
        # Calculate pairwise distances within chain_B without visualization
        for i in range(len(chain_b_residues)):
            for j in range(i + 1, len(chain_b_residues)):
                res1, res2 = chain_b_residues[i], chain_b_residues[j]
                res1_sel = f"chain_B and resi {res1} and name CA"
                res2_sel = f"chain_B and resi {res2} and name CA"
                distance = cmd.get_distance(res1_sel, res2_sel)
                writer.writerow(['chain_B', res1, 'chain_B', res2, distance])


def main():
    # File names
    csv_file = "../Input/crosslinks.csv"
    output_file = crosslink_output
    equality1_file = equality1_output
    equality2_file = equality2_output

    # Run the three tasks
    calculate_distances(csv_file, output_file)
    calculate_equality_chain_A(csv_file, equality1_file)
    calculate_equality_chain_B(csv_file, equality2_file)

# Execute the main function
main()
