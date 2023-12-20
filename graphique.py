""" Module """
from fltk import *
from random import *
from initialisation_et_calcul import (val_cases, NB_CASES, tableau,dico_tirettes,lst_tirettes)


#dimension de la fenêtre
LARGEUR = 800
HAUTEUR = 800

def plateau(largeur, hauteur):
    
    image(largeur // 2, hauteur // 2, "img/fond_ecran.jpg", largeur=2 * largeur, hauteur=2 * hauteur,
        ancrage='c')
    
    """Algo du jeu.

    Args:
        hauteur (int): hauteur de la fenêtre
        largeur (int): largeur de la fenêtre
    """
    #rectangle(3*largeur//13, 3*hauteur//13, 10*largeur//13, 10*hauteur//13)

    """ Choix des couleurs des cases par tirettes
            Bleu = un plat
            Rouge = un trou
    """
    
    list_couleur=[]
    for tir in dico_tirettes:
        for elmt in dico_tirettes[str(tir)][0]:
            if elmt == False:
                list_couleur.append("blue")
            else:
                list_couleur.append("red")
    
    
    """tirettes horizontales"""
    ligne = 0
    colonne = 0
    nb_ligne = 7
    nb_colonne = 9
    cote = largeur / 11
    x = 0
    y = (hauteur / 11)*2
    x2 = largeur / 11
    y2 = (hauteur / 11)*3
    i = 0
    while ligne != nb_ligne: #passe à la ligne suivante
        colonne = 0
        x = 0
        x2 = x + cote
        while colonne != nb_colonne: #fais toute une ligne
            rectangle(x+((dico_tirettes[str(ligne+1)][1])-1)*cote,y,x2+((dico_tirettes[str(ligne+1)][1])-1)*cote,y2,remplissage=list_couleur[i])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote

    
    """tirettes verticales"""
    ligne = 0
    colonne = 0
    nb_ligne = 7
    nb_colonne = 9
    cote = largeur / 11
    x = 0
    y = (hauteur / 11)*2
    x2 = x + cote
    y2 = (hauteur / 11)*3
    i = 0
    while ligne != nb_ligne: #passe à la ligne suivante
        colonne = 0
        x = 0
        x2 = x + cote
        while colonne != nb_colonne: #fais toute une ligne
            rectangle(y,x+((dico_tirettes[str(ligne+8)][1])-1)*cote,y2,x2+((dico_tirettes[str(ligne+8)][1])-1)*cote,remplissage=list_couleur[i+63])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote
      
    
    """ Choix des couleurs des cases tirettes superposées
            Rouge = La bille tombe
            orange = La bille est sur un seul plat
            Blanc = La bille est sur 2 plat
    """
    
    lst_couleur=[]
    for i in range (NB_CASES**2):
        for elmt in tableau:
            if tableau[elmt][0] == False and tableau[elmt][1] == False:
                lst_couleur.append("blue")
            elif (tableau[elmt][0] == True and tableau[elmt][1] == False) or (tableau[elmt][0] == False and tableau[elmt][1] == True):
                lst_couleur.append("orange")
            else:
                lst_couleur.append("red")  
      
    """cases centrales"""
    ligne = 0
    colonne = 0
    nb_ligne = 7
    nb_colonne = 7
    cote = largeur / 11
    x = (largeur / 11)*2
    y = (hauteur / 11)*2
    x2 = x
    y2 = (hauteur / 11)*3
    i = 0
    while ligne != nb_ligne: #passe à la ligne suivante
        colonne = 0
        x = (largeur / 11)*2
        x2 = x + cote
        while colonne != nb_colonne: #fais toute une ligne
            rectangle(x,y,x2,y2,remplissage=lst_couleur[i])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote
    
    #cadre du jeu
    rectangle((largeur/11)*2,(hauteur/11)*2,(largeur / 11)*9,(hauteur/11)*9,epaisseur=4)

def tirettes(dico_tirettes):
    print(lst_tirettes,dico_tirettes)
    for elem in dico_tirettes:
        print(dico_tirettes[elem][1])
        pass
    pass


def regles(largeur, hauteur):
    """Algo des règles.

    Args:
        largeur (int): largeur de la fenêtre
        hauteur (int): hauteur de la fenêtre
    """
    #image regles
    image(largeur//2 ,hauteur//2, "img/Regle.jpg", largeur=largeur,
          hauteur = hauteur, ancrage='c')
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
            if (largeur//10 < abscisse(evv) < 2*largeur//3 and
                    8*hauteur//10 < ordonnee(evv)< 9*hauteur//10):
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
        print(tev)
        if tev == 'Quitte':
            break
        if tev == "ClicGauche":
            #dimension de la touche
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    4 * hauteur // 10 < ordonnee(evv) < 5 * hauteur // 10):
                efface_tout()
                plateau(LARGEUR, HAUTEUR)
            #dimension de la touche
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    6 * hauteur // 10 < ordonnee(evv) < 7 * hauteur // 10):
                efface("menu")
                image(largeur //2 ,hauteur //2, "img/Regle.jpg", largeur= largeur , hauteur= hauteur, ancrage='c') 
                efface_tout()
                regles(LARGEUR, HAUTEUR)
            #dimension de la touche
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    8 * hauteur // 10 < ordonnee(evv) < 9 * hauteur // 10):
                break
    mise_a_jour()
    ferme_fenetre()

def affichage_num(largeur,hauteur):
    """création liste numéro tirettes"""
    num = []
    i = 1
    while i <= 14:
       num.append(i)
       i += 1
    
    """affichage numéro vertical"""
    i = 0
    x = largeur/22
    y = (hauteur/22)*5
    while i <= 6:
        texte(x,y, str(num[i]),couleur="red",taille=15)
        i += 1
        y += hauteur/11
    
    """affichage numéro horizontal"""
    i = 0
    x = (largeur/22)*5
    y = hauteur/22
    while i <= 6:
        texte(x,y, str(num[i+7]),couleur="red",taille=15)
        x += largeur/11
        i += 1

#tirettes(dico_tirettes)
cree_fenetre(LARGEUR,HAUTEUR)
menu(LARGEUR, HAUTEUR)

