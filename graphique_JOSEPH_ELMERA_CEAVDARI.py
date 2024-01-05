""" Module """
from fltk import *
from random import *
from initialisation_et_calcul_JOSEPH_ELMERA_CEAVDARI import (val_cases, NB_CASES, tableau,dico_tirettes,lst_tirettes,
                                      rempli_verti,rempli_hori,tirettes_verti,tirettes_hori,
                                      rempli_tab, action, cree_grille, num_tirettes)
from bille_JOSEPH_ELMERA_CEAVDARI import *

#dimension de la fenêtre
LARGEUR = 600
HAUTEUR = 600

def plateau(largeur, hauteur,tab):
    """Affiche le plateau du jeu """
    efface_tout()
    image(largeur // 2, hauteur // 2, "img/fond_ecran.jpg",
          largeur=2 * largeur, hauteur=2 * hauteur,
        ancrage='c') #affichage fond ecran
    tirettes(largeur, hauteur) #affichage tirettes en arrière plan
    #carré du jeu
    rectangle((largeur/11)*2,(hauteur/11)*2,(largeur / 11)*9,(hauteur/11)*9,
              remplissage="grey",epaisseur=4) #cadre du jeu

    """ Choix des couleurs des cases tirettes superposées
            gris = La bille tombe
            bleu = La bille est sur le plat horizontal (vertical doute?!! :) )
            vert = La bille est sur le plat vertical
    """

    lst_couleur=[]
    for elmt in tab:
        if tab[elmt][0] == 0: #plat horizontal
            lst_couleur.append("green")
        elif (tab[elmt][1] == 0) and (tab[elmt][0] == 1):#plat verti et pas plat hori
            lst_couleur.append("blue")
        else: #trou
            lst_couleur.append(None)  

    #cases centrales
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


    #affichage des numéros des tirettes
    affichage_num(largeur,hauteur)

    mise_a_jour()
    return tableau

def tirettes(largeur, hauteur):
    """Affichage des tirettes et de leurs couleurs"""

    """couleur tirette verticales"""
    list_couleur = []
    for tir in dico_tirettes:
        for elmt in dico_tirettes[tir][0]:
            if elmt == False:
                list_couleur.append("blue")
            else:
                list_couleur.append(None)

    #tirettes verticales
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
            if 2*cote<(x+((dico_tirettes[ligne+1][1])-1)*cote)<9*cote:
                rectangle(x+((dico_tirettes[ligne+1][1])-1)*cote,y,
                          x2+((dico_tirettes[ligne+1][1])-1)*cote,y2)
            else:
                rectangle(x+((dico_tirettes[ligne+1][1])-1)*cote,y,
                          x2+((dico_tirettes[ligne+1][1])-1)*cote,y2,remplissage=list_couleur[i])
            rectangle(y,x+((dico_tirettes[ligne+8][1])-1)*cote,y2,
                      x2+((dico_tirettes[ligne+8][1])-1)*cote,remplissage=list_couleur[i+63])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote

    #couleur tirette horizontales
    list_couleur = []
    for tir in dico_tirettes:
        for elmt in dico_tirettes[tir][0]:
            if elmt == False:
                list_couleur.append("green")
            else:
                list_couleur.append(None)

    #tirettes horizontales
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
            if 2*cote<(x+((dico_tirettes[ligne+1][1])-1)*cote)<9*cote:
                rectangle(x+((dico_tirettes[ligne+1][1])-1)*cote,y,
                          x2+((dico_tirettes[ligne+1][1])-1)*cote,y2)
            else:
                rectangle(x+((dico_tirettes[ligne+1][1])-1)*cote,y,x2+((dico_tirettes[ligne+1][1])-1)*cote,y2,
                          remplissage=list_couleur[i])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote
    mise_a_jour()


def affichage_billes_1(largeur, hauteur,joueur_1):
    """Affiche les billes"""
    ligne = 0
    colonne = 0
    nb_ligne = 7
    nb_colonne = 7
    cote = largeur/22*2
    x = (largeur/22)*5
    y = (hauteur/22)*5
    x2 = x
    y2 = (hauteur/22)*3
    i = 0
    print("i",joueur_1)
    while ligne != nb_ligne: #passe à la ligne suivante
        colonne = 0
        x = (largeur/22)*5
        x2 = x + cote
        while colonne != nb_colonne: #fais toute une ligne
            for bille in joueur_1:
                if (joueur_1[bille][0]-1) == colonne: #comparaison abscisse
                    if (joueur_1[bille][1]-1)== ligne: #comparaison ordonnee
                        cercle(x,y,cote/2,couleur=joueur_1[bille][2],remplissage=joueur_1[bille][2])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote
    mise_a_jour()
    return joueur_1

