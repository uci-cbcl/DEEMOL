#!/usr/bin/env python

import sys
import inspect

import numpy as np
from rdkit.Chem import Descriptors, MolFromSmiles

MOL_H2O = MolFromSmiles('O')

def main():
    decriptors_names = map(lambda x:x.strip('\n'), open(sys.argv[1]).readlines())
    inSMILES = open(sys.argv[2])
    inBRD = open(sys.argv[3])
    
    SMILES_dict = {}
    
    for line in inSMILES:
        BRD, SMILES = line.strip('\n').split('\t')
        SMILES_dict[BRD] = SMILES
    
    BRD_lst = []
    
    for line in inBRD:
        BRD_lst.append(line.split('\t')[1])
    
    descriptors = inspect.getmembers(Descriptors, inspect.isfunction)
    descriptors_func = []
    
    for pair in descriptors:
        name, func = pair
        
        if name in decriptors_names:
            descriptors_func.append(func)
            
        
    for BRD in BRD_lst:
        SMILES = SMILES_dict[BRD]
        mol = MolFromSmiles(SMILES)
        descriptor = []
        
        for func in descriptors_func:
            val = func(mol)
            
            if np.isinf(val) or np.isnan(val):
                val = func(MOL_H2O)
            
            descriptor.append(val)
        
        print '\t'.join(map(str, descriptor))
    
    
    
    inSMILES.close()
    inBRD.close()


if __name__ == '__main__':
    main()
