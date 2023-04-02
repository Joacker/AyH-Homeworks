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

import itertools
import time


def get_row_indices(index, width):
    row = index // width
    return [row * width + i for i in range(width)]

def get_col_indices(index, height):
    col = index % height
    return [col + i * height for i in range(height)]

def check_constraint(sequence, clues):
    count = [len(list(g)) for k, g in itertools.groupby(sequence) if k == 1]
    return count == clues

def is_consistent(assignment, index, value, row_clues, col_clues, width, height):
    row_indices = get_row_indices(index, width)
    col_indices = get_col_indices(index, height)
    
    row = [assignment.get(i, None) for i in row_indices]
    col = [assignment.get(i, None) for i in col_indices]
    
    row[index % width] = value
    col[index // width] = value
    
    if None not in row and not check_constraint(row, row_clues[index // width]):
        return False

    if None not in col and not check_constraint(col, col_clues[index % height]):
        return False

    return True

def select_variable(domains):
    min_remaining_values = float('inf')
    selected_index = -1

    for i, domain in enumerate(domains):
        if 1 < len(domain) < min_remaining_values:
            min_remaining_values = len(domain)
            selected_index = i
    return selected_index if selected_index != -1 else len(domains)

def forward_checking(domains, width, height, row_clues, col_clues, node_count, backtrack_count):
    selected_index = select_variable(domains)

    if selected_index == len(domains):
        return domains, node_count, backtrack_count

    node_count += 1

    for value in domains[selected_index]:
        assignment = {i: domains[i][0] for i in range(selected_index)}

        if is_consistent(assignment, selected_index, value, row_clues, col_clues, width, height):
            new_domains = [domain.copy() for domain in domains]
            new_domains[selected_index] = [value]

            for i in range(selected_index + 1, len(domains)):
                new_domains[i] = [v for v in domains[i] if is_consistent(assignment, i, v, row_clues, col_clues, width, height)]

            if all(new_domains[i] for i in range(selected_index + 1, len(domains))):
                result, new_node_count, new_backtrack_count = forward_checking(new_domains, width, height, row_clues, col_clues, node_count, backtrack_count)
                if result:
                    return result, new_node_count, new_backtrack_count
        else:
            backtrack_count += 1

    return None, node_count, backtrack_count

def validate(constrains):
    suma = 0
    if len(constrains) > 1:
        for c in constrains:
            suma += int(c)
        suma += len(constrains) - 1
    else:
        suma = int(constrains[0])
    if suma == 10:
        return True
    return False

def preprocess(row_clues, col_clues, width, height):
    print(row_clues, col_clues, width, height)
    domains = [[0, 1] for _ in range(width * height)]
    # Procesar filas
    for row, clues in enumerate(row_clues):
        if len(clues) == 1:
            clue = clues[0]
            #solo para 10
            if clue == width:
                for col in range(width):
                    index = row * width + col
                    domains[index] = [1]
            elif clue * 2 > width:
                for col in range(width - clue + 1, clue):
                    index = row * width + col
                    domains[index] = [1]
        else:
            if validate(clues):
                if len(clues) == 1:
                    for col in range(width):
                        index = row * width + col
                        domains[index] = [1]
                else:
                    cont = 0
                    nrestriccion = 0
                    aux = 0
                    for c in clues:
                        print("rango de c", c)
                        i = 0
                        nrestriccion += 1
                        for i in range(c):
                            index = row * width + cont
                            print("index",index)
                            domains[index] = [1]
                            cont += 1
                            i += 1
                        if cont < 10:
                            print("Entra a 0")
                            print(cont)
                            index = row * width + cont
                            
                            print("index",index)
                            domains[index] = [0]
                            cont += 1
                            aux += 1



    
    # Procesar columnas
    for col, clues in enumerate(col_clues):
        if len(clues) == 1:
            clue = clues[0]
            if clue == height:
                for row in range(height):
                    index = row * width + col
                    domains[index] = [1]
            elif clue * 2 > height:
                for row in range(height - clue + 1, clue):
                    index = row * width + col
                    domains[index] = [1]
    return domains

def solve_nonogram(row_clues, col_clues):
    height = len(row_clues)
    width = len(col_clues)
    domains = preprocess(row_clues, col_clues, width, height)
    print(domains)

    new_domains, node_count, backtrack_count = forward_checking(domains, width, height, row_clues, col_clues, 0, 0)
    print( new_domains, node_count, backtrack_count)

    if new_domains:
        assignment = {i: new_domains[i][0] for i in range(len(new_domains))}
        grid = [[assignment[row * width + col] for col in range(width)] for row in range(height)]
        return grid, node_count, backtrack_count
    else:
        print("No solution found")
        return None, node_count, backtrack_count

def main():

    row_clues = [
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

    col_clues = [
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

    start_time = time.perf_counter()
    solution, node_count, backtrack_count = solve_nonogram(row_clues, col_clues)
    end_time = time.perf_counter()

    if solution:
        for row in solution:
            print("".join("1 " if cell == 1 else "0 " for cell in row))

    elapsed_time = end_time - start_time
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")
    print(f"Nodos generados: {node_count}")
    print(f"Nodos con backtracking: {backtrack_count}")

main()