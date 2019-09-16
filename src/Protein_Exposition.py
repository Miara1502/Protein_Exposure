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

def exctraction_coord(pdb_file):
    """Get a PDB file and return a Pandas Dataframe of x , y, z coordinates ,
    name and residu for each atomes.
    """

    filin = open(pdb_file)
    #position_file.seek(0)

    atom_dico = {"atom_central" : [] , "residu" : [] , "coord_X" : [] ,
                 "coord_Y" : [] , "coord_Z" : []}
    list_atom = []
    list_residu = []
    X = []
    Y = []
    Z = []
    for line in filin:
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
    coord_dataframe['Atom_name'] = coord_dataframe['atom_central'].astype(str).str[0]

    return coord_dataframe

def golden_sphere(n):
    """create a sphere with n points
    """
    golden_angle = np.pi * (3 - np.sqrt(5))
    theta = golden_angle * np.arange(n)
    z = np.linspace(1 - 1.0 / n, 1.0 / n - 1, n)
    radius = np.sqrt(1 - z * z)

    points = np.zeros((n, 3))
    points[:,0] = radius * np.cos(theta)
    points[:,1] = radius * np.sin(theta)
    points[:,2] = z
    sphere = pd.DataFrame(points)
    sphere.columns = ['X' , 'Y' , 'Z']

    return sphere


def translocation(Atom , n):
    """translocate a sphere for one atom
    """
    sphere = golden_sphere(n)
    #print(sphere)

    dico_rayon = {'H':1.2,'C':1.7,'N':1.55,'O':1.52,'F':1.47,'S':1.8}
    for i , (atom, r) in enumerate(dico_rayon.items()):
        if(Atom['Atom_name'] == atom) :
            rayon = r
            #print(rayon)
            sphere['X'] = (sphere['X'] + Atom['coord_X'])*rayon
            sphere['Y'] = (sphere['Y'] + Atom['coord_Y'])*rayon
            sphere['Z'] = (sphere['Z'] + Atom['coord_Z'])*rayon

    return sphere


if __name__ == '__main__' :

    data = exctraction_coord('3i40.pdb')
    print(data)
    print(data['Atom_name'])


    atom1 = data.iloc[1]
    print(atom1['coord_X'])

    #translocation pour l'atome 01
    nouv1 = translocation(atom1, 10)
    print(nouv1)
