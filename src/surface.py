#!/usr/bin/env python3

"""
""" # TODO the program is not doing that, but it is OK for the moment. (to improve the description later).

import argparse
import pandas as pd

import Protein_Exposition as PE

import sys
import pprint

parser = argparse.ArgumentParser(description="Surface exposition , main program.")
# Positionnal argument containing the 3D coordinate of genes
parser.add_argument("-p", "--positions-file", type= str,
                    help='Path to the file containing the x, y, z coordinates of atoms',
                    dest="atomPos", metavar="atom_position_file")

parser.add_argument("-n", "--nb-points", help="Select the number of points for each sphere --DEFAULT = 10",
                    type=int, default=10, dest="nPoint", metavar="noGenes")
args = parser.parse_args()

coord = PE.exctraction_coord(args.atomPos)
print(coord)
print('\n')
resultat = PE.protocol(coord,agrs.npoint)
print(resultat)
