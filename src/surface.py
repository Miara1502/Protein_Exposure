#!/usr/bin/env python3

"""
""" # TODO Write a dockstrings 

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
parser.add_argument("outfile", nargs='?', default="-", metavar='filename.txt',
                    help="Create a file to put the result of the program ex: > filename.txt ( or STDOUT). / must be a .text file")


args = parser.parse_args()

coord = PE.exctraction_coord(args.atomPos)

resultat = PE.protocol(coord,args.nPoint)
print(resultat)
