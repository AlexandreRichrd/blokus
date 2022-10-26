# Gestion des fonctions de sauvegarde
# Écriture d'un fichier de sauvegarde
# Lecture d'un fichier de sauvegarde

import time
import dict_pieces


def sauvegarde(plateau, dicoj1, dicoj2, dicoj3, dicoj4):
    """ Entrée : plateau, une matrice 22x22 ; les dictionnaires des joueurs
    But : Ecriture d'un fichier 'blokus_date_heure.txt' contenant le plateau puis les cles des pièces restantes
     des joueurs
    Sortie : None
    Créateur : Romain """
    
    # Création du nom du fichier
    date = time.localtime(time.time())
    nom_fichier = 'blokus_' + str(date.tm_year) + str(date.tm_mon) + str(date.tm_mday) \
                  + '_' + str(date.tm_hour) + str(date.tm_min) + '.txt'
   
    fichier = open(nom_fichier, 'w')  # Ouverture du fichier
    
    for lignes in plateau:  # Ecriture dans le fichier du plateau
        ligne = ''
        for case in lignes:
            ligne = ligne + case
        ligne = ligne + '\n'
        fichier.write(ligne)

    # Ecriture dans le fichier des dicos des joueurs
    for dico in [dicoj1, dicoj2, dicoj3, dicoj4]:
        ligne = ''
        for k in dico.keys():
            ligne = ligne + str(k) + ' '
        ligne = ligne + '\n'
        fichier.write(ligne)

    fichier.close()  # Fermeture du fichier

    return


def lecture_sauvegarde(nom_fichier):
    """
    Entrée : nom_fichier, str
    But : lire le fichier, en déduire le joueur qui doit jouer, les dictionnaires des joueurs, le plateau
    Sortie : une liste [plateau, dicoj1, dicoj2, dicoj3, dicoj4, joueur_a_jouer]
    Créateur : Romain
    """

    fichier = open(nom_fichier, 'r')
    plateau = []
    lignes = fichier.readlines()
    for k in range(22):
        ligne = []
        for x in lignes[k]:
            if x != '\n':
                ligne.append(x)
        plateau.append(ligne)

    dicoj1 , dicoj2, dicoj3, dicoj4 = {}, {}, {}, {}

    print(len(lignes))
    for cle in lignes[22].split(' '):
        if cle != '\n':
            dicoj1[int(cle)] = dict_pieces.dict.get(int(cle))
    for cle in lignes[23].split(' '):
        if cle != '\n':
            dicoj2[int(cle)] = dict_pieces.dict.get(int(cle))
    for cle in lignes[24].split(' '):
        if cle != '\n':
            dicoj3[int(cle)] = dict_pieces.dict.get(int(cle))
    for cle in lignes[25].split(' '):
        if cle != '\n':
            dicoj4[int(cle)] = dict_pieces.dict.get(int(cle))
    
    joueur_a_jouer = min([(1, len(dicoj1)), (2, len(dicoj2)), (3, len(dicoj3)), (4, len(dicoj4))], key = lambda t: t[1])[0]
    return [plateau, dicoj1, dicoj2, dicoj3, dicoj4, joueur_a_jouer]
