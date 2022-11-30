# Gestion de l'affichage console
from colorama import Back, Fore


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
            else:
                affichage += '    '
        affichage += '\n'
    print(affichage)


def afficher_plateau_couleur(plateau):
    """
    Entrée : plateau, une matrice 22x22
    But : Afficher le plateau en couleur dans la console
    Sortie : None
    Créateurs : Valentin et Romain
    """
    affichage = Fore.BLACK
    for ligne in plateau:
        for x in ligne:
            if x == '1':
                affichage += Back.BLUE + ' 1  ' + Back.RESET
            elif x == '2':
                affichage += Back.RED + ' 2  ' + Back.RESET
            elif x == '3':
                affichage += Back.GREEN + ' 3  ' + Back.RESET
            elif x == '4':
                affichage += Back.YELLOW + ' 4  ' + Back.RESET
            elif x == ' ':
                affichage += Back.WHITE + '    ' + Back.RESET
        affichage += '\n'
    print(affichage + Back.RESET + Fore.RESET)
