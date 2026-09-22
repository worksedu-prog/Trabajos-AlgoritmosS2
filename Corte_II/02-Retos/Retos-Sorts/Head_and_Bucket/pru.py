import random
import time



#Bucket Sort, prueben con cinco cubetas y con cincuenta sobre los mismos datos, y medir

#Verificación del tiempo

import time


def bucket_sort(arr, num_buckets):
    if len(arr) == 0:
        return arr

    # Determinar los valores mínimo y máximo para definir el rango de distribución
    min_value = min(arr)
    max_value = max(arr)
    
    # Manejo de caso borde: si todos los números son iguales
    if min_value == max_value:
        return arr

    # Calcular el tamaño del rango que cubrirá cada cubeta (bucket)
    bucket_range = (max_value - min_value) / num_buckets

    # Crear 'n' cubetas vacías
    buckets = [[] for i in range(num_buckets)]

    # Distribuir los elementos del arreglo dentro de las cubetas correspondientes
    for num in arr:
        index = int((num - min_value) / bucket_range)
        # Ajuste para evitar desbordamiento de índice en el elemento máximo
        if index >= num_buckets:
            index -= num_buckets - 1
        buckets[index].append(num)

    # Ordenar individualmente cada cubeta y unir los resultados en una sola lista
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Utiliza el ordenamiento ´sorted()´ para sublistas pequeñas

    return sorted_arr


# ... (tu función bucket_sort con la corrección del index) ...

# Creamos una lista con 10,000 números aleatorios para que la medición sea REAL
mi_lista = [random.uniform(1, 10000) for _ in range(10000)]

# Medición con 5 cubetas
inicio_tiempo = time.perf_counter()
v = bucket_sort(mi_lista.copy(), num_buckets=5)  # Usamos .copy() para no reutilizar la ordenada
fin_tiempo = time.perf_counter()
tiempo_total = fin_tiempo - inicio_tiempo

# Medición con 50 cubetas
inicio_tiempo_2 = time.perf_counter()
l = bucket_sort(mi_lista.copy(), num_buckets=50)
fin_tiempo_2 = time.perf_counter()
tiempo_total_2 = fin_tiempo_2 - inicio_tiempo_2

print(f"Tiempo con 5 cubetas:  {tiempo_total:.6f} segundos")
print(f"Tiempo con 50 cubetas: {tiempo_total_2:.6f} segundos")