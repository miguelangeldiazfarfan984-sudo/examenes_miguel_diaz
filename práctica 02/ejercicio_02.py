"""Ejercicio 2 - Transferencias entre personas"""
from ejercicio_01 import Persona  # reutiliza la clase del ejercicio anterior

lucia = Persona("Lucía", 30, 1000)
jorge = Persona("Jorge", 25, 300)

# Una transferencia válida y tres rechazadas (no numérico, negativo, excede saldo)
for monto in (250, "cien", -50, 5000):
    lucia.transferir(jorge, monto)
    print("Saldos -> {}: S/ {} | {}: S/ {}".format(
        lucia.nombre, lucia.consultar_saldo(), jorge.nombre, jorge.consultar_saldo()))
