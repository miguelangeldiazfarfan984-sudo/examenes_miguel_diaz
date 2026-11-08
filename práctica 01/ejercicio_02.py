"""
2. Caso: Reporte de calificaciones
Matemáticas: 17 (40%), Ciencia: 14 (30%), Historia: 15 (30%)
- Calcular la nota final ponderada y mostrarla con 1 decimal
- Evaluar si aprueba (nota final >= 13.0) y mostrar un mensaje booleano
- Generar una cadena resumen con la nota final y el estado
"""

# Notas de los cursos
matematicas = 17
ciencia = 14
historia = 15

# Nota ponderada: cada nota por su peso
nota_final = matematicas * 0.40 + ciencia * 0.30 + historia * 0.30
print(f"La nota final es: {nota_final:.1f}")

# Evaluación booleana
aprobado = nota_final >= 13.0
print(f"¿Aprobado?: {aprobado}")

# Estado en texto
if aprobado:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

# Cadena resumen
resumen = f"El estudiante obtuvo una nota final de {nota_final:.1f} y su estado final es: {estado}"
print(resumen)