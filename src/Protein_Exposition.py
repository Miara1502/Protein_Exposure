# -*- coding: utf-8  -*-

"""Module qui contient touts les fonctions utilisés pour le projet : Calcul de la Surface
exposé au solvant d'une protéine
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

def calcule_distance_carre(point , atom):
    """Calcule la distance entre un point d'une sphère et un atom dans le fichier PDB
    Attention : LES VALEURS SONT ENCORE AU CARRE !!!!
    Il faut rajouter math.sqrt()
    """
    distance = (atom['coord_X'] - point['X'])**2 + (atom['coord_Y'] - point['Y'])**2 + (atom['coord_Z'] - point['Z'])**2
    return distance #math.sqrt(dist) pour la racine carré


def distance_all_atom(sphere , coord_dataframe):
    """ Calcule la distance entre un point et les atoms dans le fichier PDB , pour
    chaque point contenu dans la sphère , en utilisant le DataFrame de la sphère (translocation)
    qui correspond à un atome et le DataFrame contenant les coordonnées de tous les atom.
    Puis les stockent dans un dictionnaire ayant le numéro d'un point de la sphère comme index

        1) Calcul de la distance entre un point de la sphère et tous les atoms

        2) Création d'un dictionnaire qui va contenir toutes les distances pour chaque atome
            dic = {'index_sphere_points' : list_distance avec tous les autres atoms}

    """
    #TODO : - Fixer un seuil : seuil = dist(H20) + rayon de l'atom
    #       - calculer la distancer d'un point avec tous les atoms
    #       - même principe pour tous les autres points d'un nuage

    dico = {}
    for point in sphere.index :
        list_distance = []

        for i in range(len(coord_dataframe)) :
            distance = calcule_distance_carre(sphere.iloc[point] , coord_dataframe.iloc[i])
            list_distance.append(distance)

        dico[point] = list_distance

    return dico


if __name__ == '__main__' :

    data = exctraction_coord('3i40.pdb')
    print(data)


    atom1 = data.iloc[1]
    atom2 = data.iloc[2]

    ##################################EXEMPLE POUR UNE SPHERE/ ATOM #######################
    #translocation pour l'atome 01
    sphere_atom1 = translocation(atom1, 1000) #N: Nuage de points de la sphère


    print('\n')
    dist_sphere1  = distance_all_atom2(sphere_atom1 , data)
    #print(dist_sphere1)
    test = pd.DataFrame(dist_sphere1)
    print(test)



##########################################################################################
# FONCTION OBSOLETE /
'''
def distance_all_atom(sphere_point , coord_dataframe):
    #Un seul point avec tous les atoms  :


    #TODO : - Fixer un seuil : seuil = dist(H20) + rayon de l'atom
    #       - calculer la distancer d'un point avec tous les atoms
    #       - même principe pour tous les autres points d'un nuage

    list_distance = []

    for i in range(20) : #len(coord_dataframe)
        distance = calcule_distance_carre(sphere_point, coord_dataframe.iloc[i])
        list_distance.append(distance)

    return list_distance
'''
