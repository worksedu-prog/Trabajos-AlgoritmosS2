#Complejidad es la medida de los recursos que requiere un algoritmo o programa para resolver un problema

# Big O: es una herramienta matemática y teórica que sirve para medir la eficiencia de un algoritmo, 
# describiendo cómo aumentan sus necesidades de tiempo o memoria a medida que el tamaño de los datos de entrada crece hacia el infinito.


#Tipos de Big O:

# O(1) - constante no cambia con el tamaño de la entrada v[i]
# O(log n) - logaritmica, divide el problema en partes iguales,busqueda binaria (sube uno o dos pasos mas)
# O(n) - lineal, recorre todos los elementos de la entrada, busqueda secuencial(se dobla) recorrer lista enlazada
# O(n log n) - logaritmica lineal, divide el problema en partes iguales y recorre todos los elementos de la entrada, mergesort, quicksort (un poco mas del doble)
# O(n^2) - cuadratica, recorre todos los elementos de la entrada y para cada elemento recorre todos los elementos de la entrada, bubble sort, selection sort, insertion sort (cuadruplica)
#Regla 1: se ignoran las constantes y los terminos de menor orden
#regla 2: manda terminos quemás crece.
