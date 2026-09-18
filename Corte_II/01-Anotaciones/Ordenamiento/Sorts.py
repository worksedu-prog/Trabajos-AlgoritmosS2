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


# Tomo el segubndo y lo inserto donde va 
# respecto al primero insertion sort

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

#-----------------------------------------------------------------------------------------------------------------


def bubble_sort_comparaciones_e_intercambios(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    
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
            
    return arr, comparaciones, intercambios


def selection_sort_comparaciones_e_intercambios(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    
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
            
    return arr, comparaciones, intercambios


def insertion_sort_comparaciones_e_intercambios(arr):
    comparaciones = 0
    intercambios = 0  # En insertion sort representa los desplazamientos/asignaciones
    
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
        
    return arr, comparaciones, intercambios


# Pruebas parte 2
#Se usa .copy() para no alterar datos, pues si se usa la misma lista todos la modificarian asi que .copy() es como "clonar" datos 

datos = [64, 25, 12, 22, 11, 90, 45, 33]

# 1. Bubble Sort (usamos .copy() para no alterar 'datos')
res1, comp1, inter1 = bubble_sort_comparaciones_e_intercambios(datos.copy())
print(f"\nBubble Sort con comparaciones e intercambios = Resultado: {res1} | Comparaciones: {comp1} | Intercambios: {inter1}")

# 2. Selection Sort
res2, comp2, inter2 = selection_sort_comparaciones_e_intercambios(datos.copy())
print(f"Selection Sort con comparaciones e intercambios = Resultado: {res2} | Comparaciones: {comp2} | Intercambios: {inter2}")

# 3. Insertion Sort
res3, comp3, inter3 = insertion_sort_comparaciones_e_intercambios(datos.copy())
print(f"Insertion Sort con comparaciones e intercambios = Resultado: {res3} | Comparaciones: {comp3} | Desplazamientos: {inter3}")