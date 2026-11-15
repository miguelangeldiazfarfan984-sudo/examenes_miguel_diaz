"""Módulo operaciones - Funciones para procesar números"""
import random


# Genera n enteros aleatorios entre 1 y 100; n debe ser entero positivo
def generar_lista(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("la cantidad n debe ser un entero positivo (recibido: {})".format(n))
    return [random.randint(1, 100) for _ in range(n)]


def sin_repetidos(lista):
    return list(dict.fromkeys(lista))  # conserva el orden original


def ordenar(lista):
    return sorted(lista), sorted(lista, reverse=True)


def mayor_par(lista):
    pares = [numero for numero in lista if numero % 2 == 0]
    return max(pares) if pares else "No existe número par"


def obtener_elemento(lista, posicion):
    try:
        return lista[posicion]
    except IndexError:
        return "Posición {} inexistente".format(posicion)
