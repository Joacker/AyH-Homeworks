# Tarea 1 Ze Hui Fu y Joaquín Fernández

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

import constraint
from functools import partial

def row_constraint(*variables, block):
    # Separamos las variables pintadas y conmtamos los bloques separados por '0's
    filled_cells = ""
    for v in variables:
        filled_cells += str(v)
    filled_cells = filled_cells.split("0")
    print(filled_cells)
    
    consecutive_filled = []
    for i in filled_cells:
        if i != "":
            consecutive_filled.append(len(i))
    
    if consecutive_filled == block:
        return True
    
    return False

def column_constraint(*variables, block):
    return row_constraint(*variables, block=block)

def create_problem(row_c, column_c):
    # Entregamos las dimensiones de la matriz
    rows, columns = len(row_c), len(column_c)
    problem = constraint.Problem()
    print(problem)

    # Variables
    variables = []
    for row in range(rows): 
        for col in range(columns):
            variables.append(f"({row},{col})")
            
    #print(variables)

    # Se definen los dominios para las variables
    domain = [0, 1]

    problem.addVariables(variables, domain)

    # Restricciones
    for i, row_blocks in enumerate(row_c):
        problem.addConstraint(partial(row_constraint, block=row_blocks), [f"({i},{j})" for j in range(columns)])

    for j, col_blocks in enumerate(column_c):
        problem.addConstraint(partial(row_constraint, block=col_blocks), [f"({i},{j})" for i in range(rows)])

    return problem.getSolution()

def display_solution(solution, size):
    if solution is None:
        print("No solution found.")
    else:
        print ("###########")
        rows, columns = size
        for i in range(rows):
            for j in range(columns):
                print(solution[f"({i},{j})"], end=" ")
            print()

def main():
    row_constraints = [
        [4],
        [8],
        [10],
        [1, 1, 2, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 6, 1],
        [6],
        [2, 2],
        [4],
        [2]
    ]

    column_constraints = [
        [4],
        [2],
        [7],
        [3, 4],
        [7, 2],
        [7, 2],
        [3, 4],
        [7],
        [2],
        [4]
    ]



    solution = create_problem(row_constraints, column_constraints)
    display_solution(solution, (len(row_constraints), len(column_constraints)))

main()