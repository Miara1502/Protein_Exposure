# Exposition d'une protéine au solvant
## Miara Rakotomavo : 

## Description : 

Un programme ptyhon qui permet de calculer la surface exposée au solvant des atomes d'une protéine.

## Requirements :

### System : 

	Linux : ce programme peut être compilé sous un un environnement linux. 

### Python packages : 

Pour faire fonctionner le programme , il est nécessaire de le lancer sur python3 avec les différents packages suivants: 

	* Pandas
	* Numpy
	* Scipy
	* Argparse

## Data files : 

Le programme va être lancé sur un fichier pdb contenant les coordonnées x, y, z des atomes de la protéine.

	* Protein_3D_coordinate data file.

## Script files :

### Protein_exposition.py

Ce script sera utilisé pour: 
	lire le fichier pdb / extraire les coordonnées
	effectuer tous les calculs nécessaire pour obtenir la surface exposé par atome
	stocker les résultats dans un Pandas Data Frame.
### main.py

Ceci est le script principal (main) du programme , celui qui va être lancé, pour procéder à toutes les étapes de calcul à partir des modules du script précedent.

## Usage : 

Tout d'abord , il faudra cloner le répertoire git suivant : 

	$git clone https://github.com/Miara1502/Protein_Exposure.git

ou le télécharger , ensuite il va falloir ce placer dans le répértoire Protein_Exposure : 

Pour Lancer le programme, utiliser la ligne de commande suivante avec les arguments de votre choix:

	$python3 src/main.py -p data/pdb_file.pdb -n Nuage_de_point -d distance_limite


## Exemple d'usage : 
### Conseil d'utilisation pour une visualisation rapide des résultats : 
	faire tourner sur une petite protéine avec n = 10 (nuage de points pour chaque sphere)  

Placez vous dans le répertoire Protein_Exposure et tapez la ligne de commande suivante pour lancer le programme sur un fichier pdb contenant 100_atom , avec un nuage de points de 10 distribués en sphère avec une distance max = 6 comme limite de calcul entre 2 atomes : 

	$python3 src/main.py -p data/100_atom.pdb -n 10 -d 6

Autre exemple , pour le pdb 3i40.pdb : 

	$python3 src/main.py -p data/3i40.pdb -n 10 -d 6

Warning : pour le fichier 3i40.pdb , les calculs peuvent durer jusqu'à 8mn , voir rapport , pour plus de détail 


 

