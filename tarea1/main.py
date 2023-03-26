# Tarea 1

'''
                        3  7  7  3
               4  2  7  4  2  2  4  7  2  4
            4           X  X  X  X
            8     X  X  X  X  X  X  X  X
           10  X  X  X  X  X  X  X  X  X  X
1  1  2  1  1  X     X     X  X     X     X
1  1  2  1  1  X     X     X  X     X     X
      1  6  1  X     X  X  X  X  X  X     X
            6        X  X  X  X  X  X
         2  2        X  X        X  X  
            4           X  X  X  X
            2              X  X
'''

# Variables de la matriz
VARIABLES = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
# Restrcciones de dimenciones de la matriz 10x10
DIMENSION = 10
# Restricciones de los valores de la matriz
FILAS = [4, 2, 7, [3, 4], [7, 2], [7, 2], [3, 4], 7, 2, 4]
COLUMNAS = [4, 8, 10, [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], 6, [2, 2], 4, 2]
COORDEANDAS = [ (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
                (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
                (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
                (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
                (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
                (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9),
                (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9),
                (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9),
                (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
                (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9) ]

# Restricciones de la matriz
def restricciones():
    # Restricciones de las filas
    for i in range(DIMENSION):
        if type(FILAS[i]) == list:
            for j in range(len(FILAS[i])):
                print("Fila " + str(i) + " columna " + str(j) + " valor " + str(FILAS[i][j]))
        else:
            print("Fila " + str(i) + " valor " + str(FILAS[i]))
    # Restricciones de las columnas
    for i in range(DIMENSION):
        if type(COLUMNAS[i]) == list:
            for j in range(len(COLUMNAS[i])):
                print("Columna " + str(i) + " fila " + str(j) + " valor " + str(COLUMNAS[i][j]))
        else:
            print("Columna " + str(i) + " valor " + str(COLUMNAS[i]))
    # Restricciones de las coordenadas
    for i in range(len(COORDEANDAS)):
        print("Coordenada " + str(i) + " valor " + str(COORDEANDAS[i]))

# Funcion para resolver el problema
def resolver():
    # Restricciones de la matriz
    restricciones()
    

def main():
    print("Tarea 1")
    resolver()
    
if __name__ == '__main__':
    main()