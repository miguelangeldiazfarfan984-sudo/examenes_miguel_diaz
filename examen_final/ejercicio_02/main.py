"""Ejercicio 2 - Programa principal"""
import operaciones as op

# Dos ejecuciones válidas y una cantidad inválida
for n in (8, 12, "cinco"):
    try:
        lista = op.generar_lista(n)
    except ValueError as error:
        print("Error: {}\n".format(error))
        continue
    ascendente, descendente = op.ordenar(lista)
    print("n = {}\nOriginal: {}\nSin duplicados: {}".format(n, lista, op.sin_repetidos(lista)))
    print("Ascendente: {}\nDescendente: {}\nMayor par: {}\n".format(ascendente, descendente, op.mayor_par(lista)))

# Posición válida y posición fuera de rango
print("Elemento en posición 2:", op.obtener_elemento(lista, 2))
print("Elemento en posición 50:", op.obtener_elemento(lista, 50))
