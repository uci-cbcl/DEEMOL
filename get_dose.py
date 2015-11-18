#!/usr/bin/env python

import sys

import numpy as np


def main():
    inBRD = open(sys.argv[1])
    
    for line in inBRD:
        fields = line.strip('\n').split('\t')
        dose = np.log10(float(fields[6]))
        
        print dose


    inBRD.close()





if __name__ == '__main__':
    main()

