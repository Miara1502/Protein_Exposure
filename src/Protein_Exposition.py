# -*- coding: utf-8  -*-

"""Module qui contient tous les fonctions utilisés pour le projet : Calcul de la Surface
exposé au solvant d'une protéine
"""

import math
import time
import numpy as np
import pandas as pd



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
    """Crée un nuage de points de coordonnées(x,y,z) dstribué dans une sphère / Algortihm Golden Spirale
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
        - Translocation de la sphère
        - N : Correspond au nombre de nuage de points qu'on souhaite générer
    """
    nouvelle_sphere = golden_sphere(n)
    nouvelle_sphere['X'] = nouvelle_sphere['X'] + Atom['coord_X']
    nouvelle_sphere['Y'] = nouvelle_sphere['Y'] + Atom['coord_Y']
    nouvelle_sphere['Z'] = nouvelle_sphere['Z'] + Atom['coord_Z']
    return nouvelle_sphere

def calcule_distance(point_sphere , point_atom):
    """Calcule la distance entre un point d'une sphère et un atom dans le fichier PDB
    """
    distance = (point_atom['coord_X'] - point_sphere['X'])**2 + (point_atom['coord_Y'] - point_sphere['Y'])**2 + (point_atom['coord_Z'] - point_sphere['Z'])**2
    return math.sqrt(distance) #math.sqrt(dist) pour la racine carré


def distance_all_point(sphere , atom):
    """Calcule la distance entre tous les points de la sphere et un atom dans le fichier PDB
    retourne une liste contenant plusieurs distance
    """
    list_distance = [] #entre tous les points et un atom
    for i in range(len(sphere)):
        dist = calcule_distance(sphere.iloc[i] , atom)
        list_distance.append(dist)
    return list_distance

def distance_all_atom(sphere , coord_dataframe):
    """ Calcule la distance entre tous les points de la sphere et tous  les atoms dans le fichier PDB/
    retourne un dictionnaire ayant comme clé l'indice d'un atom et comme valeur une liste de distance
    avec tous les points de la sphère puis la transforme en data frame
    """
    dico = {}
    for ind_atom in range(len(coord_dataframe)) :
        dico[ind_atom] = distance_all_point(sphere , coord_dataframe.iloc[ind_atom])
    dico_df = pd.DataFrame(dico)
    return dico_df


def EXPOSITION(distance_dataframe , Atom , seuil_distance):
    """Permet de calculer la surface exposé au solvant de l'atome
        - Calcul de la surface de l'atom
        - Calcul du ration exposé
        - Surface d'exposition : le produit de la surface et le ratio
    retourne la surface exposé au solvant
    """
    #1 CALCUL DE LA SURFACE
    rayon = 0
    dico_rayon = {'H':1.2,'C':1.8,'N':1.5,'O':1.4,'F':1.47,'S':1.8}
    for i , (atom, r) in enumerate(dico_rayon.items()):
        if(Atom['Atom_name'] == atom) :
            rayon = r
    surface = 4*math.pi*((rayon)**2)

    #2) Calcul du ratio exposé :  #Si DISTANCE > seuil => Point exposé
    count = 0
    seuil = 2.8 + rayon
    limite = seuil_distance
    for i in range(len(distance_dataframe)):
        for j in range(len(distance_dataframe.iloc[i])):
            if((distance_dataframe.iloc[i][j]) >= seuil and (distance_dataframe.iloc[i][j]) < limite ):
            #FIXME : DEFINIR UNE LIMITE POUR NE PAS CONSIDERER TOUTES LES DISTANCES :
                count = count + 1
    ratio = count/(distance_dataframe.shape[0]*distance_dataframe.shape[1])

    #3) Calcul de la surface exposé :
    return ratio*surface


def Surface(Atom) :
    """Renvoie la surface d'une sphère/atom
    """
    rayon = 0
    dico_rayon = {'H':1.2,'C':1.8,'N':1.5,'O':1.4,'F':1.47,'S':1.8}
    for i , (atom, r) in enumerate(dico_rayon.items()):
        if(Atom['Atom_name'] == atom) :
            rayon = r
    surface = 4*math.pi*((rayon)**2)
    return surface



def Exposition_All(coord_dataframe , nbr_point , seuil_distance):
    """Renvoie une liste contenant la surface exposé au solvant pour tous les atomes
    de la pdb en utilisant les fonctions de la manière suivante :
    1) Selection d'un atome
    2) Création d'une sphère puis Translocation
    3) Calcul des différentes distances avec tous les atoms du pdb
    4) Calcul de la surface exposé de l'atome 
    """
    dico = {}
    list_surface = []
    for atom_number in range(len(coord_dataframe)) :
        atom = coord_dataframe.iloc[atom_number]
        sphere = translocation(atom , nbr_point)
        distance_atom = distance_all_atom(sphere , coord_dataframe)
        expo = EXPOSITION(distance_atom , atom , seuil_distance)
        dico[atom_number] = expo

        s = Surface(coord_dataframe.iloc[atom_number])
        list_surface.append(s)

    list = []
    for i , j in enumerate(dico.items()) :
        valeur =  j[1]
        list.append(valeur)

    coord_dataframe['exposition'] = list
    coord_dataframe['surface_atom'] = list_surface

    return coord_dataframe

#       - Faire le même calcul pour tous les atoms
