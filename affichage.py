# Gestion de l'affichage console
from colorama import Back, Fore
import dict_pieces
import lib


def afficher_plateau(plateau):
    """
    Entrée : plateau, une matrice 22x22
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
    liste_affichage = []
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 'x':
                if joueur == 1:
                    affichage += Back.BLUE + ' 1  ' + Back.RESET
                elif joueur == 2:
                    affichage += Back.RED + ' 2  ' + Back.RESET
                elif joueur == 3:
                    affichage += Back.GREEN + ' 3  ' + Back.RESET
                elif joueur == 4:
                    affichage += Back.YELLOW + ' 4  ' + Back.RESET
                liste_affichage.append(affichage)
            else:
                affichage += '    '
        affichage += '\n'
    print(affichage)
    return liste_affichage


def afficher_plateau_couleur(plateau):
    """
    Entrée : plateau, une matrice 22x22
    But : Afficher le plateau en couleur dans la console
    Sortie : None
    Créateurs : Valentin et Romain
    """
    affichage = ''
    for k in range(1, 21):
        affichage += str(k) + ' ' * (4 - len(str(k)))
    affichage += '\n'
    compteur = 1
    for ligne in plateau[1:21]:
        for x in ligne:
            if x == '1':
                affichage += Back.BLUE + '    ' + Back.RESET
            elif x == '2':
                affichage += Back.RED + '    ' + Back.RESET
            elif x == '3':
                affichage += Back.GREEN + '    ' + Back.RESET
            elif x == '4':
                affichage += Back.YELLOW + '    ' + Back.RESET
            elif x == ' ':
                affichage += Back.WHITE + '    ' + Back.RESET
        affichage += ' ' + str(compteur) + ' ' * (2 - len(str(compteur))) + '\n'
        compteur += 1
    print(affichage + Back.RESET + Fore.RESET)


def afficher_liste_pieces(liste_piece, liste_piece_id, joueur_id):

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
                        affichage += Back.RED + '    ' + Back.RESET
                    elif joueur_id == 3:
                        affichage += Back.GREEN + '    ' + Back.RESET
                    elif joueur_id == 4:
                        affichage += Back.YELLOW + '    ' + Back.RESET
                else:
                    affichage += '    '
            affichage += '    '
        affichage += '\n'

    print(affichage_numero + '\n' + affichage)


def titre_blokus():
    print(' ____  _      ____  _  ___    _  _____ \n'
          '|  _ \| |    / __ \| |/ / |  | |/ ____|\n'
          '| |_) | |   | |  | | \' /| |  | | (___  \n'
          '|  _ <| |   | |  | |  < | |  | |\___ \\ \n'
          '| |_) | |___| |__| | . \| |__| |____) |\n'
          '|____/|______\____/|_|\_\\____/|_____/ )\n')


def menu():
    print('> MENU PRINCIPAL')
    print('     > 1. Nouvelle partie')
    print('     > 2. Charger une partie')
    print('     > 3. Quitter')


def menu_sauvegarde():
    print('> SAUVEGARDE ?')
    print('     > 1. Non')
    print('     > 2. Oui')


def menu_sauvegarde_dispos(liste):
    print('> SAUVEGARDE(S) DISPONIBLE(S) :')
    for k in liste:
        print(f'    > {k[:-4]}')

# afficher_liste_pieces([dict_pieces.dict[k] for k in range(1, 22)], range(1, 22), 1)
