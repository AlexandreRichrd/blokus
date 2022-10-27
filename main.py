

from lib import afficher_matrix
import sauvegarde
import dict_pieces

listesJoueurs = [1, 2, 3, 4]
plateauInitial = [['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',]]


if __name__ == "__main__":
   
    # INITIALISATION
    plateau = plateauInitial
    #affichage.afficher_plateau(plateau)

    
    #Attribution des pièces à chaque joueurs 
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
    dict_joueurs= {1: ('joueur1',[]), 2: ('joueur2',[]), 3: ('joueur3',[]), 4: ('joueur4',[])}
    while game:
        if not choix_fait:
            print('-------------------')
            print('Jeu du Blokus')
            print('-------------------')
        choix_fait == False
        while not choix_fait:
            print('1. Nouvelle partie')
            print('2. Charger une partie')
            print('3. Quitter')
            choix = input('Votre choix : ')
            if choix == '1':
                print('nouvelle partie')
                for i in range(1, 5):
                    dict_joueurs[i][1].append(dict_pieces.dict)
                    print('joueur ', i, ' : ', dict_joueurs[i])
                print(dict_joueurs)
                choix_fait = True
            if choix == '2':
                print('chargement')
                choix_fait = True
            if choix == '3':
                print('Au revoir')
                choix_fait = True
                game = False
            elif choix != '1' and choix != '2' and choix != '3': 
                print('\n'*100)
                print(choix)
                print('Choix incorrect')
        #-------------Debut du Jeu----------------

        #print plateau

        for i in range(nb_joueurs_restants):
            #game = checkStatusGame(nb_joueurs_restants)
            #jouer(joueur, nbTours, plateau)
            jouer(i+1,dict_joueurs)
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
