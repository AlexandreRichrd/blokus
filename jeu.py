# Fonctions appelées dans la boucle principale du jeu

# /!\ A FINIR /!\
# Compléter la fonction peut joueur pour tester toutes les configurations d'une pièce et non seulement la
# configuration initiale


import dict_pieces


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


def peut_jouer(plateau, dico_joueurs, id_joueur):
    """
    Entrée : plateau (matrice 22x22), dico_joueurs (construit comme {1:[1,2,3...], 2:[,]...}), id_joueur : int [1:4]
    But : Savoir si un joueur peut jouer en parcourant toutes les cases vides du plateau et en essayant les pièces
    Sortie : Un booléen
    Créateur : Romain
    """
    pieces_du_joueur = dico_joueurs.get(id_joueur)
    for x in range(1, 22):  # Parcours des cases et vérifie si la case est vide
        for y in range(1, 22):
            if plateau[x][y] == 0:

                for piece in pieces_du_joueur:  # Code à compléter pour tester toutes les configurations d'une pièce
                    if test_coup_legal(plateau, piece, (x, y), id_joueur):
                        return True
    return False
