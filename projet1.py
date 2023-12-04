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
        
def tirettes():
    tirette_droite = tirette_aleatoire()
    tirette_gauche = tirette_aleatoire()
    tirette_haut = tirette_aleatoire()
    tirette_bas = tirette_aleatoire()
    lst_tirettes = [tirette_gauche,tirette_droite,tirette_haut,tirette_bas]
    return lst_tirettes
    
tirettes = tirettes() #liste de liste: tirette gauche, droite, haut, bas


