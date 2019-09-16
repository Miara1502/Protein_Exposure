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

    """Nice wrapper to time functions. Works as a decorator.
    Taken from https://stackoverflow.com/questions/5478351/python-time-measure-function
    """

    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap



def exctraction_coord(position_file):
    file = open(position_file)
    #position_file.seek(0)

    atom_dico = {"atom_central" : [] , "residu" : [] , "coord_X" : [] ,
                 "coord_Y" : [] , "coord_Z" : []}
    list_atom = []
    list_residu = []
    X = []
    Y = []
    Z = []
    for line in file:
        list = line.split()
        id = list[0]
        if id == 'ATOM':
            list_atom.append(list[2])
            list_residu.append(list[3])
            X.append(float(list[6]))
            Y.append(float(list[7]))
            Z.append(float(list[8]))
    atom_dico['atom_central'] = list_atom
    atom_dico['residu'] = list_residu
    atom_dico['coord_X'] = X
    atom_dico['coord_Y'] = Y
    atom_dico['coord_Z'] = Z

    coord_dataframe = pd.DataFrame(atom_dico)
    return coord_dataframe

if __name__ == '__main__' :
    data = exctraction_coord('3i40.pdb')
    print(data)
