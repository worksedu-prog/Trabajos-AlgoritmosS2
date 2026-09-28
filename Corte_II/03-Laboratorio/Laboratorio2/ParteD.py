import time
import random

# 1. Algoritmo Básico: Selection_sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 2. Algoritmo Avanzado: Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Medición para 3 tamaños de entrada distintos
tamaños = [1000, 5000, 10000]

print(f"{'Tamaño (n)':<12} | {'Selección (s)':<15} | {'Quicksort (s)':<15}")
print("-" * 48)

for n in tamaños:
    datos = [random.randint(1, 100000) for i in range(n)]
    
    # Medir Selección
    copia_sel = datos.copy()
    inicio = time.perf_counter()
    selection_sort(copia_sel)
    tiempo_sel = time.perf_counter() - inicio
    
    # Medir Quicksort
    copia_quick = datos.copy()
    inicio = time.perf_counter()
    quicksort(copia_quick)
    t_quick = time.perf_counter() - inicio
    
    print(f"{n:<12} | {tiempo_sel:<15.4f} | {t_quick:<15.4f}")