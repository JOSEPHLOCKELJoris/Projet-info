""" Module """
from fltk import *
from random import *
from initialisation_et_calcul import (val_cases, NB_CASES, tableau,dico_tirettes,lst_tirettes,
                                      rempli_verti,rempli_hori,tirettes_verti,tirettes_hori)
from bille import *

#dimension de la fenêtre
LARGEUR = 800
HAUTEUR = 800

def plateau(largeur, hauteur):
    efface_tout()
    image(largeur // 2, hauteur // 2, "img/fond_ecran.jpg", largeur=2 * largeur, hauteur=2 * hauteur,
        ancrage='c') #affichage fond ecran
    tirettes(largeur, hauteur) #affichage tirettes en arrière plan
    
    """carré du jeu"""
    rectangle((largeur/11)*2,(hauteur/11)*2,(largeur / 11)*9,(hauteur/11)*9,remplissage="grey",epaisseur=4) #cadre du jeu
    
    
    """Algo du jeu.

    Args:
        hauteur (int): hauteur de la fenêtre
        largeur (int): largeur de la fenêtre
    """
    #rectangle(3*largeur//13, 3*hauteur//13, 10*largeur//13, 10*hauteur//13)

   
    
    """ Choix des couleurs des cases tirettes superposées
            gris = La bille tombe
            bleu = La bille est sur le plat horizontal (vertical doute?!! :) )
            vert = La bille est sur le plat vertical
    """
    
    lst_couleur=[]
    for elmt in tableau:
        if tableau[elmt][0] == 0: #plat horizontal
            lst_couleur.append("green")
        elif (tableau[elmt][1] == 0) and (tableau[elmt][0] == 1):#plat verti et pas plat hori
            lst_couleur.append("blue")
        else: #trou
            lst_couleur.append(None)  

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
        

    """affichage des numéros des tirettes"""
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
            rectangle(y,x+((dico_tirettes[ligne+8][1])-1)*cote,y2,x2+((dico_tirettes[ligne+8][1])-1)*cote,remplissage=list_couleur[i+63])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote

    
    """couleur tirette horizontales"""
    list_couleur = []
    for tir in dico_tirettes:
        for elmt in dico_tirettes[tir][0]:
            if elmt == False:
                list_couleur.append("green")
            else:
                list_couleur.append(None)
    
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
            rectangle(x+((dico_tirettes[ligne+1][1])-1)*cote,y,x2+((dico_tirettes[ligne+1][1])-1)*cote,y2,remplissage=list_couleur[i])
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote
        
def affichage_billes(largeur, hauteur,joueur_1):
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
    while ligne != nb_ligne: #passe à la ligne suivante
        colonne = 0
        x = (largeur/22)*5
        x2 = x + cote
        while colonne != nb_colonne: #fais toute une ligne
            for bille in joueur_1:
                if (joueur_1[bille][0]-1) == colonne: #comparaison abscisse
                    if (joueur_1[bille][1]-1)== ligne: #comparaison ordonnee
                        cercle(x,y,cote/2,couleur=joueur_1[bille][2],remplissage=joueur_1[bille][2])
                        #cercle(x,y,cote/2,couleur=coul_j1,remplissage=coul_j1) #bille tracé    
            x+= cote
            x2 += cote
            colonne += 1
            i += 1
        ligne += 1
        y += cote
        y2 += cote
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
    boucle_menu(largeur,hauteur)
    return tableau

def boucle_menu(largeur,hauteur):
    #boucle du menu
    while True:
        evv = attend_ev()
        tev = type_ev(evv)
        print(tev)
        if tev == 'Quitte':
            break
        if tev == "ClicGauche":
            #touche JOUER
            if (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    4 * hauteur // 10 < ordonnee(evv) < 5 * hauteur // 10):
                efface_tout()
                return tableau
            #touche REGLES
            elif (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
                    6 * hauteur // 10 < ordonnee(evv) < 7 * hauteur // 10):
                efface("menu")
                image(largeur //2 ,hauteur //2, "img/Regle.jpg", largeur= largeur , hauteur= hauteur, ancrage='c') 
                efface_tout()
                regles(LARGEUR, HAUTEUR)
            #touche QUITTER
            elif (largeur // 3 < abscisse(evv) < 2 * largeur // 3 and
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

def action(dico, lst):
    num_tir = int(input("Numéro de tirettes: "))
    direction = input("Pousser(d) ou Tirer(g): ")
    if num_tir > NB_CASES*2:
        num_tir = int(input("Tirettes introuvable: "))
    if direction != "d" or "g":
        dico_tirettes = input("Mauvaise syntaxe: ")
    if num_tir > NB_CASES:
        dico = rempli_verti(dico, tirettes_verti, num_tir, lst[num_tir][1])
    else:
        dico = rempli_hori(dico, tirettes_hori, num_tir, lst[num_tir][1])
    return dico



