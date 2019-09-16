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


for line in open('3i40.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        atom_central = list[2]
        residu = list[3]
        x = float(list[5])
        y = float(list[6])
        z = float(list[7])
        print(residu ,atom_central , x , y , z)
