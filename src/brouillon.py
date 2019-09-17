import math
import time
import numpy as np
import scipy
import pandas as pd

from scipy.spatial import distance_matrix
import pprint

def exctraction_coord(pdb_file):
    """Lis un fichier PDB (type = str) et retourne un Pandas DataFrame qui contient
    les coordonnées de chaque atome , leurs nom ainsi que leur résidus

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
    """Crée un nuage de point dstribué dans une sphère / Algortihm Golden Spirale
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
    """Translocation d'une sphere pour un atom en utilisant l'atome comme origine de la sphère (1)
        - Créer une sphère avec la fonction Golden_sphere
        - Créer un dictionnaire contenant le radius de chaque atome dans le fichier PDB
        - Translocation de la sphère
        - N : Correspond au nombre de nuage de points qu'on souhaite générer
    """
    nouvelle_sphere = golden_sphere(n)
    #print(sphere)

    dico_rayon = {'H':1.2,'C':1.7,'N':1.55,'O':1.52,'F':1.47,'S':1.8}
    for i , (atom, r) in enumerate(dico_rayon.items()):
        if(Atom['Atom_name'] == atom) :
            rayon = r
            #print(rayon)
            nouvelle_sphere['X'] = (nouvelle_sphere['X'] + Atom['coord_X'])*rayon
            nouvelle_sphere['Y'] = (nouvelle_sphere['Y'] + Atom['coord_Y'])*rayon
            nouvelle_sphere['Z'] = (nouvelle_sphere['Z'] + Atom['coord_Z'])*rayon

    return nouvelle_sphere




if __name__ == '__main__':
    data = exctraction_coord('CD59_2J8B.pdb')
    print(data)


    df = pd.DataFrame(dico)
    print(df)
