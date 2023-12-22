from random import randint
from fltk import *
from initialisation_et_calcul import *
from graphique import *
from bille import *


#dimension de la fenêtre
LARGEUR = 800
HAUTEUR = 800

jeu = True

"""
joueur_1 = pose_bille()
joueur_2 = pose_bille()
joueur_3 = pose_bille()
joueur_4 = pose_bille()
"""

cree_fenetre(LARGEUR,HAUTEUR)
menu(LARGEUR, HAUTEUR) #boucle du menu

while jeu:
    tableau = plateau(LARGEUR,HAUTEUR) #bouton JOUER pressé = début de l'installation du jeu
    
    """choix position bille"""
    affichage_billes(LARGEUR,HAUTEUR,"pink")
    tableau = action(tableau,dico_tirettes)
    
    print("i")
    
    
    #affichage_billes(largeur, hauteur,coul_j1) #affichage billes
    break
print("i")

    
    

    