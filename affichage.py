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
    return


def afficher_plateau_couleur(plateau):
    """
    Entrée : plateau, une matrice 22x22
    But : Afficher le plateau en couleur dans la console
    Sortie : None
    Créateur : Valentin
    """
    affichage = ''
    for ligne in plateau:
        for x in ligne:
            if x == '1':
                affichage = affichage + (Back.BLUE + ' 2  ' + Back.RESET)
            if x == '2':
                affichage = affichage + (Back.RED + ' 2  ' + Back.RESET)
            if x == '3':
                affichage = affichage + (Back.GREEN + ' 3  ' + Back.RESET)
            if x == '4':
                affichage = affichage + (Back.YELLOW + ' 4  ' + Back.RESET)
            if x == ' ':
                affichage = affichage + (Back.WHITE + '    ' + Back.RESET)
        affichage = affichage + '\n'
    print(affichage + Back.RESET)
    return None
