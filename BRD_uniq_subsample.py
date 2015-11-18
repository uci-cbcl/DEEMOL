#!/usr/bin/env python

import sys

import numpy as np

DOSE = 10.0

def main():
    infile = open(sys.argv[1])
    
    BRD_old = ''
    line_best = ''
    dose_best = 1e5
    
    for line in infile:
        fields = line.strip('\n').split('\t')
        BRD = fields[1]
        dose = float(fields[6])
        
        if BRD == BRD_old:
            if np.abs(dose-DOSE) < dose_best:
                dose_best = np.abs(dose-DOSE)
                line_best = line
            else:
                continue
        else:
            if line_best != '':
                print line_best.strip('\n')
            
            BRD_old = BRD
            line_best = line
            dose_best = np.abs(dose-DOSE)
    
    print line_best.strip('\n')
            







if __name__ == '__main__':
    main()

