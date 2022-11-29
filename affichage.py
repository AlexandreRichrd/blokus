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
    for ligne in plateau:
        affichage = ''
        for x in ligne:
            if x == '1':
                affichage = affichage + (Back.BLUE + '1')
                affichage = affichage + (Back.BLUE + ' ')
            if x == '2':
                affichage = affichage + (Back.RED + '2')
                affichage = affichage + (Back.RED + ' ')
            if x == '3':
                affichage = affichage + (Back.GREEN + '3')
                affichage = affichage + (Back.GREEN + ' ')
            if x == '4':
                affichage = affichage + (Back.YELLOW + '4')
                affichage = affichage + (Back.YELLOW + ' ')
            if x == ' ':
                affichage = affichage + (Back.WHITE + " ")
                affichage = affichage + (Back.WHITE + " ")
            if x == '':
                affichage = affichage + (Back.BLACK + '')
                affichage = affichage + (Back.BLACK + '*')
        print(affichage)
    print(Back.RESET)
    print(Fore.RESET)
    return
