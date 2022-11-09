# Fonctions appelées dans la boucle principale du jeu


def placer_piece(plateau, piece, coord, id_joueur):
    """
    Entrée : plateau : une matrice 22x22, piece : la matrice d'une piece, coord : (x,y), id_joueur : entier (1 à 4)
    But : Placer une piece dans la matrice aux coordonnées voulues avec la couleur du joueur correspondante
    Sortie : le plateau mis à jour
    Créateurs : Romain, Antonin
    """

    nouveau_plateau = plateau
    hauteur_piece = len(piece)
    largeur_piece = len(piece[0])
    x, y = coord[0], coord[1]

    for i in range(hauteur_piece):
        for j in range(largeur_piece):
            if piece[i][j] == 'x':
                nouveau_plateau[x+i][y+j] = str(id_joueur)
    return nouveau_plateau


def test_chevauchement(plateau, piece, coord):
    """
    Entrée : plateau : matrice 22x22, piece : matrice, coord : tuple (x,y)
    But : vérifier qu'il n'y a pas de piece où le joueur veut placer sa pièce ou qu'on ne sort pas de la grille
    Sortie : un booléen
    Créateurs : Antonin, Romain
    """
    hauteur_piece = len(piece)
    largeur_piece = len(piece[0])
    x, y = coord[0], coord[1]
    for i in range(hauteur_piece):
        for j in range(largeur_piece):
            if piece[i][j] == 'x':
                if plateau[x+i][y+j] != ' ':
                    return False
    return True


def test_coup_legal(plateau, piece, coord, id_joueur):
    """
    Entrée : plateau : une matrice 22x22, piece : la matrice d'une piece, coord : (x,y), id_joueur : entier (1 à 4).
    But : Détecter si le joueur fait un coup légal en plaçant sa pièce.
    Sortie : Booléen.
    Créateurs : Antonin, Romain
    """
    hauteur_piece = len(piece)
    largeur_piece = len(piece[0])
    x, y = coord[0], coord[1]

    compteur_coin = 0
    for i in range(hauteur_piece):
        for j in range(largeur_piece):
            if piece[i][j] == 'x':
                # Detection d'un bord adjacent de même couleur :
                if plateau[x + i - 1][y + j] == str(id_joueur):
                    return False
                if plateau[x + i + 1][y + j] == str(id_joueur):
                    return False
                if plateau[x + i][y + j - 1] == str(id_joueur):
                    return False
                if plateau[x + i][y + j + 1] == str(id_joueur):
                    return False

                # Detection d'un coin :
                if plateau[x + i - 1][y + j - 1] == str(id_joueur):
                    compteur_coin += 1
                if plateau[x + i + 1][y + j - 1] == str(id_joueur):
                    compteur_coin += 1
                if plateau[x + i - 1][y + j + 1] == str(id_joueur):
                    compteur_coin += 1
                if plateau[x + i + 1][y + j + 1] == str(id_joueur):
                    compteur_coin += 1

    if compteur_coin > 0:
        return True

    return False




