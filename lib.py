import numpy as np
import dict_pieces


def generate_config(dict1):
  '''
  Entree: dictonnaire pieces et dictionnaire vierge
  But: Generer les config de pieces
  Sortie: Dictionnaire avec les configs des pieces
  '''
  dict2 = {}
  for i in range(1, len(dict1)+1):
    print('test: ', i)
    print(len(dict1[i]))
    if len(dict1[i]) > 1:
      list_combi = []
      for j in range(4):
        print("j: ", j)
        m = rotate_matrix(dict1[i], j+1)
        print('m: ', m)
        list_combi.append(m)
      
      m = np.flip(dict1[i], 1)
      list_combi.append(m)
      print(list_combi)
      dict2[i] = (dict1[i], (set(list_combi))) # ne pas oublier la matrice de base
    elif len(dict1[i]) == 1:
      dict2[i] = (dict1[i], dict1[i])
    
  return dict2



def rotate_matrix(matrix, rotnb):
  '''
  Entree: la matrice à tourner
  But: On fait une rotation de la matrice à 90°
  Sortie: La matrice s'est faite retourner
  '''
  for i in range(rotnb):
    matrix = np.rot90(matrix)
  return matrix


def afficher_matrix(mat):
  for i in range(len(mat)):
    for j in range(len(mat)):
      print(mat[i][j], end='')
    print("")
  


print(generate_config(dict_pieces.dict))