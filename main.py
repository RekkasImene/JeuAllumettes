#########################################################################
# nom : main
# fonction : initialiser le jeu et l'organiser.
#########################################################################
import os
from afficher_allumettes import * 
from jeu_ordi import * 
from jeu_user import * 

def main():
    # initialisation des variables.
    nb_max_d=0 #nbre d'allumettes maxi au départ 
    nb_allu_max=0 #nbre d'allumettes maxi que l'on peut tirer au maxi
    nb_allu_rest=0; #nbre d'allumettes restantes
    prise=0 #nbre d'allumettes prises par le joueur
    qui= -1 #qui joue? 0=User --- 1=PC
    # verification pour l'initialisation.
    while( nb_max_d < 10 or nb_max_d > 60):
        try:
            nb_max_d=int(input("Entrez un nombre max d'allumette au depart entre 10 et 60."))
        except:
            print("saisie incorrecte")
    # mise a jour du nombre d'allumette en jeu.
    nb_allu_rest=nb_max_d
    
    # complétez, ……

    # verification pour l'initialisation de nb_allu_max
    while( nb_allu_max < 1 or nb_allu_max > nb_max_d):
        try:
                nb_allu_max=int(input("Entrez un nombre max d'allumette que l'on peut tirer."))
        except:
                print("saisie incorrecte")
    
    # verification pour l'initialisation de qui
    while( qui != 1 and qui != 0):
        try:
             qui=int(input("Qui commence? (0 pour le joueur et 1 pour l'ordinateur)."))
        except:
            print("saisie incorrecte")
    
    ##on commance le jeu
    print("le jeu commence ...")
    # Affichage du nombre total des allumettes
    afficher_allumettes(nb_allu_rest)
    # Reboucler tq le nbr allu restante > 0
    while nb_allu_rest>0 :
            if qui==1 :
                # Ordinateur qui va jouer
                print("***********ordinateur*********")
                prise=jeu_ordi(nb_allu_rest,nb_allu_max)
                nb_allu_rest=nb_allu_rest - prise
                # Affichage du nombre des allumettes restantes
                afficher_allumettes(nb_allu_rest)
                if nb_allu_rest == 0 :
                    print("Vous avez gagnee !")
                    break
                else:
                    qui=0
            else:
                # Joeur qui va jouer
                print("***********Joueur******")
                prise=jeu_user(nb_allu_rest,nb_allu_max)
                nb_allu_rest=nb_allu_rest - prise
                # Affichage du nombre des allumettes restantes
                afficher_allumettes(nb_allu_rest)
                if nb_allu_rest == 0 :
                    print("Vous avez perdu !")
                    break
                else:
                    qui=1
    print("le jeu est termine ...")

   # test de main
if __name__ == "__main__":
    main()
    os.system("pause")     
    