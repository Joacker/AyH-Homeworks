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
import sys
from csp import CSP
# Restrcciones de dimenciones de la matriz 10x10
DIMENSION = 10

def domains():
    # Se crea un diccionario con las variables y sus dominios
    domains = {}
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            domains[(i, j)] = [1, 2, 3, 4, 6, 7, 8, 10]
    return domains

def constraints():
    # Se crea una lista de restricciones
    constraints = []
    # Se agregan las restricciones de las filas
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            for k in range(j + 1, DIMENSION):
                constraints.append(([(i, j), (i, k)], lambda x, y: x != y))
    # Se agregan las restricciones de las columnas
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            for k in range(j + 1, DIMENSION):
                constraints.append(([(j, i), (k, i)], lambda x, y: x != y))
    # Se agregan las restricciones de las diagonales
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            for k in range(j + 1, DIMENSION):
                constraints.append(([(i, j), (i + k - j, k)], lambda x, y: x != y))
                constraints.append(([(i, j), (i - k + j, k)], lambda x, y: x != y))
    return constraints

def solve():
    # Se crea un problema de CSP
    problem = CSP(domains(), constraints())
    # Se resuelve el problema
    solution = problem.backtracking_search()
    # Se imprime la solucion
    print(solution)

def main():
    print("Hello World")

if __name__ == '__main__':
    main()