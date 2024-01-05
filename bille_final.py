""" Fonctions Billes """
from initialisation_et_calcul import NB_CASES

#Futur amelioration:
#Vérifier si la case n'est pas déjà occupée,
#besoin du plateau

def pose_billes(tableau):
    """tableau séparé en ligne"""
    #statut case
    tab = []
    tabl = []
    i = 0
    for elem in tableau:
        tabl.append(tableau[elem])
        i += 1
        if i == 7:
            tab.append(tabl)
            i = 0
            tabl = []

    """
    Demande au joueurs de placer ces billes et stock
    leurs positions dans un dictionnaire.
    """
    #couleur_bille = input("Couleur bille? yellow, grey, pink...")
    couleur_bille = "yellow"
    dico_billes = {}
    joueur = 1
    while joueur != 6:
        """ordonnée de la bille"""
        bille_y = int(input("Donner la ligne où vous voulez poser la bille " + str(joueur) + " :"))
        while (bille_y < 0) or (bille_y > 7):
            print("Choississez un chiffre entre la ligne 1 et la ligne 7 en partant du haut!!")
            bille_y = int(input("Ligne_bille_" + str(joueur) + " :"))

        """abscisse de la bille"""
        bille_x = int(input("Donner la colonne où vous voulez poser la bille " +str(joueur) + " :"))
        while (bille_x < 0) or (bille_x > 7):
            print("Choississez un chiffre entre la colonne 1 et la colonne 7 en partant de la gauche!!")
            bille_x = int(input("Colonne_bille_" + str(joueur) + " :"))

        #condition tableau, bille posable
        if tab[(bille_y)-1][(bille_x)-1] == (1,1):
            print("Trou! Choisissez un autre emplacement")
        else:
            dico_billes[joueur] = (bille_x, bille_y,couleur_bille)
            joueur += 1

    return dico_billes

def verif_bille(dico_tab, dico_joueur):
    """Vérifie si les billes d'un joueur sont sur un trou, 
    et les supprimes alors si besoin .

    Args:
        dico_tab (dict): tableau du jeu
        dico_joueur (dict): billes du joueur

    Returns:
        dico_joueur: Dictionnaire des billes qui ne sont
        pas sur des trou
        -----------------------------------------------------------
        joueur_1={1: (1 ,1, 'yellow'), 2: (1, 2, 'yellow'), 3: (1, 3, 'yellow'),
              4: (1, 4, 'yellow'), 5: (1, 5, 'yellow')}
        tableau = {0: (1, 1), 1: (1, 1), 2: (1, 0), 3: (0, 1), 4: (1, 0), 5: (0, 1),
                6: (1, 1), 7: (1, 0)
        >>> joueur_1 = verif_bille(tableau, joueur_1)
        >>> print(joueur_1)
        {2: (1, 2, 'yellow'), 3: (1, 3, 'yellow'),4: (1, 4, 'yellow'),
        5: (1, 5, 'yellow')}
    """
    lst_del = []
    for elt, val in dico_joueur.items():
        case = int((val[1]-1)*NB_CASES + (val[0]-1))
        if (dico_tab[case][0]) == 1 and (dico_tab[case][1] == 1):
            lst_del.append(elt)
    for supp in lst_del:
        del dico_joueur[supp]
    return dico_joueur

COUL_J1 = "pink"
