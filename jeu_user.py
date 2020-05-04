#########################################################################
# nom : jeu_user
# valeurs entree : nb_allum et prise_max, nombre d'allumette en jeu et
# nombre d'allumette que l'on peut prendre au plus.
# valeurs sortie : prise, nombre d'allumettes prises.
# fonction : retourne la prise à faire
#########################################################################
def jeu_user(nb_allum, prise_max):
    j=-1
    while j<1 or j>prise_max or j>nb_allum:
        try:
             j=int(input("vous prenez combien d\'allumettes?"))
        except:
             print("saisie incorrecte")
    prise=j
    print("le joueur en prend : ", prise)
    return prise