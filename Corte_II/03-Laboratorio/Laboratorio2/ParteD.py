import time

pruebas = [
    (12324638621, "Julian"), (100372362754, "Isabella"), (14527463725, "Enrique"),
    (67670932176563, "Paulo"), (1021837261873, "Sofia"), (405387126, "Jose"),
    (150183721665, "Lopez"), (145035427168, "Fernando"), (10138726318, "Fernanda")
]

# 1. Algoritmo Básico: Selection sort (ordena la misma lista que recibe)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # comparo por el número, que es la posición 0 de cada par
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 2. Algoritmo Avanzado: Quicksort (devuelve una lista nueva)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0]
    left = [x for x in arr if x[0] < pivot]
    middle = [x for x in arr if x[0] == pivot]
    right = [x for x in arr if x[0] > pivot]
    return quicksort(left) + middle + quicksort(right)

# Medir Selección
copia_sel = pruebas.copy()
inicio = time.perf_counter()
selection_sort(copia_sel)
tiempo_sel = time.perf_counter() - inicio

# Medir Quicksort
inicio = time.perf_counter()
ordenado_quick = quicksort(pruebas.copy())
t_quick = time.perf_counter() - inicio

# Resultados
print("Lista ordenada con Selección:")
for num, nombre in copia_sel:
    print(f"{num:<16} {nombre}")

print("\nLista ordenada con Quicksort:")
for num, nombre in ordenado_quick:
    print(f"{num:<16} {nombre}")

print(f"\n{'Algoritmo':<12} | {'Tiempo (s)':<12}")
print("-" * 27)
print(f"{'Selección':<12} | {tiempo_sel:<12.8f}")
print(f"{'Quicksort':<12} | {t_quick:<12.8f}")