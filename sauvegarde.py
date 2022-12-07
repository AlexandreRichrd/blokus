# Gestion des fonctions de sauvegarde
# Écriture d'un fichier de sauvegarde
# Lecture d'un fichier de sauvegarde

import time
import os


def save(partie):
    """ Entrée : plateau, une matrice 22x22 ; les dictionnaires des joueurs
    But : Ecriture d'un fichier 'blokus_date_heure.txt' contenant le plateau puis les cles des pièces restantes
     des joueurs
    Sortie : None
    Créateur : Romain """
    
    # Création du nom du fichier

    os.chdir(os.getcwd() + '/sauvegardes')
    date = time.localtime(time.time())
    nom_fichier = 'blokus_' + str(date.tm_year) + str(date.tm_mon) + str(date.tm_mday) + '_' + str(date.tm_hour) + str(date.tm_min) + '.txt'

    plateau = partie['plateau']
    joueurs = partie['joueurs']

    fichier = open(nom_fichier, 'w')  # Ouverture du fichier
    
    for lignes in plateau:  # Ecriture dans le fichier du plateau
        ligne = ''
        for case in lignes:
            ligne = ligne + case
        ligne = ligne + '\n'
        fichier.write(ligne)

    # Ecriture dans le fichier des dicos des joueurs
    for k in range(1, 5):
        ligne = joueurs[k]['nom']
        ligne += ' ' + str(joueurs[k]['dernier_coup'])
        for piece_id in joueurs[k]['main']:
            ligne += ' ' + str(piece_id)
        ligne = ligne + ' ' + '\n'
        fichier.write(ligne)

    fichier.close()  # Fermeture du fichier


def read_save(nom_fichier):
    """
    Entrée : nom_fichier, str
    But : lire le fichier, en déduire le joueur qui doit jouer, les dictionnaires des joueurs, le plateau
    Sortie : une liste [plateau, dicoj1, dicoj2, dicoj3, dicoj4, j_suivant]
    Créateur : Romain
    """
    os.chdir(os.getcwd() + '/sauvegardes')

    partie = {}

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

    partie['plateau'] = plateau

    joueurs = {}
    compteurs = []
    for k in range(22, 26):
        datas_joueur = lignes[k][:-1].split(" ")
        joueurs[k+1 - 22] = {'nom': datas_joueur[0],
                             'dernier_coup' : int(datas_joueur[1]),
                             'main': [int(x) for x in datas_joueur[2:]]}
        compteurs.append(len(datas_joueur[2:]))
    partie['joueurs'] = joueurs
    compteur = 21 - min(compteurs)
    return partie, compteur
