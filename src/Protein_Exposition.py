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


'''
def exctraction_coord(position file) :
    atom_coord = {"coordX" : [] , "coordY" : [] , "coordZ" : []}

    list_atom = []
    list_residu = []
    X = [] , Y = [] , Z = []
    for line in open(position file) :
        list = line.split()
        id = list[0]
        if id == 'ATOM':
            list_atom.append(list[2])
            list_residu.append(list[3])
            X.append(float(list[5]))
            Y.append(float(list[6]))
            Z.append(float(list[7]))
'''


#Fonction brut
#TODO : Création d'une fonction pour cette partie
atom_coord = {"atom_central" : [] , "residu" : [] , "coord_X" : [] ,
             "coord_Y" : [] , "coord_Z" : []}
list_atom = []
list_residu = []
X = []
Y = []
Z = []
for line in open('3i40.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        list_atom.append(list[2])
        list_residu.append(list[3])
        X.append(float(list[6]))
        Y.append(float(list[7]))
        Z.append(float(list[8]))

atom_coord['atom_central'] = list_atom
atom_coord['residu'] = list_residu
atom_coord['coord_X'] = X
atom_coord['coord_Y'] = Y
atom_coord['coord_Z'] = Z

data = pd.DataFrame(atom_coord)
