from pymol import cmd

# Launch PyMOL
cmd.load("../Flipping/flip1.chkref.pdb")
cmd.load("../Flipping/flip2.chkref.pdb")

cmd.show("cartoon")
