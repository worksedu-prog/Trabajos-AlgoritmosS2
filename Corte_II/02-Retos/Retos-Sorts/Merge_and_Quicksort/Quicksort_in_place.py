def quicksort_in_place(arr, bajo=0, alto=None):
    # Definir alto como el último índice de la lista
    if alto is None:
        alto = len(arr) - 1

    # Caso base: detenerse cuando el subarreglo tenga 0 o 1 elementos
    if bajo < alto:
        p_indice = partir(arr, bajo, alto)

        # Ordenamos recursivamente la mitad izquierda
        quicksort_in_place(arr, bajo, p_indice - 1)
        # Ordenamos recursivamente la mitad derecha
        quicksort_in_place(arr, p_indice + 1, alto)


def partir(arr, bajo, alto):
    pivote = arr[alto]  # Elegimos el último como pivote
    i = bajo - 1

    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            # Intercambiamos los elementos en el mismo lugar
            arr[i], arr[j] = arr[j], arr[i]

    # Colocar el pivote justo después de los menores
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1


# --- Prueba ---
mi_lista = [29, 10, 14, 37, 13, 2, 14]
print("Original:", mi_lista)

quicksort_in_place(mi_lista)
print("Ordenada:", mi_lista)