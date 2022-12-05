import dict_pieces
import jeu
import affichage
import lib
import sauvegarde
import os


def debug(partie, joueur_a_jouer):
    print('\n\n\n#########################################################')
    print('                         DEBUG')
    print('#########################################################')

    plateau = partie['plateau']
    joueurs = partie['joueurs']
    joueurs_r = partie['joueurs_restants']

    affichage.afficher_plateau_couleur(plateau)
    print(f'Joueurs : {joueurs}')
    print(f'Joueurs restants : {joueurs_r}')

    print(f"C'est le tour du joueur {joueur_a_jouer}")
    print('#########################################################\n\n')






if __name__ == "__main__":

    affichage.titre_blokus()

    choix_fait = False
    while not choix_fait:
        affichage.menu()
        choix = input('Votre choix : ')
        if choix == '1':
            print('\n> Nouvelle partie')
            partie = jeu.initialisation()
            choix_fait = True
        elif choix == '2':
            affichage.menu_sauvegarde_dispos(os.listdir(os.getcwd() + '/sauvegardes'))
            nom_fichier = input('Quel fichier voulez vous ? ')
            if nom_fichier not in [nom[:-4] for nom in os.listdir(os.getcwd() + '/sauvegardes')]:
                print("ATTENTION : Ce n'est pas un nom de fichier valide.\n")
                choix_fait = False

            else:
                partie = sauvegarde.read_save(nom_fichier + '.txt')
                choix_fait = True
        elif choix == '3':
            print('Ciao, bye !')
            choix_fait = True
            exit()
        else:
            print(f'\n\nATTENTION : {choix} n\'est pas une entrée valide.')

    compteur_tour = 1
    joueur_a_jouer = 1
    print(f"\n> TOUR N° {compteur_tour}")

    while len(partie['joueurs_restants']) > 1:

        joueur = partie['joueurs'][joueur_a_jouer]
        print(f"\nC'est au tour du joueur {joueur_a_jouer} : {joueur['nom']} !")
        affichage.afficher_plateau_couleur(partie['plateau'])

        # Boucle pour jouer un coup
        coup_legal = False
        while not coup_legal:
            print(f"Voici votre main :")
            affichage.afficher_liste_pieces([dict_pieces.dict[k] for k in joueur['main']], joueur['main'],
                                            joueur_a_jouer)

            choix_piece = False
            while not choix_piece:
                piece_choisie_id = int(input(f"Que voulez vous joueur ? Numéro : "))
                if piece_choisie_id in joueur['main']:
                    choix_piece = True

            print(f"Voici les configurations de la pièces {piece_choisie_id} :")
            configurations = lib.generate_config_piece(dict_pieces.dict[piece_choisie_id])
            affichage.afficher_liste_pieces(configurations, range(1, len(configurations) + 1), joueur_a_jouer)

            choix_config = False
            while not choix_config:
                config_choisie = int(input(f"Que voulez vous joueur ? Numéro : "))
                if config_choisie in range(1, len(configurations) + 1):
                    choix_config = True

            piece_choisie = configurations[config_choisie - 1]

            # Première pièce du joueur
            if len(joueur['main']) == 21:
                if joueur_a_jouer == 1:
                    pos_x, pos_y = 1, 1
                elif joueur_a_jouer == 2:
                    pos_x, pos_y = 1, 20 - len(piece_choisie[0]) + 1
                elif joueur_a_jouer == 3:
                    pos_x, pos_y = 20 - len(piece_choisie[0]) + 1, 20
                else:
                    pos_x, pos_y = 20 - len(piece_choisie[0]) + 1, 1
                print(pos_x, pos_y)
                if piece_choisie[0][0] == 'x':
                    coup_legal = True

            # Si ce n'est pas la première pièce...
            else:

                choix_position = input(f"Où voulez vous placer la pièce {piece_choisie_id} ? (colonne ligne) ")
                [pos_y, pos_x] = [int(x) for x in choix_position.split(' ')]


                #print(jeu.test_coup_legal(partie['plateau'], piece_choisie, (pos_x, pos_y), joueur_a_jouer))
                #print(jeu.test_chevauchement(partie['plateau'], piece_choisie, (pos_x, pos_y)))

                coup_legal = jeu.test_coup_legal(partie['plateau'], piece_choisie, (pos_x, pos_y), joueur_a_jouer) and jeu.test_chevauchement(partie['plateau'], piece_choisie, (pos_x, pos_y))
                if not coup_legal:
                    print(f'Attention ce coup est illégal.')
                    affichage.afficher_plateau_couleur(partie['plateau'])

        jeu.placer_piece(partie['plateau'], piece_choisie, (pos_x, pos_y), joueur_a_jouer)
        joueur['main'].remove(piece_choisie_id)
        # affichage.afficher_plateau(partie['plateau'])

        joueur_a_jouer = partie['joueurs_restants'][(joueur_a_jouer + 1) % (len(partie['joueurs_restants'])) - 1]

        if joueur_a_jouer == partie['joueurs_restants'][0]:
            compteur_tour += 1

            print(f"\n> TOUR N° {compteur_tour}")

            choix_sauvegarde = False
            while not choix_sauvegarde:
                affichage.menu_sauvegarde()
                sauvegarde_choisie = input(f"Que voulez vous faire ? ")
                if sauvegarde_choisie in ['1', 'O', 'Y']:
                    choix_sauvegarde = True
                elif sauvegarde_choisie in ['2', 'N']:
                    choix_sauvegarde = True
                    sauvegarde.save(partie)
                    exit()

    print('> Fin de partie - SCORES :')
    scores = jeu.score(partie['plateau'])

    for k in range(4):
        print(f"    >{k+1}. {partie['joueurs'][scores[k][1]]['nom']} - {scores[k][1]} pts ")



