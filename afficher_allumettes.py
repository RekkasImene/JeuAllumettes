#########################################################################
# nom : afficher_allumettes
# valeurs entree : n 
# valeurs sortie : /
# fonction : affiche les allumettes qui rest
#########################################################################


def afficher_allumettes(n):
    i=0
    print("nombre d\'allumette restante est: ", n)
    while i<n:
        print("O",end=' ')
        i +=1
    print("")
    i=0
    while i<n:
        print("|",end=' ')
        i +=1
    print("")


    
    