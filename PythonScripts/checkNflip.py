import numpy as np
from Bio.PDB import PDBParser, PDBIO
import subprocess

def getRotationMatrix_fromfiles(listoffiles):
    '''

    '''

    n = len(listoffiles)
    rot = []
    for file in listoffiles:
        rot_i = np.loadtxt(file, skiprows=1)
        rot.append(rot_i)

    return rot

def checkPDBnROT(pdb_outliers, rot, TOL=0.4):
    '''

    '''
    rot_refl = rot.copy()

    I_refl = np.identity(3)
    I_refl[0,0] = -1

    count = 0
    for outlier in pdb_outliers:
        if outlier > TOL:
            rot_refl[count] = I_refl @ rot[count]
        #else:
        #    rot_refl[count] = rot[count]
        count = count+1

    return rot_refl

def makeOneMatrix(rot_list):
    '''

    '''

    n = len(rot_list)
    rot = np.empty((3,0), dtype=float)
    count = 0
    for rot_i in rot_list:
        rot = np.concatenate((rot,rot_i),1)

    return rot

def regFlipCorrect(list_of_outliers, list_of_rot, B_file, L_inv_file, tot_atoms):
    '''

    '''

    rot_org_  = getRotationMatrix_fromfiles(list_of_rot)
    rot_new_  = checkPDBnROT(list_of_outliers, rot_org_)
    rot_new   = makeOneMatrix(rot_new_)
    B         = np.loadtxt(B_file, skiprows=1)
    L_inv     = np.loadtxt(L_inv_file, skiprows=1)

    X = rot_new @ B @ L_inv

    return X[:,0:tot_atoms]
 
def updateCoordinate(pdb, new_coords, outpdbname):
    '''

    '''
    io = PDBIO()
    p = PDBParser()
    pdbname = pdb[:-3]
    structure = p.get_structure(pdbname, pdb) # input files
    i = 0
    for model in structure:
        for chain in model:
            for residue in chain: 
                for atom in residue:
                    atom.set_coord(new_coords[:,i]) # change coordinates
                    i += 1
    io.set_structure(structure)
    io.save(outpdbname, preserve_atom_numbering = True)

#def flipIfneeded(pdb1, outlier1, rotation1, atoms1, pdb2, outlier2, rotation2, atoms2, rotation3, B_file, L_inv_file):
def flipIfneeded(pdb1, rotation1, atoms1, pdb2, rotation2, atoms2, rotation3, B_file, L_inv_file): 
    '''

    '''
    outlier1_ = subprocess.run(["../Flipping/pyrama_outliers",pdb1], capture_output=True, text=True, check=True)
    outlier2_ = subprocess.run(["../Flipping/pyrama_outliers",pdb2], capture_output=True, text=True, check=True)

    outlier1 = float(outlier1_.stdout.split(":")[-1][:-2])
    outlier2 = float(outlier2_.stdout.split(":")[-1][:-2])

    print(outlier1)
    print(outlier2)

    X = regFlipCorrect([outlier1, outlier2, 1], \
                       [rotation1, rotation2, rotation3],\
                       B_file, L_inv_file, atoms1+atoms2)


    pdb1_ = pdb1[:-3]
    pdb2_ = pdb2[:-3]
    pdb1_new = pdb1_ + "chkref.pdb"
    pdb2_new = pdb2_ + "chkref.pdb"

    print(pdb1_new)
    print(pdb2_new)

    updateCoordinate(pdb1, X[:,0:atoms1], pdb1_new)
    updateCoordinate(pdb2, X[:,atoms1:atoms1+atoms2], pdb2_new)


