# Gestion des fonctions de sauvegarde
# Ecriture d'un fichier de sauvegarde
# Lecture d'un fichier de sauvegarde

import time
import dict_pieces

def sauvegarde(plateau, dicoJ1, dicoJ2, dicoJ3, dicoJ4):
    '''
    Entrée : plateau, une matrice 22x22 ; les dictionnaires des joueurs
    But : Ecriture d'un fichier 'blokus_date_heure.txt' contenant le plateau puis les dicos des joueurs
    Sortie : None
    Créateur : Romain
    '''
    
    # Création du nom du fichier
    date = time.localtime(time.time())
    nom_fichier = 'blockus_' + str(date.tm_year) + str(date.tm_mon) + str(date.tm_mday) + '_' + str(date.tm_hour) + str(date.tm_min) + '.txt'
   
    fichier = open(nom_fichier, 'w')  # Ouverture du fichier
    
    for ligne in plateau:  # Ecriture dans le fichier du plateau
        fichier.write(str(ligne)+'\n')
    
    fichier.write(str(dicoJ1.keys)+'\n')  # Ecriture dans le fichier des dicos des joueurs
    fichier.write(str(dicoJ2.keys)+'\n')
    fichier.write(str(dicoJ3.keys)+'\n')
    fichier.write(str(dicoJ4.keys)+'\n')

    fichier.close()  # Fermeture du fichier
    return


def lecture_sauvegarde(nom_fichier):
    '''
    Entrée : nom_fichier, str
    But : lire le fichier et en déduire le joueur qui doit jouer, les dictionnaires des joueurs, le plateau en cours de partie
    Sortie : une liste [plateau, dicoJ1, dicoJ2, dicoJ3, dicoJ4, joueur_a_jouer]
    Créateur : Romain
    '''

    fichier = open(nom_fichier, 'r')
    plateau = []
    lignes = fichier.realines()
    for k in range(23):
        ligne = []
        for x in lignes[k]:
            ligne.append(x)
        plateau.append(ligne)
    dicoJ1 = {}
    dicoJ2 = {}
    dicoJ3 = {}
    dicoJ4 = {}
    for cle in lignes[23]:
        dicoJ1[int(cle)] = dict_pieces.dict.get(int(cle))
    for cle in lignes[24]:
        dicoJ2[int(cle)] = dict_pieces.dict.get(int(cle))
    for cle in lignes[25]:
        dicoJ3[int(cle)] = dict_pieces.dict.get(int(cle))
    for cle in lignes[26]:
        dicoJ4[int(cle)] = dict_pieces.dict.get(int(cle))
    
    joueur_a_jouer = min((1, len(dicoJ1)), (2, len(dicoJ2)), (3, len(dicoJ3)), (4, len(dicoJ4)), 1)
    
    






