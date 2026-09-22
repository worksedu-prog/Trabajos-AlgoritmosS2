#Implementen Heapsort de mínimos en vez de máximos, y dígan qué cambió.

#def heapify(arr, n, i):
#    largest = i          # Inicializa el nodo actual como el más grande
#    left = 2 * i + 1     # Hijo izquierdo en representación de árbol basada en arreglo
#    right = 2 * i + 2    # Hijo derecho

#    # Si el hijo izquierdo existe y es mayor que el elemento actual
#    if left < n and arr[left] > arr[largest]:
#        largest = left

#    # Si el hijo derecho existe y es mayor que el elemento actual
#    if right < n and arr[right] > arr[largest]:
#        largest = right

#    # Si el nodo más grande no es la raíz actual, se intercambian y se aplica heapify recursivo
#    if largest != i:
#        arr[i], arr[largest] = arr[largest], arr[i]
#        heapify(arr, n, largest)

## Función principal de HeapSort
#def heap_sort(arr):
#    n = len(arr)

#    # 1. Construir el Max-Heap (reorganiza el arreglo)
#    for i in range(n // 2 - 1, -1, -1):
#        heapify(arr, n, i)

#    # 2. Extraer elementos uno por uno del montículo
#    for i in range(n - 1, 0, -1):
#        # Mueve la raíz actual (máximo) al final del arreglo
#        arr[i], arr[0] = arr[0], arr[i]
#        # Aplica heapify en el árbol reducido
#        heapify(arr, i, 0)
        
#    return arr



#Implementen Heapsort de mínimos en vez de máximos, y dígan qué cambió.

def heapify(arr, n, i):
    smallest = i          # Inicializa el nodo actual como el más pequeño
    left = 2 * i + 1     # Hijo izquierdo en representación de árbol basada en arreglo
    right = 2 * i + 2    # Hijo derecho

    # Si el hijo izquierdo existe y es menor que el elemento actual
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Si el hijo derecho existe y es menor que el elemento actual
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Si el nodo más pequeño no es la raíz actual, se intercambian y aplicamos recursión
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

# Función principal de HeapSort de Minimos
def heap_sort(arr):
    n = len(arr)

    # 1. Construir el Min-Heap (reorganiza el arreglo)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. Extraer elementos uno por uno del montículo
    for i in range(n - 1, 0, -1):
        # Mueve la raíz actual (minimo) al final del arreglo
        arr[i], arr[0] = arr[0], arr[i]
        # Aplica heapify en el árbol reducido
        heapify(arr, i, 0)
        
    return arr



mi_lista = [12, 3, 4, 6, 7]

print(f"Su lista organizada por heap_sort de minimos es: {heap_sort(mi_lista)}")


#Cambios:
#La variable largest cambia a smallest 

#Operadores de comparación:
#En heapify, cambió arr[left] > arr[largest] por arr[left] < arr[smallest].
#Cambió arr[right] > arr[largest] por arr[right] < arr[smallest]

#La raíz del montículo (arr[0]) pasa a ser siempre el elemento mínimo en lugar del máximo
#Max-Heap: Extrae el mayor y lo manda al final. Ordenando de Menor a Mayor (Ascendente)
#Min-Heap: Extrae el menor y lo manda al final. Ordenando de Mayor a Menor (Descendente).