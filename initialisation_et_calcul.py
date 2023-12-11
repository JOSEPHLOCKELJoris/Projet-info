"""Module"""
from random import randint
from fltk import *

NB_CASES = 7 #Nombre de cases par ligne

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

def placement_aleatoire(posi_hori,posi_verti):  
    pos_hori = []
    position = []
    for tirette in posi_hori:
        alea = randint(0,2)
        position.append(alea)
    pos_hori.append(position)
    
    pos_verti = []
    position = []
    for tirette in posi_verti:
        alea = randint(0,2)
        position.append(alea)
    pos_verti.append(position)
    return pos_hori, pos_verti

def all_tirettes():
    tirettes_horizontal = tirette_aleatoire()
    tirettes_verticale = tirette_aleatoire()
    return tirettes_horizontal,tirettes_verticale

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
    
def choix_tirettes(posi_hor,posi_vert):
    print("Il existe 2 types de tirettes: les verticales et les horizontales. ")
    sens = input("Quelles type de tirettes voulez-vous bouger? Tapez 'v' ou 'h'. ")
    print("Le rang se fait de haut en bas et de droite à gauche. ")
    rang = int(input("Quelles tirettes choississez vous? Tapez un chiffre de 0 à 6 puis sur la touche entrez. "))
    if sens == 'h':
        posi_hor[0][rang] = possibilites(posi_hor[0][rang])
    elif sens == 'v':
        print(posi_vert)
        posi_vert[0][rang] = possibilites(posi_vert[0][rang])
    return posi_hor, posi_vert

def reinitialisation(tir_hori,tir_verti,pos_hori,pos_verti):
    """à faire avec tableau"""
    pass

#Initialisation
tirettes_hori,tirettes_verti = all_tirettes() #[tirettes_horizontales],[tirettes_verticales]
#position initiale de chaque tirettes
posi_hori,posi_verti = placement_aleatoire(tirettes_hori,tirettes_verti)
print(tirettes_hori)


"""fonction à répéter
print(posi_hori, posi_verti)
posi_hori, posi_verti = choix_tirettes(posi_hori,posi_hori) #nouvelle position suite au choix et direction de la tirette par le joueur
print(posi_hori, posi_verti)
reinitialisation(tirettes_hori,tirettes_verti,posi_hori, posi_verti)# réinitialisation du plateau
"""

def cree_grille():
    """Crée une grille sous forme de dictionnaire qui 
    servira de plateau de jeu.

    Returns:
        dict: contient les données de chaque cases
    """
    dico = {}
    for case in range(NB_CASES**2):
        dico[case] = []
    return dico


def rempli_hori(dico, lst, ligne, debut):
    """Complète la ligne souhaité de la grille en horizontale
    selon la liste contenant les tirettes

    Args:
        dico (dict): grille
        lst (list): liste des tirettes horizontales
        ligne (int): numéro de la ligne à modifier
        debut (int): postion de la tirettes

    Returns:
        dict: grille modifiée
    """
    for elt in range((debut-1), ((debut-1)+ NB_CASES)):
        if tirettes_hori[ligne-1][elt] == True:
            dico[NB_CASES*(ligne-1) + (elt-(debut-1))] = 1
        else:
            dico[NB_CASES*(ligne-1) + (elt-(debut-1))] = 0
    return dico

tableau = cree_grille()
tableau = rempli_hori(tableau, tirettes_hori, 7, 3)
print(tableau)
