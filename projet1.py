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
    
    """Config bille"""
    joueur_1 = pose_billes(tableau)
    #joueur_1 = {1: (1, 1, 'yellow'), 2: (2, 1, 'yellow'), 3: (3, 1, 'yellow'), 4: (4, 1, 'yellow'), 5: (7, 1, 'yellow')}
    affichage_billes(LARGEUR,HAUTEUR,joueur_1)

    break
print("i")

    
    
#Bug : la fênetre se ferme ps quand on est en jeu