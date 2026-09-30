import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# ----Pruebas con rangos invertidos--------
tamanios = [1000, 2000, 4000]
tiempos_py = []

print("Pruebas con rangos invertidos")

for N in tamanios:
    # Generar una la lista invertida: [1000, 999, ..., 1]
    datos_rango = list(range(N, 0, -1))
    
    inicio = time.perf_counter()
    insertion_sort(datos_rango)
    fin = time.perf_counter()
    
    tiempo_ms = (fin - inicio) * 1000  # Convertimos a milisegundos pues time.perf_counter() da el tiempo en segundos
    tiempos_py.append(tiempo_ms)
    print(f"Rango = {N} | Tiempo: {tiempo_ms:.2f} ms")

# Calculamos las proporciones de crecimiento
prop1 = tiempos_py[1] / tiempos_py[0]
prop2 = tiempos_py[2] / tiempos_py[1]

print(f"\nProporción 1 (2000 / 1000): {prop1:.2f}")
print(f"Proporción 2 (4000 / 2000): {prop2:.2f}")