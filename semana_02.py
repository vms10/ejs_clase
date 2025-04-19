def invertir_lista(lista: list[any]) -> list[any]:
    lista_invertida = []
    i = len(lista) - 1
    while i >= 0:
        lista_invertida.append(lista[i])
        i -= 1

    return lista_invertida


def collatz(nro: int) -> int:
    if nro <= 0:
        raise ValueError("El número debe ser un entero positivo.")

    pasos: int = 0
    while nro != 1:
        if nro % 2 == 0:
            nro //= 2
        else:
            nro = 3 * nro + 1
        pasos += 1

    return pasos


def contar_definiciones(d: dict[str, list[str]]) -> dict[str, int]:

    return {clave: len(definiciones) for clave, definiciones in d.items()}


def cantidad_de_claves_letra(d: dict[str, list[str]], l: str) -> int:

    return sum(1 for clave in d if clave.startswith(l))


def propagar(lista: list[int]) -> list[int]:

    resultado: list[int] = lista[:]

    # Propagar fuego a la derecha
    for i in range(1, len(resultado)):
        if resultado[i] == 0 and resultado[i - 1] == 1:
            resultado[i] = 1

    # Propagar fuego a la izquierda
    for i in range(len(resultado) - 2, -1, -1):
        if resultado[i] == 0 and resultado[i + 1] == 1:
            resultado[i] = 1

    return resultado
