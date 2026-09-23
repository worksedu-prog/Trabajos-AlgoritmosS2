

import time



# ==========================================
# 1. MERGE SORT: Divide la lista por la mitad de manera recursiva hasta tener sublistas de un solo elemento (las cuales ya se consideran ordenadas). 
# Luego, compara los elementos de las sublistas y los recombina (merge) de forma ordenada hacia arriba
# Complejidad: O(n log n) en todos los casos
# ==========================================
def merge_sort(arr):


    inicio_tiempo = time.perf_counter()

    # Caso base: Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) > 1:
        # Encuentra el punto medio de la lista
        mid = len(arr) // 2
        
        # Divide la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamadas recursivas para ordenar cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Índices para recorrer:
        # i -> left_half, j -> right_half, k -> lista principal (arr)
        i = j = k = 0

        # Mezcla (merge) las dos sublistas de forma ordenada
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Si quedaron elementos restantes en left_half, se agregan al final
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Si quedaron elementos restantes en right_half, se agregan al final
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    fin_tiempo = time.perf_counter()
    total_tiempo = fin_tiempo - inicio_tiempo
            
    return arr, total_tiempo


# ==========================================
# 2. QUICKSORT: Selecciona un valor conocido como pivote. Clasifica todos los demás elementos en tres grupos: menores que el pivote, 
# iguales al pivote y mayores que el pivote. Luego aplica el mismo proceso recursivamente a las sublistas de menores y mayores.
# Complejidad: O(n log n) promedio, O(n²) peor caso
# ==========================================
def quick_sort(arr):
    # Caso base: Si la lista tiene 1 elemento o menos, retorna la lista
    if len(arr) <= 1:
        return arr
    else:
        # Selección del pivote (en este caso, el elemento central)
        pivot = arr[len(arr) // 2]
        
        # Partición de la lista mediante comprensión de listas:
        left = [x for x in arr if x < pivot]      # Elementos menores al pivote
        middle = [x for x in arr if x == pivot]   # Elementos iguales al pivote
        right = [x for x in arr if x > pivot]     # Elementos mayores al pivote
        
        # Llamada recursiva en sublistas izquierda y derecha, luego concatena
        return quick_sort(left) + middle + quick_sort(right)


# ==========================================
# 3. HEAPSORT: Modela el arreglo como un árbol binario completo denominado Max-Heap (donde cada padre es mayor o igual que sus hijos).
# Complejidad: O(n log n)
# ==========================================

# Función auxiliar para mantener la propiedad del Max-Heap (Montículo Máximo)
def heapify(arr, n, i):
    largest = i          # Inicializa el nodo actual como el más grande
    left = 2 * i + 1     # Hijo izquierdo en representación de árbol basada en arreglo
    right = 2 * i + 2    # Hijo derecho

    # Si el hijo izquierdo existe y es mayor que el elemento actual
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho existe y es mayor que el elemento actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo más grande no es la raíz actual, se intercambian y se aplica heapify recursivo
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Función principal de HeapSort
def heap_sort(arr):
    n = len(arr)

    # 1. Construir el Max-Heap (reorganiza el arreglo)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. Extraer elementos uno por uno del montículo
    for i in range(n - 1, 0, -1):
        # Mueve la raíz actual (máximo) al final del arreglo
        arr[i], arr[0] = arr[0], arr[i]
        # Aplica heapify en el árbol reducido
        heapify(arr, i, 0)
        
    return arr


# ==========================================
# 4. BUCKET SORT: Divide el rango de valores en intervalos o "cubetas" (buckets). 
# Clasifica cada número en su cubeta correspondiente, ordena cada cubeta por separado (aquí usando sorted()) y finalmente concatena todas las cubetas en orden.
# Complejidad: O(n + k) promedio (asumiendo distribución uniforme)
# ==========================================
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determinar los valores mínimo y máximo para definir el rango de distribución
    min_value = min(arr)
    max_value = max(arr)
    
    # Manejo de caso borde: si todos los números son iguales
    if min_value == max_value:
        return arr

    # Calcular el tamaño del rango que cubrirá cada cubeta (bucket)
    bucket_range = (max_value - min_value) / len(arr)

    # Crear 'n' cubetas vacías
    buckets = [[] for i in range(len(arr))]

    # Distribuir los elementos del arreglo dentro de las cubetas correspondientes
    for num in arr:
        index = int((num - min_value) / bucket_range)
        # Ajuste para evitar desbordamiento de índice en el elemento máximo
        if index == len(arr):
            index -= 1
        buckets[index].append(num)

    # Ordenar individualmente cada cubeta y unir los resultados en una sola lista
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Utiliza el ordenamiento ´sorted()´ para sublistas pequeñas

    return sorted_arr



mi_lista_prueba = [21, 434, 464, 7594]
arr_1, t1 = merge_sort(mi_lista_prueba.copy()) 
print(f"Ordenamiento por merge_sort con tiempo de {t1:.8f} ordenado de {arr_1}")