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


def translocation(Atom , sphere):
    """Create a sphere for each atoms with n number of points
    """
    sphere_nouv = sphere
    #TODO : Create a dictionnary for all the atom
    dico_rayon = {'H':1.2,'C':1.7,'N':1.55,'O':1.52,'F':1.47,'S':1.8}
    for i , (atom, r) in enumerate(dico_rayon.items()):
        if(Atom['Atom_name'] == atom) :
            rayon = r

            sphere_nouv['X'] = (sphere['X'] + Atom['coord_X'])*rayon
            sphere_nouv['Y'] = (sphere['Y'] + Atom['coord_Y'])*rayon
            sphere_nouv['Z'] = (sphere['Z'] + Atom['coord_Z'])*rayon


    print(rayon)

    return sphere_nouv


if __name__ == '__main__' :

    data = exctraction_coord('3i40.pdb')
    print(data)
    print(data['Atom_name'])

    s1 = golden_sphere(10)
    print(s1)

    atom1 = data.iloc[0]
    print(atom1['coord_X'])

    print('Je suis làa')

    nouv = translocation(atom1 , s1)

    print(nouv)
