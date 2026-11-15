"""Ejercicio 3 - Sistema de registro de pedidos de Rappi"""
from datetime import datetime


# Decorador: muestra fecha y hora de ejecución y confirma si terminó bien
def registrar_pedido(funcion):
    def envoltura(*args, **kwargs):
        print("[{}] Ejecutando {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), funcion.__name__))
        resultado = funcion(*args, **kwargs)
        if resultado is not None:
            print("Operación finalizada correctamente. Total: S/ {:.2f}".format(resultado))
        print()
        return resultado
    return envoltura


# Valida que todos los precios sean numéricos y mayores que cero
def precios_validos(precios):
    for precio in precios:
        if not isinstance(precio, (int, float)) or precio <= 0:
            print("Precio inválido ({}): no se realizó el cálculo".format(precio))
            return False
    return True


@registrar_pedido
def calcular_total(*args):
    return sum(args) if precios_validos(args) else None


@registrar_pedido
def procesar_pedido(cliente, **kwargs):
    print("Cliente: {} | Productos: {}".format(cliente, ", ".join(kwargs)))
    return sum(kwargs.values()) if precios_validos(kwargs.values()) else None


calcular_total(12.5, 30, 8)
calcular_total(5, 10, 15, 20, 25, 30)
procesar_pedido("Ana", hamburguesa=18.9, papas=7.5, gaseosa=5, helado=6.5)
procesar_pedido("Luis", pizza=35, bebida=-4, postre=9)
