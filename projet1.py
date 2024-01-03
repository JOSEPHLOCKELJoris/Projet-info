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
    tableau = conversion_tableau(tableau)
    
    """choix position bille"""
    
    
    
    """
    affichage_billes(LARGEUR,HAUTEUR,"pink")
    affichage_billes(LARGEUR, HAUTEUR,"grey") #affichage billes
    tableau = action(tableau,dico_tirettes)
    affichage_billes(LARGEUR, HAUTEUR,coul_j1) #affichage billes
    print("i")
    """
    break
print("i")

    
    

    