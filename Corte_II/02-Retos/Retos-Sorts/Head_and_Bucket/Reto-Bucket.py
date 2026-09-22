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
            index = num_buckets - 1
        buckets[index].append(num)

    # Ordenar individualmente cada cubeta y unir los resultados en una sola lista
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Utiliza el ordenamiento ´sorted()´ para sublistas pequeñas

    return sorted_arr

#Medicion del tiempo

#-------5 CUBETAS-------

inicio_tiempo = time.perf_counter()


mi_lista = [0.43, 567, 8739, 83, 9]



v = bucket_sort(mi_lista.copy(), num_buckets=5)

fin_tiempo = time.perf_counter()
tiempo_total = fin_tiempo - inicio_tiempo

print(f"Ordenamiento de lista apartir de 5 cubetas con bucket_sort {v} con un tiempo de {tiempo_total:.8f} ")



#---------50 CUBETAS----------

inicio_tiempo_2 = time.perf_counter()

l = bucket_sort(mi_lista.copy(), num_buckets=50)

fin_tiempo_2 = time.perf_counter()
tiempo_total_2 = fin_tiempo_2 - inicio_tiempo_2

print(f"Ordenamiento de lista apartir de 50 cubetas con bucket_sort {l} con un tiempo de {tiempo_total_2:.8f} ")



#El punto optimo es más cercano si es igual al número de datos que tiene mi lista. 
#Para alcanzar el estado optimo el  num.datos_de_mi_lista = num.de_cubetas


#Pues si se agregan demasiadas cubetas en una lista de pocos datos (o viceversa en ambos casos) 
#Se realizara una degeneración debido a la desproporcionalidad de la cantidad de ambas variables