"""if not jeu.peut_jouer(partie['plateau'], joueur['main'], joueur_a_jouer):
            print(f'le joueur {joueur_a_jouer} est éliminé')
            partie['joueurs_restants'].remove(joueur_a_jouer)"""

''' #Attribution des pièces à chaque joueurs
    tailleDico = len(dict_pieces.dict)
    dicoJoueur = dict_pieces.dict.copy()

    # for clefs in range(len(dict)):
    

        # for ligne in dicoJoueur[1]:
        #     for case in ligne: 
        #         if case == 'x':
        #             case = str(joueur)

    #VARIABLES
    #nbTour
    #
    def afficherPiece(matrix):
        for cpt in range(1, len(matrix)):
            for j in range(len(matrix[cpt])):
                for k in range(len(matrix[cpt][j])):
                    print(matrix[cpt][j][k], end='')
                print()

    def AfficherPiecesJoueur(joueur, dicojoueur):
        print(dicoJoueur)
        for i in range(len(dicojoueur[joueur][1])):
            # print(dicojoueur[joueur][1][i])
            print('Pièce n°', i+1)
            afficherPiece(dicojoueur[joueur][1][i])


    def jouer(joueur, dicoJoueur):
        #Afficher les pieces disponibles
        print('Joueur ', joueur, ' à toi de jouer !')
        print('Voici les pièces disponibles :')
        AfficherPiecesJoueur(joueur, dicoJoueur)


    def checkStatusGame(nbJoueursRestants):
        if nbJoueursRestants > 1:
            return True
        else:
            return False

    game = True
    choix_fait = False
    nb_Tours = 0
    nb_joueurs_restants = 4
    dict_joueurs= {1: ('joueur1', []), 2: ('joueur2', []), 3: ('joueur3', []), 4: ('joueur4', [])}
    while game:
        if not choix_fait:
            print('-------------------')
            print('Jeu du Blokus')
            print('-------------------')

        #-------------Debut du Jeu----------------

        #print plateau

        for i in range(nb_joueurs_restants):
            #game = checkStatusGame(nb_joueurs_restants)
            #jouer(joueur, nbTours, plateau)
            jouer(i+1, dict_joueurs)
            print('Joueur', i+1)

        nb_Tours += 1
        #sauvegarde
        print('Souhaitez-vous sauvegarder la partie ? (Y/yes = oui)')
        choix = input('Votre choix : ')
        if choix == 'Y' or choix == 'yes' or choix == 'y' or choix == 'Yes':
            print('sauvegarde')
        else:
            print('pas de sauvegarde')
        

        
            

    
        

                
                   
        

    # BOUCLE DE JEU
'''
