""" Module """
from fltk import (image, rectangle, texte, attend_ev,
                  type_ev, cree_fenetre,abscisse,
                  ordonnee, efface_tout)


#dimension de la fenêtre
LARGEUR = 700
HAUTEUR = 500


def jeu(largeur, hauteur):
    """Algo du jeu.

    Args:
        hauteur (int): hauteur de la fenêtre
        largeur (int): largeur de la fenêtre
    """
    #rectangle(3*largeur//13, 3*hauteur//13, 10*largeur//13, 10*hauteur//13)
    
    ligne = 0
    colonne = 0
    nb_ligne = 7
    nb_colonne = 7
    
    cote = largeur / 11
    x = (largeur / 11)*2
    y = (hauteur / 11)*2
    x2 = x
    y2 = (hauteur / 11)*3
    print(x)
    while ligne != nb_ligne: #passe à la ligne suivante
        colonne = 0
        x = (largeur / 11)*2
        x2 = x + cote
        while colonne != nb_colonne: #fais toute une ligne
            rectangle(x,y,x2,y2)
            x+= cote
            x2 += cote
            colonne += 1
        ligne += 1
        y += cote
        y2 += cote


def regles(largeur, hauteur):
    """Algo des règles.

    Args:
        largeur (int): largeur de la fenêtre
        hauteur (int): hauteur de la fenêtre
    """
    image(largeur //2 ,hauteur //2, "img/Regle.jpg", largeur= largeur ,
          hauteur= hauteur, ancrage='c')
    #touche jouer
    rectangle(7*largeur // 10, 8 * hauteur // 10, 9 * largeur // 10,
              9 * hauteur // 10, remplissage="grey", tag="menu")
    texte(8*largeur // 10, 8.5 * hauteur // 10, "JOUER", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")
    #touche quitter
    rectangle(largeur // 10, 8 * hauteur // 10, 3 * largeur // 10,
              9 * hauteur // 10, remplissage="grey", tag="menu")
    texte(2*largeur // 10, 8.5 * hauteur // 10, "RETOUR", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")

    while True:
        evv = attend_ev()
        tev = type_ev(evv)
        if tev == 'Quitte':
            break
        if tev == "ClicGauche":
            #dimension de la touche
            if (7*largeur // 10 < abscisse(evv) < 3 * largeur // 10 and
                    8 * hauteur // 10 < ordonnee(evv) < 9 * hauteur // 10):
                efface_tout()
                jeu(LARGEUR, HAUTEUR)
            #dimension de la touche
            if (largeur // 10 < abscisse(evv) < 2 * largeur // 3 and
                    8 * hauteur // 10 < ordonnee(evv) < 9 * hauteur // 10):
                efface_tout()
                menu(LARGEUR, HAUTEUR)


def menu(largeur, hauteur):
    """
    Menu principale du jeu
    """
    #fond du menu
    image(largeur // 2, hauteur // 2, "img/fond_menu.jpg", largeur=2 * largeur, hauteur=2 * hauteur,
        ancrage='c')
    #dessin des touches du menu
    rectangle(largeur // 3, 4 * hauteur // 10, 2 * largeur // 3,
              5 * hauteur // 10, remplissage="blue", tag="menu")
    rectangle(largeur // 3, 6 * hauteur // 10, 2 * largeur // 3,
              7 * hauteur // 10, remplissage="green", tag="menu")
    rectangle(largeur // 3, 8 * hauteur // 10, 2 * largeur // 3,
              9 * hauteur // 10, remplissage="red", tag="menu")
    #texte des touches du menu
    texte(largeur // 2, 2.5 * hauteur // 10, "STAY ALIVE !", ancrage='c', couleur="black",
          taille=largeur // 18, tag="menu")
    texte(largeur // 2, 4.5 * hauteur // 10, "JOUER", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")
    texte(largeur // 2, 6.5 * hauteur // 10, "REGLES", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")
    texte(largeur // 2, 8.5 * hauteur // 10, "QUITTER", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")

    #boucle du menu
    while True:
        evv = attend_ev()
        tev = type_ev(evv)
        if tev == 'Quitte':
            break
        if tev == "ClicGauche":
            #dimension de la touche
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    4 * hauteur // 10 < ordonnee(evv) < 5 * hauteur // 10):
                efface_tout()
                jeu(LARGEUR, HAUTEUR)
            #dimension de la touche
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    6 * hauteur // 10 < ordonnee(evv) < 7 * hauteur // 10):
                efface_tout()
                regles(LARGEUR, HAUTEUR)
            #dimension de la touche
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    8 * hauteur // 10 < ordonnee(evv) < 9 * hauteur // 10):
                break

cree_fenetre(LARGEUR, HAUTEUR)
menu(LARGEUR, HAUTEUR)

#Bug quitter (prend du temps après être aller dans règles)
