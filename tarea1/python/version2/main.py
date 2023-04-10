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
import sys


def index_columna(index, largo):
    col = index % largo
    column_indices = []
    for i in range(largo):
        column_indices.append(col + i * largo)
    return column_indices

def index_fila(index, ancho):
    row = index // ancho
    crow_indices = []
    for i in range(ancho):
        crow_indices.append(row * ancho + i)
    return crow_indices

def verify(sequence, constraint):
    count = []
    for k, g in itertools.groupby(sequence):
        if k == 1:
            count.append(len(list(g)))
    return count == constraint

def consistent(asignados, index, value, row_constraints, column_constraints, ancho, largo):
    row_indices = index_fila(index, ancho)
    col_indices = index_columna(index, largo)

    row = []
    col = []

    for i in row_indices:
        if i not in asignados:
            row.append(None)
        else:
            row.append(asignados[i])
    
    for i in col_indices:
        if i not in asignados:
            col.append(None)
        else:
            col.append(asignados[i])

    row[index % ancho] = value
    col[index // ancho] = value
    
    if None not in row and not verify(row, row_constraints[index // ancho]):
        return False

    if None not in col and not verify(col, column_constraints[index % largo]):
        return False

    return True

def forward_checking(domains, ancho, largo, row_constraints, column_constraints, node_count):
    
    index = get_variable(domains)

    if index == len(domains):
        return domains, node_count

    node_count += 1

    for value in domains[index]:
        asignados = {}
        for i in range(index):
            asignados[i] = domains[i][0]

        if consistent(asignados, index, value, row_constraints, column_constraints, ancho, largo):
            #new_domains = [domain.copy() for domain in domains]
            new_domains = []
            for domain in domains:
                new_domains.append(domain.copy())
            new_domains[index] = [value]

            for i in range(index + 1, len(domains)):
                new_domains[i] = []
                for v in domains[i]:
                    if consistent(asignados, i, v, row_constraints, column_constraints, ancho, largo):
                        new_domains[i].append(v)
                
            if all(new_domains[i] for i in range(index + 1, len(domains))):
                result, new_node_count = forward_checking(new_domains, ancho, largo, row_constraints, column_constraints, node_count)
                if result:
                    return result, new_node_count

    return None, node_count

def get_variable(domains):
    
    minimo_local = float(sys.maxsize)
    index = -1

    for i, domain in enumerate(domains):
        if 1 < len(domain) < minimo_local:
            minimo_local = len(domain)
            index = i
    if index != -1:
        return index
    else:
        return len(domains)

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

def preprocess(row_constraints, column_constraints, ancho, largo):
    #print(row_constraints, column_constraints, ancho, largo)
    domains = []
    for _ in range(ancho * largo):
        domains.append([0, 1])
    # Procesar filas
    for row, constraint in enumerate(row_constraints):
        if len(constraint) == 1:
            constraint = constraint[0]
            #solo para 10
            if constraint == ancho:
                for col in range(ancho):
                    index = row * ancho + col
                    domains[index] = [1]
            elif constraint * 2 > ancho:
                for col in range(ancho - constraint + 1, constraint):
                    index = row * ancho + col
                    domains[index] = [1]
        else:
            if validate(constraint):
                if len(constraint) == 1:
                    for col in range(ancho):
                        index = row * ancho + col
                        domains[index] = [1]
                else:
                    cont = 0
                    for c in constraint:
                        #print("rango de c", c)
                        i = 0
                        for i in range(c):
                            index = row * ancho + cont
                            #print("index",index)
                            domains[index] = [1]
                            cont += 1
                            i += 1
                        if cont < 10:
                            #print("Entra a 0")
                            #print(cont)
                            index = row * ancho + cont
                            
                            #print("index",index)
                            domains[index] = [0]
                            cont += 1
    # Procesar columnas
    for col, constraint in enumerate(column_constraints):
        if len(constraint) == 1:
            constraint = constraint[0]
            if constraint == largo:
                for row in range(largo):
                    index = row * ancho + col
                    domains[index] = [1]
            elif constraint * 2 > largo:
                for row in range(largo - constraint + 1, constraint):
                    index = row * ancho + col
                    domains[index] = [1]
        else:
            if validate(constraint):
                if len(constraint) == 1:
                    for col in range(ancho):
                        index = row * ancho + col
                        domains[index] = [1]
                else:
                    cont = 0
                    nrestriccion = 0
                    aux = 0
                    for c in constraint:
                        #print("rango de cc", c)
                        i = 0
                        nrestriccion += 1
                        for i in range(c):
                            index = col  + cont
                            #print("indexc",index)
                            domains[index] = [1]
                            cont += 10
                            i += 1
                        if cont < 100:
                            #print("Entra a 0c")
                            #print(cont)
                            index = col  + cont
                            
                            #print("indexc",index)
                            domains[index] = [0]
                            cont += 10
                            aux += 1
    return domains

def solver(row_constraints, column_constraints):
    largo = len(row_constraints)
    ancho = len(column_constraints)
    domains = preprocess(row_constraints, column_constraints, ancho, largo)
    #print(domains)

    new_domains, node_count = forward_checking(domains, ancho, largo, row_constraints, column_constraints, 0)

    if new_domains:
        asignados = {}
        for i in range(len(new_domains)):
            asignados[i] = new_domains[i][0]
        
        cells = []
        for row in range(largo):
            cells.append([])
            for col in range(ancho):
                cells[row].append(asignados[row * ancho + col])
            
                
        return cells, node_count
    else:
        print("No solution found")
        return None, node_count

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

    start_time = time.perf_counter()
    solution, node_count= solver(row_constraints, column_constraints)
    end_time = time.perf_counter()

    if solution:
        for row in solution:
            print()
            for cell in row:
                if cell == 1:
                    print("#", end=" ")
                else:
                    print(".", end=" ")

    elapsed_time = end_time - start_time
    print()

    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")
    print(f"Nodos generados: {node_count}")

main()