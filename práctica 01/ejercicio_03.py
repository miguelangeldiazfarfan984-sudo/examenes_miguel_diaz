"""
3. Caso: Calculadora de propinas
Ingresar por input el total de la cuenta (float), el porcentaje de propina (float)
y el número de personas (int). Mostrar el monto total con propina, el monto por
persona con 2 decimales y una advertencia si el monto por persona supera S/. 100
"""

# Datos ingresados por el usuario
total_cuenta = float(input("Total de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina: "))
numero_personas = int(input("Número de personas: "))

# Cálculos
propina = total_cuenta * porcentaje_propina / 100
total_con_propina = total_cuenta + propina
monto_por_persona = total_con_propina / numero_personas

# Resultados
print(f"Monto total con propina: S/. {total_con_propina:.2f}")
print(f"Cada persona debe pagar: S/. {monto_por_persona:.2f}")

# Mensaje personalizado según el monto
if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
else:
    print("El monto por persona está dentro del rango de S/. 100")