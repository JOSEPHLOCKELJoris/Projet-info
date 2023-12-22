""" Fonctions Billes """

#Futur amelioration:
#Vérifier si la case n'est pas déjà occupée,
#besoin du plateau

def pose_billes():
    """
    Demande au joueurs de placer ces billes et stock
    leurs positions dans un dictionnaire.
    """
    #couleur_bille = input("Couleur bille? yellow, grey, pink...")
    dico_billes = {}
    for joueur in range(5):
        """ordonnée de la bille"""
        bille_y = int(input("ligne_bille_" + str(joueur) + " :"))
        while (bille_y < 0) or (bille_y > 7):
            print("Choississez un chiffre entre la ligne 1 et la ligne 7 en partant du haut!!")
            bille_y = int(input("Ligne_bille_" + str(joueur) + " :"))
        
        """abscisse de la bille"""
        bille_x = int(input("colonne_bille_" + str(joueur) + " :"))
        while (bille_x < 0) or (bille_x > 7):
            print("Choississez un chiffre entre la ligne 1 et la ligne 7 en partant de la gauche!!")
            bille_x = int(input("Colonne_bille_" + str(joueur) + " :"))
        dico_billes[joueur + 1] = (bille_x, bille_y,couleur_bille)
        
    return dico_billes


#joueur_1 = pose_billes()
coul_j1 = "pink"
#joueur_2 = pose_billes()
joueur_1 = {1: (1, 2), 2: (2, 4), 3: (3, 6), 4: (6, 4), 5: (1, 5)}




#def verif_bille(pallette, dico):
#besoin des palettes
