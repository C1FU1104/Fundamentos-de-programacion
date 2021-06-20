numero_del_bus = int(input('Ingrese el número de bus: '))
velocidad_promedio = float(input('Ingrese la velocidad promedio por hora del bus: '))
distancia = float(input('Ingrese la ditancia a recorrer por el bus: '))
numero_asajeros_suben = float(input('Ingrese el numero de pasajeros que suben al bus: '))
numero_pasajeros_bajan = float(input('Ingrese el numero de pasajeros que bajan del bus: '))
tiempo_subida_pasajeros = float(input('Ingrese el tiempo de subida de un pasajero: '))
tiempo_bajada_pasajeros = float(input('Ingrese el tiempo de bajada de un pasajero: '))


def calcular_tiempo_por_velocidad() -> float:
    tiempo_recorrido_inicial = (distancia / velocidad_promedio)*60
    return tiempo_recorrido_inicial

def calcular_tiempo_subida() -> float:
    tiempo_subida = numero_asajeros_suben * tiempo_subida_pasajeros
    return tiempo_subida

def calcular_tiempo_bajada() -> float:
    tiempo_bajada = numero_pasajeros_bajan * tiempo_bajada_pasajeros
    return tiempo_bajada

def calcular_tiempo_total():
    
    calcular_tiempo_recorrido_total = (calcular_tiempo_por_velocidad() + calcular_tiempo_subida() + calcular_tiempo_bajada())/60
    print('El tiempo total del recorrido del bus con número: ' + str(numero_del_bus) + ' es de '+ str(round(calcular_tiempo_recorrido_total,2))+' horas')
  
calcular_tiempo_total()

