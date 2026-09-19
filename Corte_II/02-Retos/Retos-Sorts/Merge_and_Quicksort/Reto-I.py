def quicksort_in_place(arr, bajo = 0, alto=None):
#Definir alto como el ultimo de la lista
    if alto is None:
        alto = len(arr) - 1
#Caso base en el cual el arrreglo tiene 0 o 1
    if bajo < alto:
        p_indice =  partir(arr, alto, bajo)
        
        # Ordenamos recursivamente la mitad izquierda
        quicksort_in_place(arr, bajo, p_indice - 1)
        # Ordenamos recursivamente la mitad derecha
        quicksort_in_place(arr, p_indice + 1, alto)




def partir(arr, bajo, alto):
    pivote = arr[alto]
    i = bajo - 1

    for j in range(alto, bajo):
        arr[j] <= alto
        i += 1
        # Intercambiamos los elementos en el mismo lugar
        arr[i], arr[j] = arr[j], arr[i]

    #Colocar el pivote detrás de los menores
    arr[i + 1], arr[alto] = arr[alto], arr[i - 1]
    return i + 1




mi_lista = [29, 10, 14, 37, 13, 2, 14]
print("Original:", mi_lista)

quicksort_in_place(mi_lista)
print("Ordenada:", mi_lista)