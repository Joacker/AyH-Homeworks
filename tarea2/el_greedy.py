import matplotlib.pyplot as plt

def read_file(name_file):
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
            #limpiamos los strings para guardarlos en la lista de aterrizazes
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
            print(uav)
            linea_actual += 1
            
            tiempo_aterrizaje = []

            
        
        #print(D)
        

if __name__ == '__main__':
    palabras = [90, 90, 113, 113, 90, 90, 113, 90, 135, 113]
    longitudes = list(map(float, palabras))
    #print(longitudes)
    read_file('t2_deimos')