import random

def crear_album(figus_total):
    return [0] * figus_total


def album_incompleto(A):
    return 0 in A


def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] += 1
        compras += 1
    return compras


def experimento_figus(n_repeticiones, figus_total):
    resultados = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    return sum(resultados) / n_repeticiones


def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(0, figus_total - 1) for _ in range(figus_paquete)]


def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu] += 1
        compras += 1
    return compras


if __name__ == "__main__":
    n_repeticiones = 100
    figus_total = 860
    experimento_figus(n_repeticiones, figus_total)
    
