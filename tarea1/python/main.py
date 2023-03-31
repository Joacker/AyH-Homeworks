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
    # Separamos las variables pintadas y contamos los bloques separados por '0's
    consecutive_filled = [len(group) for group in "".join(str(v) for v in variables).split("0") if group]
    if consecutive_filled == block:
        return True
    return False

def column_constraint(*variables, block):
    return row_constraint(*variables, block=block)

def create_function(rows, columns, row_constraints, column_constraints):
    problem = constraint.Problem()
    variables = [f"X_{row}_{col}" for row in range(rows) for col in range(columns)]
    domain = [0, 1]
    problem.addVariables(variables, domain)
    for i, row_blocks in enumerate(row_constraints):
        problem.addConstraint(partial(row_constraint, block=row_blocks), [f"X_{i}_{j}" for j in range(columns)])
    for j, col_blocks in enumerate(column_constraints):
        problem.addConstraint(partial(row_constraint, block=col_blocks), [f"X_{i}_{j}" for i in range(rows)])
    return problem.getSolution()
     

def display_solution(solution, size):
    if solution != None:
        print ("###########")
        rows, columns = size
        for i in range(rows):
            for j in range(columns):
                print(solution[f"X_{i}_{j}"], end=" ")
            print()
    else:
        print("Cannot found a solution for the problem.")

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
    sol = create_function(len(row_constraints), len(column_constraints), row_constraints, column_constraints)
    display_solution(sol, (len(row_constraints), len(column_constraints)))

if __name__ == "__main__":
    main()