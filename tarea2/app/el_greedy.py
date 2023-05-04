import matplotlib.pyplot as plt

def read_file(name_file):
    uav_data = []
    name_file = name_file+'.txt'
    
    with open(name_file, 'r') as file:
        lines = file.readlines()
        linea_actual = 1
        #print(lines[0])
        D = int(lines[0])
        #print(D)
        #print(lines[1].strip().split(" "))
        for i in range(D):
            uav = {
                "index": 0,
                "tiempo_aterrizaje_menor": 0,
                "tiempo_aterrizaje_ideal": 0,
                "tiempo_aterrizaje_maximo": 0,
                "tiempos_aterrizaje": [],
                "orden": None
            }
            #limpiamos los strings para guardarlos en la lista de aterrizajes
            aterrizaje = lines[linea_actual].strip().split()
            # iteramos sobre los tiempos de aterrizaje y los convertimos en floats
            aterrizaje = list(map(float, aterrizaje))
            # Sacamos la información del aterrizaje para cada uav
            uav['index'] = i
            uav['tiempo_aterrizaje_menor'] = aterrizaje[0]
            uav['tiempo_aterrizaje_ideal'] = aterrizaje[1]
            uav['tiempo_aterrizaje_maximo'] = aterrizaje[2]
            uav['tiempos_aterrizaje'] = uav['tiempos_aterrizaje']
            uav['orden'] = uav['orden']
            #print(uav)
            linea_actual += 1
            
            tiempo_aterrizaje = []
            #print(lines[linea_actual])
            # Añadimos todos los tiempos que se encuentran por debajo de cada tiempo, 
            # es decir guardamos los tiempos de aterrizaje los uavs en un array, 
            # dentro del objeto uav 
            while len(tiempo_aterrizaje) < D:
                # limpiamos los tiempos
                clean_tiempos = lines[linea_actual].strip().split()
                tiempos = list(map(float,clean_tiempos))
                # unimos los elementos del array de tiempos de aterrizaje 
                # con los elementos internos del aray tiempos
                tiempo_aterrizaje.extend(tiempos)
                linea_actual += 1
            
            uav['tiempos_aterrizaje'] = tiempo_aterrizaje
            uav_data.append(uav)
        return uav_data



def greedy_determinista(uav_data):
    # primero, lo que hacemos es ordenar los tiempo de aterrizaje sobre cada uav, 
    # de manera ascendente
    costo_total = 0
    sorting_uavs = sorted(uav_data, key=lambda uav: uav['tiempo_aterrizaje_ideal'], reverse=False)
    # print(sorting_uavs)
    # ahora, iteramos sobre cada uav, y sobre cada tiempo de aterrizaje,
    # para ver si el tiempo de aterrizaje es menor al tiempo de aterrizaje ideal
    # si es menor, lo guardamos en un array de tiempos de aterrizaje
    # si no, lo guardamos en un array de tiempos de aterrizaje ideal
    for i , uav in enumerate(sorting_uavs):
        assigned_time = -1
        penalizacion = float('inf')
        if i == 0:
            uav['orden'] = i
            uav['tiempo_aterrizaje_asignado'] = uav['tiempo_aterrizaje_ideal']
            continue
        #Procedemos a comparar entre los vlaores de tiempo de aterrizaje ideal y el tiempo de aterrizaje menor
        uav_anterior = sorting_uavs[i-1]
        assigned_time = max(uav["tiempo_aterrizaje_menor"],uav_anterior["tiempo_aterrizaje_asignado"]
                            +uav_anterior["tiempos_aterrizaje"][uav["index"]])
        if assigned_time <= uav['tiempo_aterrizaje_maximo']:
            uav['orden'] = i
            uav['tiempo_aterrizaje_asignado'] = assigned_time
            costo_total += abs(assigned_time - uav['tiempo_aterrizaje_ideal'])
            continue
        else:
            print("No se puede asignar un tiempo de aterrizaje")
    
    return costo_total, sorting_uavs

def display_data(total_cost,uav_data):
        print("Costo total:", total_cost)
        sorted_uav_data = sorted(uav_data, key=lambda uav: uav['orden'])
        array_solutions = []
        for i in sorted_uav_data:
            array_solutions.append(i['index'])
        print("Orden de aterrizaje:", array_solutions)

def plot_schedule(uav_data):
        fig, ax = plt.subplots()

        for uav in uav_data:
            y = uav['orden']
            
            # Dibujar puntos en el tiempo minimo, tiempo ideal, tiempo maximo y tiempo de aterrizaje asignado
            ax.plot(uav['tiempo_aterrizaje_menor'], y, marker='o', markersize=6, color='red')
            ax.plot(uav['tiempo_aterrizaje_ideal'], y, marker='o', markersize=6, color='green')
            ax.plot(uav['tiempo_aterrizaje_maximo'], y, marker='o', markersize=6, color='blue')
            ax.plot(uav['tiempo_aterrizaje_asignado'], y, marker='o', markersize=8, color='black')
            
            # Mostrar los valores del tiempo minimo, tiempo ideal, tiempo maximo y tiempo de aterrizaje asignado
            ax.text(uav['tiempo_aterrizaje_menor'], y, f"{uav['tiempo_aterrizaje_menor']:.1f}", ha='right', va='bottom', color='red')
            ax.text(uav['tiempo_aterrizaje_ideal'], y, f"{uav['tiempo_aterrizaje_ideal']:.1f}", ha='right', va='bottom', color='green')
            ax.text(uav['tiempo_aterrizaje_maximo'], y, f"{uav['tiempo_aterrizaje_maximo']:.1f}", ha='left', va='bottom', color='blue')
            ax.text(uav['tiempo_aterrizaje_asignado'], y, f"{uav['tiempo_aterrizaje_asignado']:.1f}", ha='left', va='bottom', color='black')

        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Orden de aterrizaje')
        ax.set_title('Programacion de aterrizaje de UAVs')
        plt.tight_layout()
        plt.show()


def process_data(file_name):
    uav_data = read_file(file_name)
    #print(uav_data)
    costo_total, processed_uav_data = greedy_determinista(uav_data)
    # print(costo_total)
    # print(processed_uav_data)
    display_data(costo_total, processed_uav_data)
    plot_schedule(processed_uav_data)

if __name__ == '__main__':
    #palabras = [90, 90, 113, 113, 90, 90, 113, 90, 135, 113]
    #longitudes = list(map(float, palabras))
    #print(longitudes)
    seguir = True
    while seguir:
        print("""Bienvenido al programa de aterrizaje de UAVs para algoritmo Greedy Determinista
                1. t2_Deimos.txt
                2. t2_Europa.txt
                3. t2_Titan.txt
                4. Salir""")
        opcion = input("Ingrese la opcion que desea: ")
        if opcion == "1":
            process_data('t2_Deimos')
        elif opcion == "2":
            process_data('t2_Europa')
        elif opcion == "3":
            process_data('t2_Titan')
        elif opcion == "4":
            seguir = False
        else:
            print("Opcion no valida")