""" Fonctions Billes """

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
        bille_x = int(input("Donner la colonne où vous voulez poser la bille " + str(joueur) + " :"))
        while (bille_x < 0) or (bille_x > 7):
            print("Choississez un chiffre entre la colonne 1 et la colonne 7 en partant de la gauche!!")
            bille_x = int(input("Colonne_bille_" + str(joueur) + " :"))
            
            """condition tableau, bille posable"""
        print(tab[(bille_y)-1][(bille_x)-1])
        if tab[(bille_y)-1][(bille_x)-1] == (1,1):
            print("Trou! Choisissez un autre emplacement")
        else:
            dico_billes[joueur] = (bille_x, bille_y,couleur_bille)
            joueur += 1
    
    print(dico_billes)
    return dico_billes


def choix_bille():
    pass

#joueur_1 = pose_billes()
coul_j1 = "pink"
#joueur_2 = pose_billes()
#joueur_1 = {1: (1, 2), 2: (2, 4), 3: (3, 6), 4: (6, 4), 5: (1, 5)}




#def verif_bille(pallette, dico):
#besoin des palettes
