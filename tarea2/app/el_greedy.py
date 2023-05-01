import matplotlib.pyplot as plt

def read_file(name_file):
    uav_data = []
    name_file = name_file+'.txt'
    uav = {
        "index": 0,
        "tiempo_aterrizaje_menor": 0,
        "tiempo_aterrizaje_ideal": 0,
        "tiempo_aterrizaje_maximo": 0,
        "tiempos_aterrizaje": [],
        "orden": None
    }
    with open(name_file, 'r') as file:
        lines = file.readlines()
        linea_actual = 1
        #print(lines[0])
        D = int(lines[0])
        #print(D)
        #print(lines[1].strip().split(" "))
        for i in range(D):
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
    print(uav_data)
           

if __name__ == '__main__':
    palabras = [90, 90, 113, 113, 90, 90, 113, 90, 135, 113]
    longitudes = list(map(float, palabras))
    #print(longitudes)
    uav_data = read_file('t2_Titan')
    #print(uav_data)
    greedy_determinista(uav_data)
    #print([i for i in uav_data])
    # for i in uav_data:
    #     print(i)
    #print(uav_data[0]['tiempos_aterrizaje'])
    # print(greedy_determinista())