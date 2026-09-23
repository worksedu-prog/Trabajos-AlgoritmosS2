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
