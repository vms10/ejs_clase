import csv
from collections import Counter, defaultdict


def arboles_parque(nombre_archivo, nombre_parque):
    arboles = {}

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            if fila['espacio_ve'].strip().upper() == nombre_parque.strip().upper():
                id_arbol = fila['id_arbol']
                arbol_info = {clave: valor for clave, valor in fila.items() if clave not in ('coord_x', 'coord_y')} # ignoro ultimas dos columnas
                arboles[id_arbol] = arbol_info
    return arboles


def arbol_mas_popular(nombre_parque):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    
    especies = [datos['nombre_com'] for datos in arboles.values()]
    contador = Counter(especies)
    
    especie_mas_comun = contador.most_common(1)
    
    if especie_mas_comun:
        return especie_mas_comun[0][0]  
    else:
        return None  
    
def n_mas_altos(nombre_parque, n):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)

    arboles_ordenados = sorted(
    arboles.items(),
    key=lambda item: int(item[1]['altura_tot']),
    reverse=True
    )

    # Devolver los n primeros
    return arboles_ordenados[:n]

def altura_promedio(nombre_parque, especie):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)

    alturas = [
        int(datos['altura_tot']) 
        for datos in arboles.values() 
        if datos['nombre_com'].strip().lower() == especie.strip().lower()
    ]

    if alturas:
        return sum(alturas) / len(alturas)
    else:
        return None  # SI NO EXISTE LA ESPECIE EN EL PARQUE
    

def parques_mas_arboles(nombre_archivo):
    contador = Counter()

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            parque = fila['espacio_ve'].strip().upper()
            if parque and parque != 'S/D':  # Filtrar entradas sin nombre de parque
                contador[parque] += 1

    if not contador:
        return []

    max_cantidad = max(contador.values())

    parques_maximos = [
        parque for parque, cantidad in contador.items()
        if cantidad == max_cantidad
    ]

    return parques_maximos

def parques_mas_altos_promedio(nombre_archivo):
    alturas_por_parque = defaultdict(list)

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            parque = fila['espacio_ve'].strip().upper()
            altura = fila['altura_tot'].strip()
            if altura.isdigit():  # número válido
                alturas_por_parque[parque].append(int(altura))

    promedios = {
        parque: sum(alturas) / len(alturas)
        for parque, alturas in alturas_por_parque.items()
    }

    if not promedios:
        return []

    max_promedio = max(promedios.values())

    parques_maximos = [
        parque for parque, promedio in promedios.items()
        if promedio == max_promedio
    ]

    return parques_maximos

def parques_mas_variedad(nombre_archivo):
    especies_por_parque = defaultdict(set)

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            parque = fila['espacio_ve'].strip().upper()
            especie = fila['nombre_com'].strip().lower()
            if parque and parque != 'S/D' and especie:
            #if especie:
                especies_por_parque[parque].add(especie)

    # Contar cuántas especies tiene cada parque
    cantidad_por_parque = {
        parque: len(especies) for parque, especies in especies_por_parque.items()
    }

    if not cantidad_por_parque:
        return []

    max_variedad = max(cantidad_por_parque.values())

    parques_maximos = [
        parque for parque, cantidad in cantidad_por_parque.items()
        if cantidad == max_variedad
    ]

    return parques_maximos

def especie_mas_frecuente(nombre_archivo):
    contador_especies = Counter()

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            especie = fila['nombre_com'].strip().lower()
            if especie:
                contador_especies[especie] += 1

    if not contador_especies:
        return []

    max_frecuencia = max(contador_especies.values())

    # Devolver todas las especies que tengan la frecuencia máxima
    especies_maximas = [
        especie for especie, cantidad in contador_especies.items()
        if cantidad == max_frecuencia
    ]

    return especies_maximas

def razon_exoticos_nativos(nombre_archivo):
    exoticos = 0
    nativos = 0

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            origen = fila['origen'].strip().lower()
            if origen == 'exótico':
                exoticos += 1
            elif origen == 'nativo/autóctono':
                nativos += 1

   
    return  exoticos/nativos