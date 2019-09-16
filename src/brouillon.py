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


import numpy

n = 100

golden_angle = numpy.pi * (3 - numpy.sqrt(5))
theta = golden_angle * numpy.arange(n)
z = numpy.linspace(1 - 1.0 / n, 1.0 / n - 1, n)
print(z)
radius = numpy.sqrt(1 - z * z)

points = numpy.zeros((n, 3))
points[:,0] = radius * numpy.cos(theta)
points[:,1] = radius * numpy.sin(theta)
points[:,2] = z

#translocations :
#Generer une sphère1 :
sphere1 = golden_sphere(100)


#
