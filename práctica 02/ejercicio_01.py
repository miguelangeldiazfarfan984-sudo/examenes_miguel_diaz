"""Ejercicio 1 - Registro de personas"""
from datetime import datetime


class Persona:
    def __init__(self, nombre="", edad=0, saldo=0, nacionalidad="Peruana"):
        self.nombre, self.edad, self.saldo, self.nacionalidad = nombre, edad, saldo, nacionalidad
        self.fecha_creacion = datetime.now()  # momento de creación del objeto

    # Registra nombre y edad por consola; repite si la edad no es válida
    def registrar(self):
        self.nombre = input("Nombre: ")
        while True:
            try:
                self.edad = int(input("Edad: "))
                if self.edad >= 0:
                    break
                print("Error: la edad no puede ser negativa")
            except ValueError:
                print("Error: ingrese un número entero válido")

    def cumpleanos(self):
        self.edad += 1

    def consultar_saldo(self):
        return self.saldo

    # Transfiere dinero validando el monto; si falla, los saldos no cambian
    def transferir(self, destino, monto):
        if not isinstance(monto, (int, float)):
            motivo = "el monto no es numérico"
        elif monto <= 0:
            motivo = "el monto debe ser mayor que cero"
        elif monto > self.saldo:
            motivo = "saldo insuficiente"
        else:
            self.saldo -= monto
            destino.saldo += monto
            print("Transferencia de S/ {} de {} a {} realizada".format(monto, self.nombre, destino.nombre))
            return True
        print("Transferencia de {} rechazada: {}".format(monto, motivo))
        return False


# Retorna la fecha y hora de registro con precisión de minutos
def fecha_registro(persona):
    return persona.fecha_creacion.strftime("%d/%m/%Y %H:%M")


if __name__ == "__main__":
    personas = [Persona(), Persona()]
    for persona in personas:
        persona.registrar()
    for persona in personas:
        persona.cumpleanos()
        print("{} ({}) - Edad actualizada: {} | Registrado: {}".format(
            persona.nombre, persona.nacionalidad, persona.edad, fecha_registro(persona)))
