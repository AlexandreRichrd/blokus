"""
main.py
Boucle principal de jeu

Créateurs: Alexandre et Romain
"""

import ressources
import jeu
import affichage
import lib
import sauvegarde
import os

if __name__ == "__main__":

    #  Affichage blokus ASCII
    affichage.titre_blokus()

    # --- MENU PRINCIPAL ---
    choix_menu_princi = False
    while not choix_menu_princi:
        affichage.menu()
        choix = input('Votre choix : ')

        # Nouvelle Partie
        if choix == '1':
            print('\n> Nouvelle partie')
            partie = jeu.initialisation()
            compteur = 0
            choix_menu_princi = True

        # Sauvegarde
        elif choix == '2':
            affichage.menu_sauvegarde_dispos(os.listdir(os.getcwd() + '/sauvegardes'))
            nom_fichier = input('Quel fichier voulez vous ? ')
            joueur_precedent = 4

            if nom_fichier not in [nom[:-4] for nom in os.listdir(os.getcwd() + '/sauvegardes')]:
                print("ATTENTION : Ce n'est pas un nom de fichier valide.\n")
                choix_menu_princi = False

            else:
                partie, compteur = sauvegarde.read_save(nom_fichier + '.txt')
                choix_menu_princi = True

        # Quitter
        elif choix == '3':
            choix_menu_princi = True
            exit()
        else:
            print(f'\n\nATTENTION : {choix} n\'est pas une entrée valide.')

    # variables "globales" de jeu
    compteur_tour = compteur
    joueur_a_jouer = 1
    peut_jouer = [True, True, True, True]
    meme_joueur = False

    # --- BOUCLE DE JEU ---
    game = True
    while game:

        # S'il n'y qu'un seul joueur dans la partie et qu'il ne peut pas jouer, on arrête le jeu
        if meme_joueur and not peut_jouer[joueur_a_jouer-1]:
            game = False

        else:
            joueur = partie['joueurs'][joueur_a_jouer]

            # Si on démarre un nouveau tour, on propose de sauvegarder
            if joueur_a_jouer == 1:
                compteur_tour += 1
                print(f"\n> TOUR N° {compteur_tour}")

                choix_sauvegarde = False
                while not choix_sauvegarde:
                    if compteur_tour == 1:
                        choix_sauvegarde = True
                    else:
                        affichage.menu_sauvegarde()
                        sauvegarde_choisie = input(f"Que voulez vous faire ? ")
                        if sauvegarde_choisie in ['1', 'O', 'Y']:
                            choix_sauvegarde = True
                        elif sauvegarde_choisie in ['2', 'N']:
                            choix_sauvegarde = True
                            sauvegarde.save(partie)
                            exit()

            # Si le joueur peut joueur il joue
            peut_jouer[joueur_a_jouer-1] = peut_jouer[joueur_a_jouer-1] and jeu.peut_jouer(partie['plateau'], joueur['main'], joueur_a_jouer)
            if peut_jouer[joueur_a_jouer-1] or len(joueur['main']) == 21:

                print(f"\nC'est au tour du joueur {joueur_a_jouer} : {joueur['nom']} !")
                affichage.afficher_plateau_couleur(partie['plateau'])

                # Boucle pour jouer un coup
                coup_legal = False
                while not coup_legal:
                    print(f"Voici votre main :")
                    affichage.afficher_liste_pieces([ressources.dico_ref_pieces[k] for k in joueur['main']], joueur['main'],
                                                    joueur_a_jouer)

                    choix_piece = False
                    while not choix_piece:
                        piece_choisie_id = int(input(f"Que voulez vous joueur ? Numéro : "))
                        if piece_choisie_id in joueur['main']:
                            choix_piece = True

                    print(f"Voici les configurations de la pièces {piece_choisie_id} :")
                    configurations = lib.generate_config_piece(ressources.dico_ref_pieces[piece_choisie_id])
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
                        if piece_choisie[0][0] == 'x':
                            coup_legal = True

                    # Si ce n'est pas la première pièce...
                    else:

                        choix_position = input(f"Où voulez vous placer la pièce {piece_choisie_id} ? (colonne ligne) ")
                        [pos_y, pos_x] = [int(x) for x in choix_position.split(' ')]

                        coup_legal = jeu.test_coup_legal(partie['plateau'], piece_choisie, (pos_x, pos_y), joueur_a_jouer) and jeu.test_chevauchement(partie['plateau'], piece_choisie, (pos_x, pos_y))

                        if not coup_legal:
                            print(f'Attention ce coup est illégal.')
                            affichage.afficher_plateau_couleur(partie['plateau'])

                joueur['dernier_coup'] = piece_choisie_id
                jeu.placer_piece(partie['plateau'], piece_choisie, (pos_x, pos_y), joueur_a_jouer)  # On place la pièce
                affichage.afficher_plateau_couleur(partie['plateau'])
                joueur['main'].remove(piece_choisie_id)  # On enlève la pièce de la main du joueur

                joueur_precedent = joueur_a_jouer

            # Si le joueur ne peut pas jouer on modifie la liste peut_jouer
            else:
                peut_jouer[joueur_a_jouer-1] = False

            joueur_a_jouer = joueur_a_jouer % 4 + 1

            if joueur_a_jouer == joueur_precedent:
                meme_joueur = True

    # On compte et affiche les scores
    print('> Fin de partie - SCORES :')
    scores = jeu.score(partie)

    # Affichage des scores
    affichage.afficher_scores(partie, scores)

