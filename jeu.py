"""
NOM_MODULE : jeu.py
BUT : Fonctions de jeu
"""

import ressources
import lib


def placer_piece(plateau, piece, coord, id_joueur):
    """
    But : Placer une piece dans la matrice aux coordonnées voulues avec la couleur du joueur correspondante
    Créateurs : Romain, Antonin
    :param plateau: matrice 22x22
    :param piece: matrice
    :param coord: (x, y)
    :param id_joueur: int (1 -> 4)
    :return: None
    """

    nouveau_plateau = plateau
    hauteur_piece = len(piece)
    largeur_piece = len(piece[0])
    x, y = coord[0], coord[1]

    for i in range(hauteur_piece):
        for j in range(largeur_piece):
            if piece[i][j] == 'x':
                nouveau_plateau[x+i][y+j] = str(id_joueur)


def test_chevauchement(plateau, piece, coord):
    """
    But : vérifier qu'il n'y a pas de piece où le joueur veut placer sa pièce ou qu'on ne sort pas de la grille
    Créateurs : Antonin et Romain
    :param plateau : matrice 22x22
    :param piece : matrice
    :param coord: (x, y) int
    :return: Booléen
    """
    hauteur_piece = len(piece)
    largeur_piece = len(piece[0])
    x, y = coord[0], coord[1]
    for i in range(hauteur_piece):
        for j in range(largeur_piece):
            if piece[i][j] == 'x':
                if x + i > 21 or y + j > 21:  # Sortie du plateau
                    return False
                elif plateau[x+i][y+j] != ' ':  # Collision
                    return False
    return True


def test_coup_legal(plateau, piece, coord, id_joueur):
    """
    But : Détecter si le joueur fait un coup légal en plaçant sa pièce (coins et côtés)
    Créateurs : Antonin, Romain
    :param plateau: matrice 22x22
    :param piece: matrice
    :param coord: (x, y) int
    :param id_joueur: int (1 -> 4)
    :return: Booléen
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

    # Il faut au moins un coin pour que le coup soit valide
    if compteur_coin > 0:
        return True

    return False


def peut_jouer(plateau, liste_piece_id, id_joueur):
    """
    But : Savoir si un joueur peut jouer en parcourant toutes les cases vides et en essayant toutes les pièces à
    disposition
    Créateur : Romain
    :param plateau: matrice 22x22
    :param liste_piece_id: matrice
    :param id_joueur: int (1 -> 4)
    :return: Booléen
    """

    pieces_du_joueur = []

    if len(liste_piece_id) == 0:  # main vide
        return False
    if len(liste_piece_id) == 21:  # 1er tour
        return True

    # On génère toutes les configurations de pièces possibles
    for piece_id in liste_piece_id:
        config = lib.generate_config_piece(ressources.dico_ref_pieces[piece_id])
        for piece in config:
            pieces_du_joueur.append(piece)

    # Parcours des cases et vérifie si la case est vide
    for x in range(1, 21):
        for y in range(1, 21):
            if plateau[x][y] == ' ':
                for piece in pieces_du_joueur:
                    if test_chevauchement(plateau, piece, (x, y)) and test_coup_legal(plateau, piece, (x, y), id_joueur):
                        return True
    return False


def initialisation():
    """
    But : Initialiser une partie telle que
        partie['plateau'] = grille de jeu
        partie['joueurs'] = dictionnaire des joueurs tel que
                joueur['nom'] = nom du joueur
                joueur['main'] = main du joueur
                joueur['dernier_coup'] = id de la dernière pièce posée
    Créateur : Romain
    :return : dict
    """

    partie = {'plateau': ressources.plateau_initial}

    joueurs = {}
    print(f'CREATION DES JOUEURS :')
    for k in range(4):
        dico_joueur = {'nom': input(f'Saisir le nom du joueur {k+1} : '),
                       'main': [k for k in range(1, 22)],
                       'dernier_coup': 0}
        joueurs[k+1] = dico_joueur
    partie['joueurs'] = joueurs
    return partie


def initialisation2j():
    """
    But : Initialiser une partie pour 2 joueurs telle que
        partie['plateau'] = grille de jeu
        partie['joueurs'] = dictionnaire des joueurs tel que
                joueur['nom'] = nom du joueur
                joueur['main'] = main du joueur
                joueur['dernier_coup'] = id de la dernière pièce posée
    Créateur : Romain
    :return : dict
    """

    partie = {'plateau': ressources.plateau_initial}

    joueurs = {}
    print(f'CREATION DES JOUEURS :')

    nom_j1 = input(f'Saisir le nom du joueur 1 : ')
    joueurs[1] = {'nom': nom_j1,
               'main': [k for k in range(1, 22)],
               'dernier_coup': 0}
    joueurs[3] = {'nom': nom_j1,
               'main': [k for k in range(1, 22)],
               'dernier_coup': 0}

    nom_j2 = input(f'Saisir le nom du joueur 2 : ')
    joueurs[2] = {'nom': nom_j2,
               'main': [k for k in range(1, 22)],
               'dernier_coup': 0}
    joueurs[4] = {'nom': nom_j2,
               'main': [k for k in range(1, 22)],
               'dernier_coup': 0}

    partie['joueurs'] = joueurs
    return partie


def score(partie, nbr_joueurs):
    """
    But : Calculer le score de chaque joueur à la fin du jeu
    Créateur : Antonin
    :param partie : dict
    :return: liste telle que [(score 1er, id 1er), (score 2eme, id 2eme) ...]
    """

    # Parcours du plateau et on ajoute un pour chaque carré posé
    plateau = partie['plateau']
    scores = [[-89, k] for k in range(1, 5)]
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if plateau[i][j] == '1':
                scores[0][0] += 1
            elif plateau[i][j] == '2':
                scores[1][0] += 1
            elif plateau[i][j] == '3':
                scores[2][0] += 1
            elif plateau[i][j] == '4':
                scores[3][0] += 1

    # Score modifié selon condition
    joueurs = partie['joueurs']
    for k in range(1, 5):
        if len(joueurs[k]['main']) == 0:
            if joueurs[k]['dernier_coup'] == 1:
                scores[k - 1][0] = 20
            else:
                scores[k - 1][0] = 15

    if nbr_joueurs == 2:
        scores = [(scores[0][0] + scores[2][0], scores[0][1]), (scores[1][0] + scores[3][0], scores[1][1])]
    # Tri du tableau
    scores.sort(reverse=True)
    return scores
