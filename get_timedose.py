#!/usr/bin/env python

import sys

import numpy as np


def main():
    inBRD = open(sys.argv[1])
    
    for line in inBRD:
        fields = line.strip('\n').split('\t')
        time = fields[4]
        dose = fields[6]
        
        if time == '6.0':
            time = -1
        elif time == '24.0':
            time = 1
        else:
            time = 1 if np.random.rand() >= 0.5 else -1
        
        dose = np.log10(float(dose))
        
        print str(time)+'\t'+str(dose)


    inBRD.close()





if __name__ == '__main__':
    main()

