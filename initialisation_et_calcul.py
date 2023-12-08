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

def placement_aleatoire(tout):
    liste = []
    for tout in tirettes:
        position = []
        for hori_verti in tout:
            alea = randint(0,2)
            position.append(alea)
        liste.append(position)
    return liste

def all_tirettes():
    tirettes_horizontal = tirette_aleatoire()
    tirettes_verticale = tirette_aleatoire()
    tirettes = [tirettes_horizontal,tirettes_verticale]
    return tirettes

def possibilites(position_ex):
    if position_ex == 0:
        print("Vous pouvez uniquement tirez à gauche. Vous tirez donc à gauche. Action effectuée. ")
        return 1
    elif position_ex == 1:
        print("Vous pouvez tirez à droite ou à gauche. ")
        choix = input("Tapez d pout tirez à droite, g à gauche")
        if choix == "d":
            print("Vous tirez à droite. Action effectuée. ")
            return 0
        elif choix == "g":
            print("Vous tirez à gauche. Action effectuée. ")
            return 2
    elif position_ex == 2:
        print("Vous pouvez uniquemennt tirez à droite. Vous tirez donc à droite. Action effectuée. ")
        return 1
    
def choix_tirettes(positions):
    print("Il existe 2 types de tirettes: les verticales et les horizontales. ")
    sens = input("Quelles type de tirettes voulez-vous bouger? Tapez 'v' ou 'h'. ")
    print("Le rang se fait de haut en bas et de droite à gauche. ")
    rang = int(input("Quelles tirettes choississez vous? Tapez un chiffre de 0 à 6 puis sur la touche entrez. "))
    if sens == 'h':
        sens = 0
        positions[sens][rang] = possibilites(positions[sens][rang])
    elif sens == 'v':
        sens = 1
        print(positions)
        positions[sens][rang] = possibilites(positions[sens][rang])
    return positions

def reinitialisation(tirettes, position):
<<<<<<< HEAD
    """à faire avec tableau"""
=======
>>>>>>> f3d82c526e3ccb9fcdc8bdc9d4c09d08713adcc7
    pass

"""initialisation"""
tirettes = all_tirettes() #[[tirettes_horizontales],[tirettes_verticales]]
position = placement_aleatoire(tirettes) #position initiale de chaque tirettes

"""fonction à répéter"""
position = choix_tirettes(position) #choix et direction de la tirette
print(position)
reinitialisation(tirettes, position)# réinitialisation du plateau

