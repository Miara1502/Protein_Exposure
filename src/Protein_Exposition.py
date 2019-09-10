# -*- coding: utf-8  -*-

"""Module with all the function that we need for Surface.solvant.py.
"""

import math
import time
import numpy as np
import scipy
import pandas as pd
from scipy.spatial import distance_matrix


import pprint

## Nice wrapper to time functions. Works as a decorator.
# Taken from https://stackoverflow.com/questions/5478351/python-time-measure-function
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap


visited = {}
for line in open('3i40.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        type = list[2]
        if type == 'CA' or type == 'SG' or type == 'CB':
            residue = list[3]
            type_of_chain = list[4]
            atom_count = int(list[5])
            position = list[6:9]
            if atom_count >= 0:
                if type_of_chain not in visited:
                    visited[type_of_chain] = 1
                    print(residue,type_of_chain,atom_count,' '.join(position))



'''with open('min.pdb') as pdbfile:
    for line in pdbfile:
        if line[:4] == 'ATOM' or line[:6] == "HETATM":
            print line
            # Split the line
            splitted_line = [line[:6], line[6:11], line[12:16], line[17:20], line[21], line[22:26], line[30:38], line[38:46], line[46:54]]
            print splitted_line
            # To format again the pdb file with the fields extracted
            print "%-6s%5s %4s %3s %s%4s    %8s%8s%8s\n"%tuple(splitted_line)'''
