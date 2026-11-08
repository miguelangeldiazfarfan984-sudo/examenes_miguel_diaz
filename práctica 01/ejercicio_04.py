"""
4. Registro de participantes con listas
Crear una lista vacía; agregar tres participantes; insertar uno en la segunda posición;
actualizar el nombre del primero; eliminar uno; mostrar la lista final y la cantidad.
No utilizar ciclos ni recorridos.
"""
from idlelib.debugger_r import close_subprocess_debugger

# Lista vacía
participantes = []

# Agregar tres participantes
participantes.append("Lucía")
participantes.append("Jorge")
participantes.append("Valeria")

# Insertar un nuevo participante en la segunda posición (índice 1)
participantes.insert(1, "Andrés")

# Actualizar el nombre del primer participante (índice 0)
participantes[0] = "Lucía Fernanda"

# Eliminar un participante
participantes.remove("Jorge")

# Mostrar la lista final y la cantidad
print(f"Lista final: {participantes}")
print(f"Cantidad de participantes: {len(participantes)}")close_subprocess_debugger()
