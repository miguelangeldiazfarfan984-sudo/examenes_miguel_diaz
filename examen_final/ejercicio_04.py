"""Ejercicio 4 - Control de inventario mediante diccionarios"""

inventario = {
    "P01": {"nombre": "Laptop", "precio": 2500, "cantidad": 5},
    "P02": {"nombre": "Mouse", "precio": 45, "cantidad": 30},
    "P03": {"nombre": "Teclado", "precio": 120, "cantidad": 15},
    "P04": {"nombre": "Monitor", "precio": 650, "cantidad": 8},
}


def mostrar_inventario(productos):
    for codigo, p in productos.items():
        print("{} - {}: S/ {:.2f} | Stock: {}".format(codigo, p["nombre"], p["precio"], p["cantidad"]))


# Valida existencia y stock; si la compra es válida, actualiza existencias
def comprar(productos, codigo, cantidad):
    producto = productos.get(codigo)
    if producto is None:
        print("Compra rechazada: el producto {} no existe".format(codigo))
    elif not 0 < cantidad <= producto["cantidad"]:
        print("Compra rechazada: {} unidades de {} superan el stock ({})".format(
            cantidad, producto["nombre"], producto["cantidad"]))
    else:
        producto["cantidad"] -= cantidad
        importe = cantidad * producto["precio"]
        print("Compra válida: {} x {} = S/ {:.2f}".format(cantidad, producto["nombre"], importe))
        return importe
    return 0


def valor_inventario(productos):
    return sum(p["precio"] * p["cantidad"] for p in productos.values())


print("Inventario inicial:")
mostrar_inventario(inventario)
print()
comprar(inventario, "P02", 10)   # compra válida
comprar(inventario, "P09", 2)    # producto inexistente
comprar(inventario, "P01", 20)   # supera el stock
print("\nInventario actualizado:")
mostrar_inventario(inventario)
print("Valor total del inventario: S/ {:.2f}".format(valor_inventario(inventario)))
