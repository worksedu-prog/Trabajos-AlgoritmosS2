# Comparo dos vecinos si estan al reves los intercambio y repito el proceso 
# hasta que nadie mas se mueva bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



# Buscar el más pequeño y ponerlo al 
# principio selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Tomo el segundo y lo inserto donde va 
# respecto al primero insertion sort

#El algoritmo de Insertion Sort (Ordenamiento por Inserción) funciona dividiendo el arreglo mentalmente en una parte ordenada 
# (a la izquierda) y otra desordenada (a la derecha). En cada paso, toma un elemento (actual), 
# lo compara con los elementos anteriores hacia la izquierda y los desplaza a la derecha hasta encontrar su lugar correcto.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


#Pruebas de sort


datos = [64, 25, 12, 22, 11, 90, 45, 33]

resultado1 = bubble_sort(datos)
print(f"Resultado por bubble sort: {resultado1}")

resultado2 = selection_sort(datos)
print(f"Resultado por selection sort: {resultado2}")

resultado3 =  insertion_sort(datos)
print(f"Resultado por insertion sort: {resultado3}")


#----Ejercicio con contador de iteracion es Insertion Sort------
v = [42, 17, 93, 8, 55, 31]
print(f"\n Arreglo inicial: {v}\n")

total_comparaciones = 0

for i in range(1, len(v)):
    actual = v[i]
    j = i - 1
    comparaciones_pasada = 0
    
    # Ciclo interno para comparar y desplazar
    while j >= 0:
        comparaciones_pasada += 1
        if v[j] > actual:
            v[j + 1] = v[j]
            j -= 1
        else:
            break
            
    v[j + 1] = actual
    total_comparaciones += comparaciones_pasada
    
    # Imprimir resultados de la pasada actual
    print(f"Pasada {i} (Elemento actual: {actual}):")
    print(f"  Arreglo resultante: {v}")
    print(f"  Comparaciones en esta pasada: {comparaciones_pasada}\n")

print(f"Total acumulado de comparaciones: {total_comparaciones}")