import csv
import pymol
from pymol import cmd

def read_distances(csv_file):
    distances = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            resi1 = int(row['resi1'])
            prot1 = row['prot1']
            resi2 = int(row['resi2'])
            prot2 = row['prot2']
            dist = float(row['dist'])
            distances.append((resi1, prot1, resi2, prot2, dist))
    return distances

def highlight_distances(distances):
    differences = []
    for resi1, prot1, resi2, prot2, dist in distances:
        # Construct PyMOL selection strings
        selection1 = f"{prot1} and resi {resi1} and name CA"
        selection2 = f"{prot2} and resi {resi2} and name CA"
        
        # Measure the distance in PyMOL
        distance_name = f"dist_{resi1}_{resi2}"
        cmd.distance(distance_name, selection1, selection2)
        
        # Store the distance and calculate the difference from the specified distance
        reference_distance = dist  # Use the distance from the CSV file
        difference = dist - reference_distance
        differences.append((resi1, prot1, resi2, prot2, difference))
    
    return differences

def save_differences(differences, output_file):
    with open(output_file, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['resi1', 'prot1', 'resi2', 'prot2', 'difference'])
        for resi1, prot1, resi2, prot2, difference in differences:
            writer.writerow([resi1, prot1, resi2, prot2, difference])

def main(csv_file, output_file):
    distances = read_distances(csv_file)
    differences = highlight_distances(distances)
    save_differences(differences, output_file)

if __name__ == "__main__":
    csv_file_path = "../DistanceBounds/distances.csv"  # Replace with your distances.csv file path
    output_file_path = "../DistanceBounds/differences.csv"  # Output file for differences
    main(csv_file_path, output_file_path)
