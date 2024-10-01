from pymol import cmd
import sys 

num = sys.argv[1]

# Launch PyMOL
cmd.load("../Input/chain_A.pdb")
cmd.load("../Input/chain_B.pdb")

cmd.show("cartoon")

# Run the script
cmd.run("showCoords.py")

# run a command
cmd.do("showRegPDBs('chain_A,chain_B','../Output/output.csv', '../Registration/Indexes/index1.txt,../Registration/Indexes/index2.txt')")

cmd.save("../Flipping/flip1.pdb", "chain_A")
cmd.save("../Flipping/flip2.pdb", "chain_B")

cmd.save(f"../Output/Output{num}.pdb")