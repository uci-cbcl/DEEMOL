#!/usr/bin/env python

import sys
import inspect

import numpy as np
from rdkit.Chem import RDKFingerprint, MolFromSmiles

MOL_H2O = MolFromSmiles('O')

def main():
    inSMILES = open(sys.argv[1])
    inBRD = open(sys.argv[2])
    
    SMILES_dict = {}
    
    for line in inSMILES:
        BRD, SMILES = line.strip('\n').split('\t')
        SMILES_dict[BRD] = SMILES
    
    BRD_lst = []
    
    for line in inBRD:
        BRD_lst.append(line.split('\t')[1])

        
    for BRD in BRD_lst:
        SMILES = SMILES_dict[BRD]
        mol = MolFromSmiles(SMILES)
        fp = RDKFingerprint(mol)
        
        print '\t'.join(fp.ToBitString())
    
    
    
    inSMILES.close()
    inBRD.close()


if __name__ == '__main__':
    main()
