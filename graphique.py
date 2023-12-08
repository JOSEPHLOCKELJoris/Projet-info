""" Module """
from fltk import (image, rectangle, texte, attend_ev,
                  type_ev, cree_fenetre,abscisse,
                  ordonnee, efface, efface_tout, rectangle)

"""def jeu(hauteur, largeur):
    rectangle(2* largeur // 10, 2* hauteur // 10, )"""

def menu(hauteur, largeur):
    """
    Menu principale du jeu
    """
    image(largeur // 2, hauteur // 2, "img/fond_menu.jpg", largeur=2 * largeur, hauteur=2 * hauteur,
        ancrage='c')
    rectangle(largeur // 3, 4 * hauteur // 10, 2 * largeur // 3,
              5 * hauteur // 10, remplissage="blue", tag="menu")
    rectangle(largeur // 3, 6 * hauteur // 10, 2 * largeur // 3,
              7 * hauteur // 10, remplissage="green", tag="menu")
    rectangle(largeur // 3, 8 * hauteur // 10, 2 * largeur // 3,
              9 * hauteur // 10, remplissage="red", tag="menu")
    texte(largeur // 2, 2.5 * hauteur // 10, "STAY ALIVE !", ancrage='c', couleur="black",
          taille=largeur // 18, tag="menu")
    texte(largeur // 2, 4.5 * hauteur // 10, "JOUER", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")
    texte(largeur // 2, 6.5 * hauteur // 10, "REGLES", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")
    texte(largeur // 2, 8.5 * hauteur // 10, "QUITTER", ancrage='c',
          couleur="white", taille=largeur // 40, tag="menu")

    while True:
        evv = attend_ev()
        tev = type_ev(evv)
        if tev == 'Quitte':
            break
        if tev == "ClicGauche":
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    4 * hauteur // 10 < ordonnee(evv) < 5 * hauteur // 10):
                efface_tout()
                texte(largeur // 2, 2.5 * hauteur // 10, "JEU", ancrage='c', couleur="blue",
                taille=largeur // 18, tag="menu")
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    6 * hauteur // 10 < ordonnee(evv) < 7 * hauteur // 10):
                efface("menu")
                texte(largeur // 2, 2.5 * hauteur // 10, "REGLES", ancrage='c', couleur="blue",
                      taille=largeur // 18, tag="menu")
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    8 * hauteur // 10 < ordonnee(evv) < 9 * hauteur // 10):
                break

cree_fenetre(700,500)
menu(500, 700)
