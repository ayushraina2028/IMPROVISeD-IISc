#!/bin/bash

# Exit on error
set -e

# Base directory for the C++ files
BASE_DIR=$(pwd)

# C++ source files to compile
cpp_sources=( 
    "$BASE_DIR/Registration/CodeFiles/one.cpp"  
    "$BASE_DIR/Registration/CodeFiles/read.cpp" 
    "$BASE_DIR/Registration/CodeFiles/final.cpp" 
    "$BASE_DIR/Registration/CodeFiles/transpose.cpp" 
)

# Corresponding binaries
cpp_binaries=( 
    "$BASE_DIR/Registration/CodeFiles/one"  
    "$BASE_DIR/Registration/CodeFiles/read" 
    "$BASE_DIR/Registration/CodeFiles/final" 
    "$BASE_DIR/Registration/CodeFiles/transpose" 
)

# Compile C++ files with -O3 optimization
for i in "${!cpp_sources[@]}"; do
    if [ ! -f "${cpp_binaries[$i]}" ]; then
        echo "Compiling ${cpp_sources[$i]} with -O3..."
        g++ "${cpp_sources[$i]}" -o "${cpp_binaries[$i]}" -O3
        echo "Compiled ${cpp_sources[$i]} successfully."
    else
        echo "Binary ${cpp_binaries[$i]} already exists. Skipping compilation."
    fi
done

echo "All C++ files compiled successfully."
echo "------------------------------------"
echo "You are ready to GO!, checkout README.md for further instructions."
