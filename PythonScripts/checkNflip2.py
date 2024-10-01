import checkNflip as ch 
import sys

a = sys.argv[1]
b = sys.argv[2]

def doFlipping(pdb1, rotation1, n_atoms1, pdb2, rotation2, n_atoms2, rotation3, B_matrix, L_inverse):
    
    ch.flipIfneeded(pdb1, rotation1, n_atoms1, pdb2, rotation2, n_atoms2, rotation3, B_matrix, L_inverse)
    
    return

pdb1 = "../Flipping/flip1.pdb"
rotation1 = "../Flipping/rotation1.txt"
n_atoms1 = int(a)

pdb2 = "../Flipping/flip2.pdb"
rotation2 = "../Flipping/rotation2.txt"
n_atoms2 = int(b)

rotation3 = "../Flipping/rotation3.txt"
B_matrix = "../Flipping/B_eigen.txt"
L_inverse = "../Flipping/L_pseudo.txt"

doFlipping(pdb1, rotation1, n_atoms1, pdb2, rotation2, n_atoms2, rotation3, B_matrix, L_inverse)