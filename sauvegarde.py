# Gestion des fonctions de sauvegarde
# Écriture d'un fichier de sauvegarde
# Lecture d'un fichier de sauvegarde

import time
import dict_pieces


def save(plateau, dicoj1, dicoj2, dicoj3, dicoj4):
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


def read_save(nom_fichier):
    """
    Entrée : nom_fichier, str
    But : lire le fichier, en déduire le joueur qui doit jouer, les dictionnaires des joueurs, le plateau
    Sortie : une liste [plateau, dicoj1, dicoj2, dicoj3, dicoj4, j_suivant]
    Créateur : Romain
    """

    fichier = open(nom_fichier, 'r')
    plateau = []
    lignes = fichier.readlines()

    # Déduction du tableau
    for k in range(22):
        ligne = []
        for x in lignes[k]:
            if x != '\n':
                ligne.append(x)
        plateau.append(ligne)

    # Déduction des dictionnaires des joueurs
    dicoj1, dicoj2, dicoj3, dicoj4 = {}, {}, {}, {}

    for (i, dico) in [(22, dicoj1), (23, dicoj2), (24, dicoj3), (25, dicoj4)]:
        for cle in lignes[i].split(' '):
            if cle != '\n':
                dico[int(cle)] = dict_pieces.dict.get(int(cle))

    fichier.close()

    # Calcul du joueur qui doit jouer
    j_suivant = max([(1, len(dicoj1)), (2, len(dicoj2)), (3, len(dicoj3)), (4, len(dicoj4))], key=lambda t: t[1])[0]

    return [plateau, dicoj1, dicoj2, dicoj3, dicoj4, j_suivant]
