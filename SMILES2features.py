#!/usr/bin/env python

import sys

import numpy as np


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
        
    X = [None for i in range(0, len(BRD_lst))]
    
    for BRD in BRD_lst:
        SMILES = SMILES_dict[BRD]
        
        print SMILES



if __name__ == '__main__':
    main()

