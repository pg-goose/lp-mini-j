i. 0                    NB. generar vector buit. resultat: 
# i. 0                  NB. mida de vector buit. resultat: 0
1 2 + 1 2 3             NB. longitud diferent, error. resultat: length error
2 | 1 2 3               NB. residu vector. resultat: 1 0 1
0 ^ 0                   NB. zero a zero. resultat: 1
1 2 3 > 2               NB. comparació vector amb escalar. resultat: 0 0 1
1 3 5 = 1 2 1           NB. comparació vector a vector. resultat: 1 0 0
i. _3                   NB. argument negatiu en i. resultat:
_1 { 1 2 3              NB. accedir a element amb índex negatiu. resultat: 3
3 { 1 2 3               NB. índex fora de límits. resultat: index error
1 0 1 # 1 2             NB. màscara més llarga que vector, error. resultat: length error
1 0 1 # 1 2 3 4         NB. filtre amb màscara de longitud 3 i dades de longitud 4, error. resultat: length error
+/ i. 0                 NB. suma de vector buit amb fold. resultat: 0
7 |~ 2                  NB. flip de residu. resultat: 1
# 1                     NB. mida d’un escalar. resultat: 1

comp =: +/ @: *: @: i.
comp 3                                        NB. suma dels quadrats de 0 1 2. resultat: 5

comp =: 0 = ] @: 2 | ]
comp i. 6                                     NB. màscara de nombres parells de 0..5. resultat: 1 0 1 0 1 0

comp =: +/ @: 0 = ] @: 2 | ] @: i.
comp 6                                        NB. suma de booleans per nombres parells de 0..5. resultat: 3