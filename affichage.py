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
                affichage = affichage + (Back.BLUE + ' 1 ')
            if x == '2':
                affichage = affichage + (Back.RED + ' 2 ')
            if x == '3':
                affichage = affichage + (Back.GREEN + ' 3 ')
            if x == '4':
                affichage = affichage + (Back.YELLOW + ' 4 ')
            if x == ' ':
                affichage = affichage + (Back.WHITE + "   ")
            if x == '*':
                affichage = affichage + (Back.BLACK + Fore.WHITE + ' * ')
        print(affichage + Back.RESET + Fore.RESET)
    print(Back.RESET)
    print(Fore.RESET)
    return
