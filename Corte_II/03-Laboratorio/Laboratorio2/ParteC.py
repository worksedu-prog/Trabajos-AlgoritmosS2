# Parte C — Los tres ordenamientos básicos (30%) Implementen Bubble, 
# Selection e Insertion sobre sus registros, con contadores de comparaciones e intercambios. 
# Reporten los resultados con datos desordenados y con datos ya ordenados, y expliquen la diferencia.

import time #Libreria para el tiempo


def bubble_sort_comparaciones_e_intercambios(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0

    inicio_tiempo1 = time.perf_counter()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1  # Se realiza la comparación
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1  # Se realiza el intercambio
                swapped = True
        if not swapped:
            break

    fin_tiempo1 = time.perf_counter()

    total_tiempo1 = fin_tiempo1 - inicio_tiempo1
            
    return arr, comparaciones, intercambios, total_tiempo1


def selection_sort_comparaciones_e_intercambios(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0

    inicio_tiempo2 = time.perf_counter()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1  # Se compara para hallar el mínimo
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Solo intercambia si encontró un elemento menor en una posición distinta
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1

    fin_tiempo2 = time.perf_counter()

    total_tiempo2 = fin_tiempo2 - inicio_tiempo2

    return arr, comparaciones, intercambios, total_tiempo2


def insertion_sort_comparaciones_e_intercambios(arr):
    comparaciones = 0
    intercambios = 0  # En insertion sort representa los desplazamientos/asignaciones

    inicio_tiempo3 = time.perf_counter() #Tiempo de ejecución
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparaciones += 1  # Evaluación de la condición (arr[j] > key)
            if arr[j] > key:
                arr[j + 1] = arr[j]
                intercambios += 1  # Desplazamiento del elemento hacia la derecha
                j -= 1
            else:
                break
                
        arr[j + 1] = key

    fin_tiempo3 = time.perf_counter() #Fin del tiempo

    total_tiempo3 = fin_tiempo3 - inicio_tiempo3 #Obtener el tiempo total
        
    return arr, comparaciones, intercambios, total_tiempo3


#-----------Desordenados----------

# Pruebas
# Se usa el .copy() para no alterar datos, pues si se usa la misma lista todos la modificarian asi que .copy() es como "clonar"  la lista de datos 

desordenados = [64, 25, 12, 22, 11, 90, 45, 33]

res1, comp1, inter1, tiempo1 = bubble_sort_comparaciones_e_intercambios(desordenados.copy())
print(f"\nBubble Sort con comparaciones e intercambios desordenados = Lista: {res1} | Comparaciones: {comp1} | Intercambios: {inter1} | Tiempo {tiempo1:.10f} segundos")

# 2. Selection Sort desordenado
res2, comp2, inter2, tiempo2 = selection_sort_comparaciones_e_intercambios(desordenados.copy())
print(f"Selection Sort con comparaciones e intercambios desordenados = Lista: {res2} | Comparaciones: {comp2} | Intercambios: {inter2} | Tiempo {tiempo2:.10f} segundos")

# 3. Insertion Sort desordenado
res3, comp3, inter3, tiempo3 = insertion_sort_comparaciones_e_intercambios(desordenados.copy())
print(f"Insertion Sort con comparaciones e intercambios desordenados = Lista: {res3} | Comparaciones: {comp3} | Desplazamientos: {inter3} | Tiempo {tiempo3:.10f} segundos")

#-------------Ordenados--------------

ordenados = [24, 25, 37, 56, 84, 99, 100, 999]

res4, comp4, inter4, tiempo4 = bubble_sort_comparaciones_e_intercambios(ordenados.copy())
print(f"\nBubble Sort con comparaciones e intercambios ordenados = Lista: {res4} | Comparaciones: {comp4} | Intercambios: {inter4} | Tiempo {tiempo4:.10f} segundos")

#2. Selection sort ordenado 

res5, comp5, inter5, tiempo5 = selection_sort_comparaciones_e_intercambios(ordenados.copy())
print(f"Selection Sort con comparaciones e intercambios ordenados = Lista: {res5} | Comparaciones: {comp5} | Intercambios: {inter5} | Tiempo {tiempo5:.10f} segundos")

#3 Insertion sort desordenado
res6, comp6, inter6, tiempo6 = insertion_sort_comparaciones_e_intercambios(ordenados.copy())
print(f"Insertion Sort con comparaciones e intercambios ordenados= Lista: {res6} | Comparaciones: {comp6} | Intercambios: {inter6} | Tiempo {tiempo6:.10f} segundos")




# Explicación

# Bubble Sort:
# Desordenados: Realiza múltiples pasadas, comparaciones e intercambios hasta ordenar la lista con un Big O de (O(n^2))
# Ordenados: Gracias a la bandera swapped, en la primera pasada realiza n-1 comparaciones, detecta que no hubo ningún intercambio (0) y rompe el ciclo inmediatamente con su Big O es decir una constante (O(n))

# Selection Sort:
# Desordenados u Ordenados: Realiza exactamente el mismo número de comparaciones en ambos casos (O(n^2)) 
# Esto ocurre porque no tiene forma de saber si la lista ya está ordenada y siempre busca el elemento mínimo en el resto del arreglo. En datos ordenados, realiza 0 intercambios pero el mismo número de comparaciones.

# Insertion Sort (Como sabemos es el más eficiente para listas casi o totalmente ordenadas):
# Desordenados: Requiere comparar y desplazar elementos hacia la derecha para hacer espacio al nuevo elemento (O(n^2))
# Ordenados: En cada iteración solo realiza 1 comparación (la condición arr[j] > key da falso de inmediato) y 0 desplazamientos. Esto reduce su trabajo a n-1 comparaciones (O(n)) siendo una constante