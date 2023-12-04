""" Fonctions Billes """

def pose_billes():
    """
    Demande au joueurs de placer ces billes et stock
    leurs positions dans un dictionnaire.
    """
    dico_billes = {}
    for joueur in range(5):
        bille_x = int(input("x:"))
        bille_y = int(input("y:"))
        dico_billes[joueur + 1] = (bille_x, bille_y)
    return dico_billes
    """
    Futur amelioration:
    vérifier si la case n'est pas déjà occupée,
    besoin du plateau 
    """

joueur_1 = pose_billes()
print(joueur_1)

#def verif_bille(pallette, dico):
#besoin des palettes
