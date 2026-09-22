# Construyan un caso que haga que su Quicksort se comporte pésimo. 
# Si escogen el primer elemento como pivote, una lista ya ordenada lo logra. Mídanlo.


import time
import sys

# Aumentamos el límite de 1000 a 3000 llamadas recursivas
sys.setrecursionlimit(3000)


def quicksort_in_place(arr, bajo = 0, alto=None):
#Definir alto como el ultimo de la lista
    if alto is None:
        alto = len(arr) - 1
#Caso base en el cual el arrreglo tiene 0 o 1
    if bajo < alto:
        p_indice =  partir(arr, bajo, alto)
        
        # Ordenamos recursivamente la mitad izquierda
        quicksort_in_place(arr, bajo, p_indice - 1)
        # Ordenamos recursivamente la mitad derecha
        quicksort_in_place(arr, p_indice + 1, alto)




def partir(arr, bajo, alto):
    pivote = arr[bajo]    #El pivote ahora sera el primero
    i = bajo - 1

    for j in range(bajo + 1, alto +1):
        arr[j] <= alto
        i += 1
        # Intercambiamos los elementos en el mismo lugar
        arr[i], arr[j] = arr[j], arr[i]

    #Colocar el pivote detrás de los menores
    arr[bajo], arr[i] = arr[i], arr[bajo]
    return i



 #Lista ordenada para el peor caso en un rango de 30 datos

mi_lista = list(range(700))  #Materializa una secuencia de datos en una lista
inicio_time = time.perf_counter()
quicksort_in_place(mi_lista)
fin_time = time.perf_counter()

tiempo_final = fin_time - inicio_time

print(f"El tiempo en ordenar la lista en el peor caso es de: {tiempo_final:.8f} segundos")