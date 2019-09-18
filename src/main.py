#!/usr/bin/env python3

"""
Main qui va générer les résultats à partir d'un fichier pdb en utilisant les fonctions
du module Protein_Expsition.py
"""

import Protein_Exposition as PE

import argparse
import sys

parser = argparse.ArgumentParser(description="Surface exposition , main program.")
# Positionnal argument containing the 3D coordinate of genes
parser.add_argument("-p", "--positions-file", type= str,
                    help='Lien vers le fichier PDB contenant les coordonnes x , y , z des atoms de la Proteine',
                    dest="atomPos", metavar="atom_position_file")
parser.add_argument("-n", "--nb-points", help="Selectionner le nombre de points pour chaque sphere --DEFAULT = 10",
                    type=int, default=10, dest="nPoint", metavar="nbPoints")
parser.add_argument("-d", "--d-max", help="definir une limite de distance (>=5 ) pour séléctionner que les atomes voisins --DEFAULT = 5.6",
                    type=float, default=5.6, dest="dMax", metavar="dist_Max")
parser.add_argument("outfile", nargs='?', default="-", metavar='filename.txt',
                    help="Va générer les résultats du programme dans un fichier .txt , ex : > filename.txt ( or STDOUT). / doit etre un fichier.txt")



args = parser.parse_args()

coord = PE.exctraction_coord(args.atomPos)

resultat = PE.Exposition_All(coord,args.nPoint , args.dMax)
print(resultat)
