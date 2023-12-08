def tirette_aleatoire():
    tirettes = []
    i = 0
    while i < 7:
        ligne = []
        for tirette in range(9):
            alea = randint(0,1)
            if alea == 0:
                alea = False
            else:
                alea = True
            ligne.append(alea)
        tirettes.append(ligne)
        i+=1
    return tirettes

"""
True = Trou; False = Plat(la boule ne peut pas tomber!)
ex: True + True = La boule tombe
"""

def all_tirettes():
    tirettes_horizontal = tirette_aleatoire()
    tirettes_verticale = tirette_aleatoire()
    tirettes = [tirettes_horizontal,tirettes_verticale]
    return tirettes

def choix_tirettes(tirettes):
    print("Il existe 2 types de tirettes: les verticales et les horizontales.")
    sens = input("Quelles type de tirettes voulez-vous bouger? Tapez 'v' ou 'h'. ")
    print("Le rang se fait de haut en bas et de droite à gauche. ")
    rang = int(input("Quelles tirettes choississez vous? Tapez un chiffre de 0 à 6 puis sur la touche entrez. "))
    if sens == 'h':
        sens = 0
        tirettes[sens][rang] = bouge_tirettes(tirettes[sens][rang]) #reconfig tirette select
    elif sens == 'v':
        sens = 1
        tirettes[sens][rang] = bouge_tirettes(tirettes[sens][rang]) #reconfig tirette select
    return tirettes

def bouge_tirettes(tirette):
    
    """Fonction donnant les possibilités de "tire" à droite et/ou à gauche""" #en cours
    
    print("Vous pouvez tirez d'un cran vers la gauche ou la droite.")
    direct = input("Dans quel sens voulez-vous tirez? Tapez 'd' ou 'g'. ")
    
    """tirette bouge, reinitialisation"""#en cours
    if direct == 'd':
        pass
    elif direct == 'g':
        pass
    
    return tirette


tirettes = all_tirettes()
choix_tirettes(tirettes)