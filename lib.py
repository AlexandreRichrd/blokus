import numpy as np
import dict_pieces
import dict_config


def generate_config(dict1):
  '''
  Entree: dictonnaire pieces et dictionnaire vierge
  But: Generer les config de pieces
  Sortie: Dictionnaire avec les configs des pieces
  '''
  dict2 = {}
  for i in range(1, len(dict1)+1):
    # print('test: ', i)
    # print(len(dict1[i]))
    if((i != 4)):
      if len(dict1[i]) > 1:
        list_combi = []
        list_combi2 = []
        for j in range(4):
          # print("j: ", j)
          m = rotate_matrix(dict1[i], j+1)
          # print('m: ', m)
          list_combi.append(m)
        
        m = np.flip(dict1[i], 1)
        list_combi.append(m)
        # print('m flip: ', m)
        for k in range(len(list_combi)):
          list_combi2.append(list_combi[k].tolist())
        # print('list: ', list_combi2)
        list_combi2.append(dict1[i])
        dict2[i] = (dict1[i], remove_double(list_combi2)) # ne pas oublier la matrice de base
        # print('dict2[', i, ']: ', dict2[i])
      elif len(dict1[i]) == 1:
        dict2[i] = (dict1[i], dict1[i])
    elif i == 4:
      dict2[i] = (dict1[i], [[['x', 'x'], ['x', '']], [['x', ''], ['x', 'x']], [['x', 'x'], ['', 'x']], [['', 'x'], ['x', 'x']]]) 
    # elif i == 9:
    #   print('test')
    #   dict2[i] = (dict1[i], [[['x', 'x', ''], ['', 'x', 'x']], [['', '', 'x'], ['x', 'x', 'x'], ['x', '', '']], [['', 'x', 'x'], ['x', 'x', '']],[['x', '', ''], ['x', 'x', 'x'], ['', '', 'x']]])
  return dict2


def remove_double(list):
  '''
  Entree: Liste avec des doublons
  But: Enlever les doublons
  Sortie: Liste sans doublons
  '''
  list2 = []
  for i in list:
    if i not in list2:
      list2.append(i)
  return list2


def rotate_matrix(matrix, rotnb):
  '''
  Entree: la matrice à tourner
  But: On fait une rotation de la matrice à 90°
  Sortie: La matrice s'est faite retourner
  '''
  
  matrix = np.rot90(matrix, rotnb, (0,1))
  return matrix




def afficher_matrix(mat):
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      print(mat[i][j], end='')  
    print("")
  
dict_pieces.dict_config = generate_config(dict_pieces.dict)

afficher_matrix(dict_pieces.dict_config[2][1][0])

print('affichage')
for i in range(1, len(dict_pieces.dict_config)+1):
  print('------------------')
  print('Pièce ', i)
  print('------------------')
  print('config de base: ')
  afficher_matrix(dict_pieces.dict_config[i][0])
  for j in range(len(dict_pieces.dict_config[i][1])):
    print('Config ', j)
    afficher_matrix(dict_pieces.dict_config[i][1][j])
    print('')


print(dict_pieces.dict_config[19][0])