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
    while i < NB_CASES:
        ligne = []
        trou_min = 0
        trou_max = 0
        for tirette in range(NB_CASES + 2):
            alea = randint(0,1)
            if alea == 0:
                alea = False
                trou_max += 1
                if trou_max == 3:
                    alea = True
            else:
                alea = True
                trou_min += 1
                if trou_min == 5:
                    alea = False
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
        if lst[ligne-1][elt] is True:
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
        if lst[colonne-1][elt + (debut-1)] is True:
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
        if (tableau[case][0] == 0 or tableau[case][1] == 0):
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
    dico = {}
    for elt in range(NB_CASES*2):
        debut = randint(1,3)
        val = (lst[elt], debut)
        dico[int(elt+1)] = val
    return dico

def rempli_tab(dico, lst):
    """Rempli de tableau de tirettes verticales et horizontales

    Args:
        dico (dict): tableau

    Returns:
        _type_: _description_
    """
    for elt in range(1, NB_CASES+1):
        num_hori = elt
        num_verti = elt+NB_CASES
        dico = rempli_hori(dico, tirettes_hori, elt, lst[num_hori][1])
        dico = rempli_verti(dico, tirettes_verti, elt, lst[num_verti][1])
    return dico

def action(tab, dico):
    """Demande aux jouer quel action il souhaite effectuer, 
    et le fait.

    Args:
        tab (dict): tableau du jeu
        dico (dict): dictionnaire des tirettes

    Returns:
        tab: tableau du jeu après l'action
    """
    cond_tir = False
    cond_dir = False
    while not cond_tir:
        num_tir = input("Numéro de tirettes: ")
        if num_tir.isdigit() is True:
            if int(int(num_tir)) <= NB_CASES*2:
                cond_tir = True
        else:
            print("La tirette n'existe pas")
    while not cond_dir:
        direction = str(input("Pousser(D) ou Tirer(G): "))

        # Si le joueur souhaite tirer la tirette
        if direction == "G":
            cond_dir = True

            #Tirettes verticales
            if int(num_tir) > NB_CASES:
                if dico[int(num_tir)][1] == 1:
                    rempli_verti(tab, tirettes_verti, int(num_tir)-NB_CASES, dico[int(num_tir)][1])
                else:
                    nv_depart = dico[int(num_tir)][1] - 1
                    dico[int(num_tir)] = (tirettes_hori[int(num_tir)-NB_CASES-1],nv_depart)
                    rempli_verti(tab, tirettes_verti, int(num_tir)-NB_CASES, nv_depart)
            #Tirettes horizontales
            else:
                if dico[int(num_tir)][1] == 1:
                    rempli_hori(tab, tirettes_hori, int(num_tir), dico[int(num_tir)][1])
                else:
                    nv_depart = dico[int(num_tir)][1] - 1
                    dico[int(num_tir)] = (tirettes_hori[int(num_tir)-1],nv_depart)
                    rempli_hori(tab, tirettes_hori, int(num_tir), nv_depart)

        #Si le joueur souhaite pousser la tirette
        elif direction == "D":
            cond_dir = True

            #Tirettes verticales
            if int(int(num_tir)) > NB_CASES:
                if dico[int(int(num_tir))][1] == 3:
                    rempli_verti(tab, tirettes_verti, int(num_tir)-NB_CASES,
                                 dico[int(int(num_tir))][1])
                else:
                    nv_depart = dico[int(num_tir)][1] + 1
                    dico[int(num_tir)] = (tirettes_verti[int(num_tir)-NB_CASES-1],nv_depart)
                    rempli_verti(tab, tirettes_verti, int(num_tir)-NB_CASES, nv_depart)
            #Tirettes horizontales
            else:
                if dico[int(int(num_tir))][1] == 3:
                    rempli_hori(tab, tirettes_hori, int(num_tir), dico[int(num_tir)][1])
                else:
                    nv_depart = dico[int(num_tir)][1] + 1
                    dico[int(int(num_tir))] = (tirettes_hori[int(num_tir)-NB_CASES-1],nv_depart)
                    rempli_hori(tab, tirettes_hori, int(num_tir), nv_depart)

        else:
            print("Mouvement impossible")
        return tab, dico_tirettes


#Initialisation:
#[tirettes_horizontales], [tirettes_verticales], [liste de toutes les tirettes]
tirettes_hori, tirettes_verti, lst_tirettes = all_tirettes()

#Tableau du jeu : dico avec tuple (x, y) pour hozi, verti
tableau = cree_grille(NB_CASES)

#Dico de toutes les tirettes avec leurs indice de début
dico_tirettes = num_tirettes(lst_tirettes)

#Rempli le tableau de tirettes
tableau = rempli_tab(tableau, dico_tirettes)

#Liste de True, False pour indiquer si trou
#ou pas pour chaque case
val_cases=statut_case(tableau)
