import pandas as pd
import sys

# Get the iteration number from the command line argument
iteration = int(sys.argv[1])

# Load the original crosslink distances
crosslink_output_original = pd.read_csv("../DistanceBounds/crosslinks_satisfy.csv")

# Paths to the flipped and no-flipped crosslink distance files
crosslink_files = {
    "flip": "../DistanceBounds/crosslinks_satisfy_flip.csv",
    "noflip": "../DistanceBounds/crosslinks_satisfy_noflip.csv"
}

for key, file_path in crosslink_files.items():
    # Prepare the output file path for each structure
    output_file_path = f"../DistanceBounds/violations_results_{key}.txt"

    # Load the modelled crosslink distances
    crosslink_output_modelled = pd.read_csv(file_path)

    # Merging on the relevant columns to align true and modelled distances
    merged = crosslink_output_original.merge(
        crosslink_output_modelled,
        on=['resi1', 'prot1', 'resi2', 'prot2'],
        suffixes=('_original', '_modelled')
    )

    # Initialize lists to collect satisfied and violated crosslinks data
    satisfied_crosslinks = []
    violated_crosslinks = []

    # Iterate through each row and check the distance
    for _, row in merged.iterrows():
        modelled_distance = row['dist_modelled']
        original_distance = row['dist_original']
        resi1 = row['resi1']
        resi2 = row['resi2']
        prot1 = row['prot1']
        prot2 = row['prot2']

        if modelled_distance < 35:
            difference = abs(modelled_distance - original_distance)
            satisfied_crosslinks.append(
                f"Crosslink satisfied between residue {resi1} (protein {prot1}) and residue {resi2} (protein {prot2}): "
                f"Modelled distance = {modelled_distance}, Off from true value = {difference}\n"
            )
        else:
            violation_amount = modelled_distance - 35
            violated_crosslinks.append(
                f"Crosslink violated between residue {resi1} (protein {prot1}) and residue {resi2} (protein {prot2}): "
                f"Modelled distance = {modelled_distance}, Amount off from 35 = {violation_amount}\n"
            )

    # Prepare the iteration results
    iteration_results = [
        f"Iteration {iteration}:\n",
        "Satisfied Crosslinks:\n",
        *satisfied_crosslinks,
        "\nViolated Crosslinks:\n",
        *violated_crosslinks,
        "\n"
    ]

    # Write the results to the text file in append mode
    with open(output_file_path, 'a') as file:
        file.writelines(iteration_results)

    print(f"Results for iteration {iteration} appended to {output_file_path}")
