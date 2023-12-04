

def tirettes():
    tirette_droite = [[True,True,True,True,False,False,True],[True,False,True,False,True,False],[False,False,True,False,False,True,True],[True,False,False,True,True,True,False],[False,True,False,False,False,False,True],[False,False,True,True,False,False,True],[True,False,True,True,True,True,False]]
    tirette_gauche = [[True,False,True,False,True,False],[False,True,False,False,False,False,True],[False,False,True,False,False,True,True],[True,False,False,True,True,True,False],[True,True,True,True,False,False,True],[False,False,True,True,False,False,True],[True,False,True,True,True,True,False]]
    tirette_haut = [[True,False,True,False,True,False],[False,False,True,False,False,True,True],[True,True,True,True,False,False,True],[True,False,False,True,True,True,False],[False,True,False,False,False,False,True],[True,False,True,True,True,True,False],[False,False,True,True,False,False,True]]
    tirette_bas = [[True,True,True,True,False,False,True],[False,False,True,False,False,True,True],[True,False,True,False,True,False],[True,False,False,True,True,True,False],[False,True,False,False,False,False,True],[True,False,True,True,True,True,False],[False,False,True,True,False,False,True]]
    lst_tirettes = [tirette_gauche,tirette_droite,tirette_haut,tirette_bas]
    return lst_tirettes
    
tirettes()

