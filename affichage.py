"""
NOM_MODULE : affichage.py
BUT : Gérer l'affichage en couleur dans la console et l'affichage des menus
"""
from colorama import Back, Fore
import ressources


def afficher_plateau(plateau):
    """
    Entrée : plateau: matrice 22x22
    But : Afficher proprement dans la console le plateau de jeu
    Sortie : None
    Créateur : Romain
    """
    for ligne in plateau:
        print(ligne)


def afficher_piece(piece, joueur):
    """
    Entree : piece: matrice, joueur: int
    But : Afficher la piece en couleur dans la console
    Sortie : None
    Créateur : Alexandre
    """
    affichage = ''
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 'x':
                if joueur == 1:
                    affichage += Back.BLUE + '    ' + Back.RESET
                elif joueur == 2:
                    affichage += Back.YELLOW + '    ' + Back.RESET
                elif joueur == 3:
                    affichage += Back.RED + '    ' + Back.RESET
                elif joueur == 4:
                    affichage += Back.GREEN + '    ' + Back.RESET
            else:
                affichage += '    '
        affichage += '\n'
    print(affichage)


def afficher_plateau_couleur(plateau):
    """
    :param: plateau: matrice 22x22
    :return: None
    But : Afficher le plateau en couleur dans la console
    Créateurs : Valentin et Romain
    """
    affichage = '   '
    for k in range(1, 21):
        affichage += str(k) + ' ' * (4 - len(str(k)))  # Aide n° colonne
    affichage += '\n'
    compteur = 1
    for ligne in plateau[1:21]:
        affichage += ' ' * (2 - len(str(compteur))) + str(compteur) + ' '  # Aide n° ligne
        for x in ligne:
            if x == '1':
                affichage += Back.BLUE + '    ' + Back.RESET
            elif x == '2':
                affichage += Back.YELLOW + '    ' + Back.RESET
            elif x == '3':
                affichage += Back.RED + '    ' + Back.RESET
            elif x == '4':
                affichage += Back.GREEN + '    ' + Back.RESET
            elif x == ' ':
                affichage += Back.WHITE + '    ' + Back.RESET
        affichage += ' ' + str(compteur) + ' ' * (2 - len(str(compteur))) + '\n'  # Aide n° ligne
        compteur += 1
    affichage += '   '
    for k in range(1, 21):
        affichage += str(k) + ' ' * (4 - len(str(k)))  # Aide n° colonne
    print(affichage + '\n' + Back.RESET + Fore.RESET)


def afficher_liste_pieces(liste_piece, liste_piece_id, joueur_id):
    """
    But : Afficher les pièces sur une ligne et numérotées dans la console
    Créateur: Romain
    :param liste_piece: list
    :param liste_piece_id: int
    :param joueur_id: int
    :return:
    """

    affichage_numero = ''
    compteur = 0
    for numero in liste_piece_id:
        affichage_numero += str(numero) + ' ' * (4 - len(str(numero))) + '    ' * (len(liste_piece[compteur][0]) - 1) + '    '
        compteur += 1

    n = max(len(piece) for piece in liste_piece)
    affichage = ''
    for hauteur in range(n):
        for indice_piece in range(len(liste_piece)):
            for largeur_piece in range(len(liste_piece[indice_piece][0])):
                if hauteur >= len(liste_piece[indice_piece]):
                    affichage += '    '
                elif liste_piece[indice_piece][hauteur][largeur_piece] == 'x':
                    if joueur_id == 1:
                        affichage += Back.BLUE + '    ' + Back.RESET
                    elif joueur_id == 2:
                        affichage += Back.YELLOW + '    ' + Back.RESET
                    elif joueur_id == 3:
                        affichage += Back.RED + '    ' + Back.RESET
                    elif joueur_id == 4:
                        affichage += Back.GREEN + '    ' + Back.RESET
                else:
                    affichage += '    '
            affichage += '    '
        affichage += '\n'

    print(affichage_numero + '\n' + affichage)


def titre_blokus():
    """
    But : Affiche le BLOKUS en ASCII
    Créateur : Romain
    :return:
    """
    print(ressources.blokus)


def menu():
    """
    But : Affiche le menu principal
    Créateur : Romain
    :return:
    """
    print('> MENU PRINCIPAL')
    print('     > 1. Nouvelle partie 4 joueurs')
    print('     > 2. Nouvelle partie 2 joueurs')
    print('     > 3. Charger une partie')
    print('     > 4. Quitter')


def menu_sauvegarde():
    """
        But : Affiche le menu de sauvegarde
        Créateur : Romain
        :return:
        """
    print('> SAUVEGARDE ?')
    print('     > 1. Non')
    print('     > 2. Oui')


def menu_sauvegarde_dispos(liste):
    """
    But : Affiche les fichiers de sauvegarde disponibles
    Créateur : Romain
    :return:
    """
    print('> SAUVEGARDE(S) DISPONIBLE(S) :')
    for k in liste:
        print(f'    > {k[:-4]}')


def afficher_scores(partie, scores):
    """
    But : Afficher les résultats
    Créateur : Romain
    :param partie: dict
    :param scores : dico des scores trié avec l'id du joueur
    :return: None
    """
    for k in range(4):
        print(f"    > {k+1}. {partie['joueurs'][scores[k][1]]['nom']} avec {scores[k][0]} pts ")