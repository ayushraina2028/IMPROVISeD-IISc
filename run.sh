#!/bin/bash

# Exit on error
set -e

# run Localization or Not
# If set to False, then you need to add localization coordinates and global index in Registration/Groups/group3.txt and Registration/Indexes/index3.txt
runLocalization=true

# Base Directory
BASE_DIR=$(pwd)
echo "Base Directory: $BASE_DIR"

# Function to measure time and display progress
function run_command() {
    local start_time=$(date +%s)
    echo "Running: $1"
    eval $1
    local end_time=$(date +%s)
    local elapsed_time=$((end_time - start_time))
    echo "Finished: $1 in $elapsed_time seconds"
    echo "------------------------------------"
}

chain_A_original="../Input/chain_A.pdb"
chain_B_original="../Input/chain_B.pdb"
crosslink_output_original="../DistanceBounds/distances.csv"
equality1_original="../DistanceBounds/equality1.csv"
equality2_original="../DistanceBounds/equality2.csv"

chain_A_modelled="../Flipping/flip1.pdb"
chain_B_modelled="../Flipping/flip2.pdb"
crosslink_output_modelled="../DistanceBounds/distances_modelled.csv"
equality1_modelled="../DistanceBounds/equality1_modelled.csv"
equality2_modelled="../DistanceBounds/equality2_modelled.csv"

# Record the start time of the entire script
total_start_time=$(date +%s)

# Number of times to repeat the entire process
NUM_RUNS=1

> DistanceBounds/violations_results_flip.txt
> DistanceBounds/violations_results_noflip.txt

for ((i=1; i<=NUM_RUNS; i++))
do
    echo "Starting iteration $i of $NUM_RUNS"

    # Generating Distance Bounds
    cd $BASE_DIR/PythonScripts

    chain_A_atoms=$(sed -n '1p' ../Input/natoms.txt)
    chain_B_atoms=$(sed -n '2p' ../Input/natoms.txt)

    # Print the variables to confirm
    echo "Number of atoms in chain_A: $chain_A_atoms"
    echo "Number of atoms in chain_B: $chain_B_atoms"
    
    if [ "$runLocalization" = true ]; then

        # Python Script 1
        run_command "python3 generateBounds.py $chain_A_original $chain_B_original $crosslink_output_original $equality1_original $equality2_original"


        # Python Script 2
        run_command "python3 generateLocalizationBounds.py"

        # Python Script 3
        run_command "python3 solveLocalization.py"

        # Python Script 4
        run_command "python3 generateGlobalIndex.py $chain_A_atoms"

        # Python Script 5
        run_command "python3 makeIndexGroup.py"

        # Python Script 6
        run_command "python3 removeComma.py"
    fi

    # Move Localization result to required folder
    run_command "cp ../Registration/Groups/group3.txt ../ExtraPDB/group3_${i}.txt"
    run_command "cp ../Registration/Indexes/index3.txt ../ExtraPDB/index3_${i}.txt"

    # C++ Code 1
    cd "../Registration/CodeFiles"
    run_command "./one"

    # C++ Code 2
    run_command "./register"

    # C++ Code 3
    run_command "./read"

    # C++ Code 4
    run_command "./final"

    # C++ Code 5
    run_command "./transpose"


    # Python Script 7
    cd "../../PythonScripts"
    run_command "python3 addComma.py"

    # Move generated files
    cd "../Registration/CodeFiles"
    mv "B_eigen.txt" "../../Flipping"
    mv "L_pseudo.txt" "../../Flipping"
    mv "rotation1.txt" "../../Flipping"
    mv "rotation2.txt" "../../Flipping"
    mv "rotation3.txt" "../../Flipping"

    # Python Script 8
    cd "../../PythonScripts"
    run_command "python3 savePDB.py $i"

    # Python Script 9
    run_command "python3 generateBounds.py $chain_A_modelled $chain_B_modelled $crosslink_output_modelled $equality1_modelled $equality2_modelled"

    # Check for flips
    run_command "python3 checkNflip2.py $chain_A_atoms $chain_B_atoms"


    #python script 11
    run_command "python3 dists.py"
    run_command "python3 dists2.py"
    run_command "python3 dists3.py"
    
    # Move required files
    run_command "mv ../Flipping/flip1.chkref.pdb ../ExtraPDB/chain_A_flipped_${i}.pdb"
    run_command "mv ../Flipping/flip2.chkref.pdb ../ExtraPDB/chain_B_flipped_${i}.pdb"
    run_command "mv ../Flipping/flip1.pdb ../ExtraPDB/chain_A_${i}.pdb"
    run_command "mv ../Flipping/flip2.pdb ../ExtraPDB/chain_B_${i}.pdb"

    # Python Script 12
    run_command "python3 error.py $i"

    # Move generated PDB file with unique name
    run_command "mv ../Output/output.csv ../ExtraPDB/output_${i}.csv"

    cd $BASE_DIR

    # Move violations results
    run_command "mv DistanceBounds/violations_results_flip.txt Output/violations_results_flip_${i}.txt"
    run_command "mv DistanceBounds/violations_results_noflip.txt Output/violations_results_noflip_${i}.txt"

    echo "Iteration $i completed successfully!"
    echo "------------------------------------"

done


# Record the end time of the entire script
total_end_time=$(date +%s)
total_elapsed_time=$((total_end_time - total_start_time))

# Summary Message
echo "All tasks completed successfully for all iterations!"
echo "Total time taken: $total_elapsed_time seconds"

