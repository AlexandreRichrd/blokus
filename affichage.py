# Gestion de l'affichage console

import dict_pieces  # Pour valentin, affichage des pièces disponibles, à supprimer dans le futur

def afficher_plateau(plateau):
    '''
    Entrée : plateau, une matrice 22x22
    But : Afficher proprement dans la console le plateau de jeu
    Sortie : None
    Créateur : Romain
    '''
    for ligne in plateau:
        print(ligne)
    return


def afficher_piece(dico_joueur):
    '''
    Entrée : dico_joueur, le dictionnaire contenant les pièces d'un joueur tel que {numéro_pièce : (pièce, config_pièce), ...} où
                numéro_pièce : un entier (1,21)
                pièce : une matrice
                config_pièce : une liste de matrices
    But : Afficher dans la console toutes les pièces du dico_joueur une par une avec un indice
    Sortie : None
    Créateur : Valentin
    '''
#J'appelle le dico_joueur en tant que choix disponible pour le joueur
#je vais chercher les informations dans les différents dictionnaires  
    #1- Obtenir les clés
    #2 -parcourir les clés / ajouter à une liste ou chaine de caractère la pièce liée à la clé



#fin de la boucle lorsqu'on arrive à 22 pièces vu qu'on en dispose que de 21
    if dict_pieces < 22 :
#Afficcher les pièces
         print(dico_joueur)




afficher_piece(dict_pieces.dict)