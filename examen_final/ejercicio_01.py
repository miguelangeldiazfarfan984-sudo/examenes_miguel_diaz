"""Ejercicio 1 - Sistema de alquiler de vehículos"""


class Vehiculo:
    def __init__(self, marca, modelo, anio=2020):
        self.marca, self.modelo, self.anio = marca, modelo, anio

    def actualizar_marca(self, marca):
        self.marca = marca

    def actualizar_anio(self, anio):
        if anio > 0:
            self.anio = anio
        else:
            print("Error: el año debe ser mayor que cero")

    def mostrar_datos(self):
        print("Vehículo: {} {} ({})".format(self.marca, self.modelo, self.anio))


class VehiculoAlquiler(Vehiculo):  # herencia
    def __init__(self, marca, modelo, codigo, tarifa_diaria, anio=2020):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self.__tarifa_diaria = 0  # atributo encapsulado (privado)
        self.actualizar_tarifa(tarifa_diaria)

    def obtener_tarifa(self):
        return self.__tarifa_diaria

    # Única forma de cambiar la tarifa: solo valores numéricos mayores que cero
    def actualizar_tarifa(self, tarifa):
        if isinstance(tarifa, (int, float)) and tarifa > 0:
            self.__tarifa_diaria = tarifa
        else:
            print("Error: tarifa {} inválida, se mantiene S/ {:.2f}".format(tarifa, self.__tarifa_diaria))

    def aumentar_tarifa(self, porcentaje=10):
        self.__tarifa_diaria *= 1 + porcentaje / 100

    # Retorna importe, descuento y total según los días de alquiler
    def calcular_descuento(self, dias_alquiler):
        importe = self.__tarifa_diaria * dias_alquiler
        tasa = 0.05 if dias_alquiler < 2 else 0.10 if dias_alquiler <= 5 else 0.15
        return importe, importe * tasa, importe * (1 - tasa)

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Código: {} | Tarifa diaria: S/ {:.2f}".format(self.codigo, self.__tarifa_diaria))


auto = VehiculoAlquiler("Toyota", "Yaris", "V001", 120)
camioneta = VehiculoAlquiler("Hyundai", "Tucson", "V002", 200, 2023)
auto.actualizar_anio(2022)

# Dos incrementos consecutivos a la tarifa del auto
for porcentaje in (10, 5):
    auto.aumentar_tarifa(porcentaje)
    print("Tarifa de {} tras aumento de {}%: S/ {:.2f}".format(auto.codigo, porcentaje, auto.obtener_tarifa()))

# Intento de tarifa negativa: la tarifa no cambia
camioneta.actualizar_tarifa(-50)
print()

# Importes con distintas cantidades de días
for vehiculo, dias in ((auto, 1), (auto, 4), (camioneta, 7)):
    vehiculo.mostrar_datos()
    importe, descuento, total = vehiculo.calcular_descuento(dias)
    print("Días: {} | Importe: S/ {:.2f} | Descuento: S/ {:.2f} | Total: S/ {:.2f}\n".format(
        dias, importe, descuento, total))
