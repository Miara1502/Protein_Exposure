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
#parser.add_argument("-e", "--geneExpression-file", type=argparse.FileType('r'), help='path to the file containing the gene expression ', dest="geneExpr", metavar="gene_expression_file")
#parser.add_argument("outfile", nargs='?', default="-", metavar='html_file', help="Path to the outputfile of the 3D_Visualization (or STDOUT). / must be a .html file")
#parser.add_argument("-n", "--nb-genes", help="Select the number of the closest genes --DEFAULT = 10", type=int, default=10, dest="nGenes", metavar="noGenes")
#parser.add_argument("-c", "--method-correlation", help="Select the methode of correlation --DEFAULT = 'pearson'", type=str, default='pearson', dest="mCorr", metavar="methode_correlation")
args = parser.parse_args()

coord = PE.exctraction_coord(args.atomPos)


print(coord)