def regles(largeur, hauteur):
    """Algo des règles.

    Args:
        largeur (int): largeur de la fenêtre
        hauteur (int): hauteur de la fenêtre
    """
    #image regles
    image(largeur//2 ,hauteur//2, "img/Regle.jpg", largeur=largeur,
          hauteur = hauteur, ancrage='c')
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
            #Retour menu
            if (largeur//10 < abscisse(evv) < 2*largeur//3 and
                    8*hauteur//10 < ordonnee(evv)< 9*hauteur//10):
                efface_tout()
                menu(LARGEUR, HAUTEUR, tableau)

def menu(largeur, hauteur,tableau):
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
    boucle_menu(largeur,hauteur)
    return tableau

def boucle_menu(largeur,hauteur):
    """Boucle du menu

    Args:
        largeur (int): largeur de la fenêtre
        hauteur (int): hauteur de la fenêtre
    """
    #boucle du menu
    cond_menu = True
    while cond_menu:
        evv = attend_ev()
        tev = type_ev(evv)
        if tev == 'Quitte':
            break
        if tev == "ClicGauche":
            #touche JOUER
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    4 * hauteur // 10 < ordonnee(evv) < 5 * hauteur // 10):
                efface_tout()
                boucle_jeu()
            #touche REGLES
            elif (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    6 * hauteur // 10 < ordonnee(evv) < 7 * hauteur // 10):
                efface("menu")
                image(largeur //2 ,hauteur //2, "img/Regle.jpg", largeur= largeur
                      , hauteur= hauteur, ancrage='c')
                efface_tout()
                regles(LARGEUR, HAUTEUR)
            #touche QUITTER
            elif (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    8 * hauteur // 10 < ordonnee(evv) < 9 * hauteur // 10):
                cond_menu = False

    mise_a_jour()

def affichage_num(largeur,hauteur):
    """création liste numéro tirettes"""
    num = []
    i = 1
    while i <= 14:
        num.append(i)
        i += 1

    #affichage numéro vertical
    i = 0
    x = largeur/22
    y = (hauteur/22)*5
    while i <= 6:
        texte(x,y, str(num[i]),couleur="red",taille=15)
        i += 1
        y += hauteur/11

    #affichage numéro horizontal
    i = 0
    x = (largeur/22)*5
    y = hauteur/22
    while i <= 6:
        texte(x,y, str(num[i+7]),couleur="red",taille=15)
        x += largeur/11
        i += 1

def defaite(dico_joueur):
    """Vérifie si il reste des bilels aux joueur

    Args:
        dico_joueur (dict): dictionnaire des billes
    
    """
    if dico_joueur == {}:
        return True
    else:
        return False

def boucle_jeu():
    """Boucle du jeu

    Args:
        larg (_type_): _description_
        haut (_type_): _description_
    """
    tour = 0

    dico_tirettes = num_tirettes(lst_tirettes)
    tableau = cree_grille(NB_CASES)
    tableau = rempli_tab(tableau, dico_tirettes)
    joueur_1 = pose_billes(tableau)
    #joueur_1={1: (1 ,1, 'yellow')}
    jeu = True
    evv = attend_ev()
    tev = type_ev(evv)
    while jeu:
        if tev == 'Quitte':
            jeu = False
        plateau(LARGEUR, HAUTEUR,tableau)
        affichage_billes_1(LARGEUR, HAUTEUR, joueur_1)
        tabl ,dico_tirettes= action(tableau, dico_tirettes)
        tableau = tabl
        joueur_1 = verif_bille(tableau, joueur_1)
        plateau(LARGEUR, HAUTEUR,tableau)
        if defaite(joueur_1) is True:
            jeu = False
            efface_tout()
            texte(HAUTEUR // 2, 2.5 * HAUTEUR // 10, "VICTOIRE !", ancrage='c', couleur="black",
            taille=LARGEUR // 18, tag="menu")
            attend_ev()

def jeu():
    """Jeu à éxecuter
    """
    cree_fenetre(LARGEUR,HAUTEUR)
    menu(LARGEUR, HAUTEUR,tableau)
    ferme_fenetre()
