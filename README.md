# AyH-Homeworks

Variables:
F: Cantidad de filas de la matriz.
C: Cantidad de columnas de la matriz.
X_ij = 1 : Cuadro pintado 
X_ij = 0 : Cuadro vacio

Dominio:
N pertenece a dimension 10x10
F = 10
C = 10
FxC = 100
X_ij pertente al dominio {0 , 1}


Restricciones:
N == 100
F == 10
C == 10
Cada 
 COORDS = 
0) FILAS = [4, 2, 7, [3, 4], [7, 2], [7, 2], [3, 4], 7, 2, 4]
COLUMNAS = [4, 8, 10, [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], 6, [2, 2], 4, 2]
for para buscar elementos de tipo entero dentro del array y si pilla un objeto que lo salte
 si type(columna[i]) == object:
    skip o continue
 si el columna[i] == 10:
    pintamos toda la columna - 1
    posicion = i = 8

    columnas_ok.append(posicion)

si usamos un array o matriz
MATRIZ_ESTADOS = [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  ] 


posicion 2 [7, 2] 7 + 2 = 9
Para los que con la formula den = 10 que partan desde el principio

(7 + 2) + 2 - 1 = 10

for i in filas:
    coord = str(i) + "," + str(posicion)
    Coords.append(coord)

aplicar lo mismo con el caso de que sea fila
    


1) buscar tamaño 10.
2) buscar suma de las cota de dominio + cantidad de numeros - 1 = 10 


si la suma de las cota de dominio + cantidad de numeros - 1 = 10, entonces todos se separan por solo 1 esacio

Utilizar una estructura como un array para aplicar observacion de los estados tanto de columnas y filas; es decir
que esten concluidos o llenos.

filas_ok = []
columnas_ok = [posicion]