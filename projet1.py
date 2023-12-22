from random import randint
from fltk import *
import initialisation_et_calcul
import graphique
import bille

jeu = True

"""
joueur_1 = pose_bille()
joueur_2 = pose_bille()
joueur_3 = pose_bille()
joueur_4 = pose_bille()
"""

while jeu:
    cree_fenetre(LARGEUR, HAUTEUR)
    
    menu(LARGEUR, HAUTEUR)

    