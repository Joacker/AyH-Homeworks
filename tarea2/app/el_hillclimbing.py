import matplotlib.pyplot as plt
import numpy as np, random

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
        
        print(uav_data[0])
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
        for tiempo in uav['tiempos_aterrizaje']:
            condicion_resta = abs(tiempo - uav['tiempo_aterrizaje_ideal'])
            if condicion_resta < penalizacion:
                print("condicion_resta",condicion_resta)
                
                assigned_time = tiempo
                penalizacion = condicion_resta
        
        #Procedemos a comparar entre los vlaores de tiempo de aterrizaje ideal y el tiempo de aterrizaje menor
        min_time_assigned = min(assigned_time, uav['tiempo_aterrizaje_maximo'])
        assigned_time = max(uav["tiempo_aterrizaje_menor"],min_time_assigned)
        uav['orden'] = i
        uav['tiempo_aterrizaje_asignado'] = assigned_time
        costo_total += abs(assigned_time - uav['tiempo_aterrizaje_ideal'])
    
    return costo_total, sorting_uavs

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
            probabilities.append(1 / (j**2 + 1))
            
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

def Cost(uav_data, result):
  cost = 0
  for i in result:
      uav = uav_data[i]
      clossest_time = uav['tiempos_aterrizaje'][0]
      cost_n = abs(uav['tiempo_aterrizaje_asignado']-result[i][0])
      #print(cost_n,"Pref: ",arrival_times[i][1],"Selct: ", result[i][0])
      cost = cost + cost_n
  return cost


if __name__ == "__main__":
    uav_data = read_file("t2_Titan")
    costo_total, sorting_uavs = greedy_determinista(uav_data)
    print(costo_total)
    print(sorting_uavs)