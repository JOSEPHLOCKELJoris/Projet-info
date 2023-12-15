from random import randint
from fltk import *
import initialisation_et_calcul
import graphique

jeu = True

while jeu:
    cree_fenetre(LARGEUR, HAUTEUR)
    menu(LARGEUR, HAUTEUR)