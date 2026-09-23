
import time



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

    inicio_tiempo3 = time.perf_counter()
    
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

    fin_tiempo3 = time.perf_counter()

    total_tiempo3 = fin_tiempo3 - inicio_tiempo3
        
    return arr, comparaciones, intercambios, total_tiempo3


# Pruebas
#Se usa .copy() para no alterar datos, pues si se usa la misma lista todos la modificarian asi que .copy() es como "clonar" datos 

datos = [64, 25, 12, 22, 11, 90, 45, 33]

res1, comp1, inter1, tiempo1 = bubble_sort_comparaciones_e_intercambios(datos.copy())
print(f"\nBubble Sort con comparaciones e intercambios = Resultado: {res1} | Comparaciones: {comp1} | Intercambios: {inter1} | Tiempo {tiempo1:.10f} milisegundos")

# 2. Selection Sort
res2, comp2, inter2, tiempo2 = selection_sort_comparaciones_e_intercambios(datos.copy())
print(f"Selection Sort con comparaciones e intercambios = Resultado: {res2} | Comparaciones: {comp2} | Intercambios: {inter2} | Tiempo {tiempo2:.10f} milisegundos")

# 3. Insertion Sort
res3, comp3, inter3, tiempo3 = insertion_sort_comparaciones_e_intercambios(datos.copy())
print(f"Insertion Sort con comparaciones e intercambios = Resultado: {res3} | Comparaciones: {comp3} | Desplazamientos: {inter3} | Tiempo {tiempo3:.10f} milisegundos")