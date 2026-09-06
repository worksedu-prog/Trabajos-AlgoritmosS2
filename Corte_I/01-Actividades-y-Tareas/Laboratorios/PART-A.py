# 1. Definir la matriz de 4 puntos de acopio x 6 días usando listas anidadas
matriz = [
    [12.5, 0.0, 15.0, 8.5, 20.0, 14.0],
    [5.0, 10.0, 0.0, 22.5, 18.0, 11.5],
    [30.0, 25.5, 19.0, 0.0, 14.5, 20.0],
    [8.0, 12.0, 10.5, 15.0, 0.0, 25.0]
]

# 2. Inicializar listas para totales y el contador de ceros
total_punto = [0.0] * 4  # [0.0, 0.0, 0.0, 0.0]
total_dia = [0.0] * 6    # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
ceros = 0

# 3. Recorrer la matriz con ciclos anidados para sumar
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        total_punto[i] += matriz[i][j]
        total_dia[j] += matriz[i][j]
        if matriz[i][j] == 0.0:
            ceros += 1

# 4. Imprimir total por punto
print("--- TOTAL POR PUNTO DE ACOPIO ---")
for i in range(len(total_punto)):
    print(f"Punto {i + 1}: {total_punto[i]} kg")

# 5. Imprimir total por día
print("\n--- TOTAL POR DIA ---")
for j in range(len(total_dia)):
    print(f"Dia {j + 1}: {total_dia[j]} kg")

# 6. Punto más productivo (usando la función max para buscar el índice del mayor)
max_punto = total_punto.index(max(total_punto))
print(f"\nPunto mas productivo: Punto {max_punto + 1} ({total_punto[max_punto]} kg)")

# 7. Día de menor recolección (usando min para buscar el índice del menor)
min_dia = total_dia.index(min(total_dia))
print(f"Dia de menor recoleccion: Dia {min_dia + 1} ({total_dia[min_dia]} kg)")

# 8. Mostrar cuántos registros en 0 hubo
print(f"Registros con valor 0 (dias sin operar): {ceros}")
