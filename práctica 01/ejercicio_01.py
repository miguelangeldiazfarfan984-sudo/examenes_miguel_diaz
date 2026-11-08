"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente.
- Asignar en variables los datos de tu nombre, salario, edad y compañía e identificar sus tipos
- Edad tiene que ser tipo string; para usarla más adelante aplicar una conversión
- Si la edad es mayor a 30: "Usted tiene un bono de 10% en el mes de diciembre",
  caso contrario: "Usted tiene un bono del 5% en el mes diciembre"
- Mostrar el bono final: potencia de 2 del salario más el 5 o 10 % de su salario
"""

# Datos del usuario
nombre = "Miguel Angel Diaz Farfan"
salario = 2500.0
edad = "39"                 # la edad se guarda como texto (string)
compania = "Globokas Peru SA"

# Identificar los tipos de cada variable
print(f"nombre: {type(nombre)}")
print(f"salario: {type(salario)}")
print(f"edad: {type(edad)}")
print(f"compania: {type(compania)}")

# Conversión de la edad a entero para poder compararla
edad_numero = int(edad)

# Condicional según la edad
if edad_numero > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    porcentaje = 0.10
else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    porcentaje = 0.05

# Bono final: salario al cuadrado + porcentaje del salario
bono_final = salario ** 2 + salario * porcentaje
print(f"Bono final: {bono_final:.2f}")
