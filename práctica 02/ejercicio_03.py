"""Ejercicio 3 - Funciones y manejo de excepciones"""


def pedir_valores():
    return float(input("Valor 1: ")), float(input("Valor 2: "))


def dividir(a, b):
    return a / b


def sumar(a, b):
    return a + b


# Guarda el dato como número si se puede; si no, como texto
def convertir(dato):
    try:
        return float(dato)
    except ValueError:
        return dato


def crear_lista(n):
    return [convertir(input("Elemento {}: ".format(i + 1))) for i in range(n)]


def obtener_elemento(lista, indice):
    return lista[indice]


def operar_valores():
    a, b = pedir_valores()
    return sumar(a, b), dividir(a, b)


def consultar(lista):
    elemento = obtener_elemento(lista, int(input("Índice a consultar: ")))
    return elemento, sumar(elemento, 10)


# Ejecuta una operación y permite reintentarla mientras haya errores
def intentar(operacion):
    while True:
        try:
            resultado = operacion()
        except ValueError:
            print("Error: debe ingresar un valor numérico")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero")
        except TypeError:
            print("Error: no se puede operar un texto con un número")
        except IndexError:
            print("Error: la posición consultada no existe en la lista")
        else:
            return resultado
        finally:
            print("- Intento procesado -")


for prueba in range(1, 4):
    print("\n=== Prueba {} ===".format(prueba))
    suma, division = intentar(operar_valores)
    print("Suma: {} | División: {:.2f}".format(suma, division))
    lista = intentar(lambda: crear_lista(int(input("¿Cuántos elementos desea registrar? "))))
    elemento, total = intentar(lambda: consultar(lista))
    print("Lista: {} | Elemento: {} | Elemento + 10: {}".format(lista, elemento, total))
