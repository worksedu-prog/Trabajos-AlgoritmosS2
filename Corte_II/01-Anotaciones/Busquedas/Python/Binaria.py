def binaria(v, x):
    # Inicializan los limites siendo izquierda en el inicio y derecha en el final del vector
    izq, der = 0, len(v) - 1
    
    # Mientras el subarreglo de búsqueda sea válido (no se hayan cruzado los índices)
    while izq <= der:
        # Calculamos el índice del punto medio
        medio = (izq + der) // 2
        
        # Si el elemento del medio es el valor buscado, retornamos su índice
        if v[medio] == x: 
            return medio
        # Si el valor del medio es menor que 'x', buscamos en la mitad derecha
        elif v[medio] < x: 
            izq = medio + 1
        # Si el valor del medio es mayor que 'x', buscamos en la mitad izquierda
        else: 
            der = medio - 1
            
    #Se retorna -1 si el elemento no se encuentra en el vector
    return -1

# Vector ordenado sobre el cual se realizará la búsqueda
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 8

print("Búsqueda binaria")
print(f"El vector de búsqueda es: {v}")

#len(v) muestra el tamaño del vector (9 elementos).
print(f"Tamaño del vector: {len(v)}")

# Llamada a la función e impresión del resultado final
print(f"El elemento {x} se encuentra en la posición: {binaria(v, x)}")
