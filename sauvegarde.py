"""
NOM_MODULE : sauvegarde.py
BUT : Sauvegarder les parties et reprendre une partie selon une sauvegarde placées en ../sauvegardes
"""

import time
import os


def save(partie):
    """ Entrée : partie: dict (cf jeu.py)
    But : Ecriture d'un fichier 'blokus_date_heure.txt' contenant le plateau puis les informations des joueurs
    Sortie : None
    Créateur : Romain """
    
    # Création du nom du fichier tel que "blokus_YYYYMMDD_HHMM.txt
    parent = os.getcwd()
    os.chdir(parent + '/sauvegardes')
    date = time.localtime(time.time())
    nom_fichier = 'blokus_' \
                  + str(date.tm_year) + str(date.tm_mon) + str(date.tm_mday) + '_' \
                  + str(date.tm_hour) + str(date.tm_min) \
                  + '.txt'

    # Récupération des informations à sauvegarder
    plateau = partie['plateau']
    joueurs = partie['joueurs']

    fichier = open(nom_fichier, 'w')

    # Ecriture des informations dans le fichier de sauvegarde
    for lignes in plateau:
        ligne = ''
        for case in lignes:
            ligne = ligne + case
        ligne = ligne + '\n'
        fichier.write(ligne)

    # Ecriture des informations concernant les joueurs comme "Nom Derniere_piece Main"
    for k in range(1, 5):
        ligne = joueurs[k]['nom']
        ligne += ' ' + str(joueurs[k]['dernier_coup'])
        for piece_id in joueurs[k]['main']:
            ligne += ' ' + str(piece_id)
        ligne = ligne + ' ' + '\n'
        fichier.write(ligne)

    # Fermeture du fichier
    fichier.close()
    os.chdir(parent)


def read_save(nom_fichier):
    """
    Entrée : nom_fichier: str
    But : lire le fichier et en déduire le dictionnaire de la partie
    Sortie : partie (dict), compteur (int)
    Créateur : Romain
    """

    # Ouverture du fichier
    parent = os.getcwd()
    os.chdir(parent + '/sauvegardes')
    fichier = open(nom_fichier, 'r')
    lignes = fichier.readlines()

    partie = {}
    plateau = []

    # Déduction du tableau
    for k in range(22):
        ligne = []
        for x in lignes[k]:
            if x != '\n':
                ligne.append(x)
        plateau.append(ligne)
    partie['plateau'] = plateau

    # Déduction des infos des joueurs
    joueurs = {}
    compteurs = []
    for k in range(22, 26):
        datas_joueur = lignes[k][:-1].split(" ")
        print(datas_joueur)
        joueurs[k+1 - 22] = {'nom': datas_joueur[0],
                             'dernier_coup': int(datas_joueur[1]),
                             'main': [int(x) for x in datas_joueur[2:]]}
        compteurs.append(len(datas_joueur[2:]))
    partie['joueurs'] = joueurs

    # Déduction du compteur en fonction de la taille de la main des joueurs
    compteur = 21 - min(compteurs)

    if joueurs[4]['nom'] == joueurs[2]['nom'] and joueurs[1]['nom'] == joueurs[3]['nom']:
        nbr_joueurs = 2
    else:
        nbr_joueurs = 4

    os.chdir(parent)

    return partie, compteur, nbr_joueurs
