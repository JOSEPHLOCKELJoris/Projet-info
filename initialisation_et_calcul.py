"""Module"""
from random import randint
from fltk import *

NB_CASES = 7 #Nombre de cases par ligne

def tirette_aleatoire():
    """Crée une liste de 0,1  qui représente
    une tirette 0 pour un trou , 1 pour pas de trou

    Returns:
        list: tirette
    """
    tirettes = []
    i = 0
    while i < 7:
        ligne = []
        for tirette in range(NB_CASES + 2):
            alea = randint(0,1)
            if alea == 0:
                alea = False
            else:
                alea = True
            ligne.append(alea)
        tirettes.append(ligne)
        i+=1
    return tirettes

def all_tirettes():
    """Crée une liste avec:
    - toutes les tirettes horizontales
    - toutes les tirettes verticales
    - toutes les tirettes

    Returns:
        list: voir précédemment
    """
    tirettes_horizontal = tirette_aleatoire()
    tirettes_verticale = tirette_aleatoire()
    tirettes_tab = []
    for elt in tirettes_horizontal:
        tirettes_tab.append(elt)
    for elt in tirettes_verticale:
        tirettes_tab.append(elt)
    return tirettes_horizontal, tirettes_verticale, tirettes_tab

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
        posi_vert[0][rang] = possibilites(posi_vert[0][rang])
    return posi_hor, posi_vert

def reinitialisation(tir_hori,tir_verti,pos_hori,pos_verti):
    """à faire avec tableau"""
    pass

#Initialisation:
#[tirettes_horizontales], [tirettes_verticales], [liste de toutes les tirettes]
tirettes_hori, tirettes_verti, lst_tirettes = all_tirettes()

def cree_grille(nb_cases):
    """Crée une grille sous forme de dictionnaire qui 
    servira de plateau de jeu.

    Returns:
        dict: contient les données de chaque cases
    """
    dico = {}
    for case in range(nb_cases**2):
        dico[case] = (0,0)
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
        if lst[ligne-1][elt] == True:
            val = list(dico[NB_CASES*(ligne-1) + (elt-(debut-1))])
            val[0] = 1
            dico[NB_CASES*(ligne-1) + (elt-(debut-1))] = tuple(val)
        else:
            val = list(dico[NB_CASES*(ligne-1) + (elt-(debut-1))])
            val[0] = 0
            dico[NB_CASES*(ligne-1) + (elt-(debut-1))] = tuple(val)
    return dico

def rempli_verti(dico, lst, colonne, debut):
    """Complète la colonne souhaité de la grille en horizontale
    selon la liste contenant les tirettes

    Args:
        dico (dict): grille
        lst (list): liste des tirettes horizontales
        colonne (int): numéro de la colonne à modifier
        debut (int): postion de la tirettes

    Returns:
        dict: grille modifiée
    """
    for elt in range(NB_CASES):
        if lst[colonne-1][elt + (debut-1)] == True:
            val = list(dico[(colonne-1) + NB_CASES*elt])
            val[1] = 1
            dico[(colonne-1) + NB_CASES*elt] = tuple(val)

        else:
            val = list(dico[(colonne-1) + NB_CASES*elt])
            val[1] = 0
            dico[(colonne-1) + NB_CASES*elt] = tuple(val)
    return dico

def statut_case(tableau):
    """Indique si il y a un trou sur la case

    Args:
        tableau (dict): valeurs de chaque case 
        sous tuple (x,y) pour la tirettes horizontal et vertical

    Returns:
        val_cases: list
    """
    vl_case = []
    for case in tableau:
        if tableau[case][0] == 0 and tableau[case][1] == 0:
            val = False
        else:
            val = True
        vl_case.append(val)
    return vl_case

def num_tirettes(lst):
    """Crée dictionnaire contenant les tirettes et 
    leurs indice de début.

    Args:
        lst (list): liste contenant toutes les tirettes

    Returns:
        dico: contient le nom, les valeurs sous liste et 
        l'indice de chaque tirettes
    """
    lst_tirettes = []
    dico = {}
    for elt in range(NB_CASES*2):
        debut = randint(1,3)
        val = (lst[elt], debut)
        dico[int(elt+1)] = val
    return dico

def rempli_tab(dico, lst):
    for elt in range(1, NB_CASES+1):
        num_hori = elt
        num_verti = elt+7
        dico = rempli_hori(dico, tirettes_hori, elt, lst[num_hori][1])
        dico = rempli_verti(dico, tirettes_verti, elt, lst[num_verti][1])
    return dico


#Tableau du jeu : dico avec tuple (x, y) pour hozi, verti
tableau = cree_grille(NB_CASES)

#Liste de True, False pour indiquer si trou
#ou pas pour chaque case
val_cases=statut_case(tableau)

#Dico de toutes les tirettes avec leurs indice de début
dico_tirettes = num_tirettes(lst_tirettes)

#Rempli le tableau de tirettes
tableau = rempli_tab(tableau, dico_tirettes)

#Tests:

#print(tirettes_hori)
#print(tirettes_verti)
#print(lst_tirettes)
print(tableau)
#print(dico_tirettes)
#print(val_cases)