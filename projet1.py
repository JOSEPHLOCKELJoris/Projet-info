from random import randint
from fltk import *

def tirette_aleatoire():
    tirettes = []
    i = 0
    while i < 7:
        ligne = []
        for tirette in range(9):
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

def all_tirettes():
    tirettes_horizontal = tirette_aleatoire()
    tirettes_verticale = tirette_aleatoire()
    tirettes = [tirettes_horizontal,tirettes_verticale]

def choix_tirettes(tirettes):
    print("Il existe 2 types de tirettes: les verticales et les horizontales")
    sens = input("Quelles type de tirettes voulez-vous bouger? Tapez 'v' ou 'h'")
    print("Le rang se fait de haut en bas et de droite à gauche.")
    rang = int(input("Quelles tirettes choississez vous? Tapez un chiffre de 0 à 6 puis sur la touche entrez."))
    if cote == 'h':
        cote = 0
        tirettes[cote][rang] = bouge_tirettes(tirettes[cote][rang]) #reconfig tirette select
    elif cote == 'v':
        cote = 1
        tirettes[cote][rang] = bouge_tirettes(tirettes[cote][rang]) #reconfig tirette select
    return tirettes

def bouge_tirettes(tirette):
    #Fonction donnant les possibilités de "tire", bientôt
    direction = input("Dans quel sens voulez-vous tirez?")
    pas = input("De combien de fois voulez-vous tirez?")

    #tirette bouge, reinitialisation
    
    return tirette
    pass
    

tirettes = all_tirettes()
choix_tirettes(tirettes)
    

