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



def Constraint_rows(row_constraints, Generate_board, Domain):
    print(row_constraints)
    # Acceder a cada arreglo dentro del arreglo
    for i in range(len(row_constraints)):
        # Acceder a cada elemento dentro del arreglo
        for j in range(len(row_constraints[i])):
            if (row_constraints[i][j] == len(row_constraints)):
                # imprime la posicion de la fila
                for x in range(len(Generate_board[i])):
                    Generate_board[i][x] = Domain[1]      
    
    print(Generate_board)
            
    

# Generate a code to solve a nonogram

def create_problem(row_constraints, column_constraints):
    dimension_rows = len(row_constraints) ; dimension_columns = len(column_constraints)
    
    # Genera la matriz de 0's
    Generate_board = [[0 for i in range(dimension_columns)] for j in range(dimension_rows)]
    Domain = [0, 1]
    
    Constraint_rows(row_constraints, Generate_board, Domain)
    
    
    

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

    create_problem(row_constraints, column_constraints)

main()