from random import randint
from fltk import *

def tirette_aleatoire():
    tirettes = []
    i = 0
    while i < 7:
        ligne = []
        for tirette in range(7):
            alea = randint(0,1)
            if alea == 0:
                alea = False
            else:
                alea = True
            ligne.append(alea)
        tirettes.append(ligne)
        i+=1
    return tirettes

"""
True = Trou; False = Plat(la boule ne peut pas tomber!)
ex: True + True = La boule tombe
"""

tirettes_droite = tirette_aleatoire()
tirettes_gauche = tirette_aleatoire()
tirettes_haut = tirette_aleatoire()
tirettes_bas = tirette_aleatoire()


