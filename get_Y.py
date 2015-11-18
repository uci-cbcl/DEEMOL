#!/usr/bin/env python

import sys

import numpy as np


def main():
    data = np.load(sys.argv[1])
    data_id = map(lambda x:x.strip('\n'), open(sys.argv[2]).readlines())
    subsample_id = map(lambda x:x.split('\t')[0], open(sys.argv[3]).readlines())
    
    data_id_dict = {}
    for i in range(0, len(data_id)):
        data_id_dict[data_id[i]] = i
    
    subsample_idx = [-1 for i in range(0, len(subsample_id))]
    
    for i in range(0, len(subsample_id)):
        id = subsample_id[i]
        subsample_idx[i] = data_id_dict[id]
    
    data_subsample = data[:, subsample_idx].transpose()
    
    np.save(sys.argv[4], data_subsample)








if __name__ == '__main__':
    main()


