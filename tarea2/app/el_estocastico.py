import matplotlib.pyplot as plt
import random, time
import numpy as np

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


def greedy_estucastico(uav_data, seed=0):
    # Usamos de semilla el tiempo actual en epoch time para que sea aleatorio
    np.random.seed(seed)
    costo_total = 0
    sorting_uavs = sorted(uav_data, key=lambda x: x['tiempo_aterrizaje_ideal'], reverse=False)
    time1 = 0
    
    for i in range(len(uav_data)):
        
        minum_values = min(len(sorting_uavs), 3)
        
        probabilities = []
        for j in range(minum_values):
            probabilities.append(1 / (j + 1))
        suma_probabilidades = sum(probabilities)
        
        new_probabilities = []
        for p in range(len(probabilities)):
            new_probabilities.append(probabilities[p] / suma_probabilidades)
        
        
        # Seleccionar uno de los minum_value UAVs más cercanos al tiempo ideal actual
        idx = np.random.choice(range(minum_values), p=new_probabilities)
        # se debe remover el uav de la lista de uavs disponibles
        selected_uav = sorting_uavs.pop(idx)
        
        closest_time =  max(selected_uav['tiempo_aterrizaje_menor'], min(selected_uav['tiempo_aterrizaje_maximo'], max(time1, selected_uav['tiempo_aterrizaje_ideal'])))
        
        penalty = abs(closest_time - selected_uav['tiempo_aterrizaje_ideal'])
        
        selected_uav['tiempo_aterrizaje_asignado'] = closest_time
        selected_uav['penalizacion'] = penalty
        
        # Actualizar el costo total y el tiempo actual
        costo_total += penalty
        time1 = closest_time + selected_uav['tiempos_aterrizaje'][i]
        
        # Asignar el orden de aterrizaje
        selected_uav['orden'] = i

    return costo_total, uav_data

def display_data(total_cost, uav_data):
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

if __name__ == "__main__":
    uav_data = read_file('t2_Titan')
    costo_total, sorting_uavs = greedy_estucastico(uav_data,12)
    print("Costo total: ", costo_total)
    print("UAVs: ", sorting_uavs)
    display_data(costo_total, sorting_uavs)
    