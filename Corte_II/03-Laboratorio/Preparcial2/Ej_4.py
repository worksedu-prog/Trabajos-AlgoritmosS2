#Ejercicio 4 · Detección de errores en búsqueda binaria  ·  Python  ·  (depuración) 
#Esta función falla en producción: con algunas entradas no termina nunca. Identifique el defecto, explique por qué se 
#produce el bucle infinito, corríjalo e indique la precondición que debe cumplir v. 

def buscar(v, x): 
    izq, der = 0, len(v) - 1 
    while izq <= der: 
        medio = (izq + der) // 2 
        if v[medio] == x: 
            return medio 
        elif v[medio] < x: 
            izq = medio   #(RTA: se le necesita +1 al lado izquierda)         # (1) 
        else: 
            der = medio  #(RTA: se le necesita  -1 al lado derecho)       
    return -1   # (2) 

v = [8, 15, 23, 31, 42, 56, 64, 77, 89, 91] 
x = 15
print(f"El elemento {x} se encuentra en la posición: {buscar(v, x)}")


#1.Rta: Como izq y derecha no cambian el del medio sigue igual y por lo tanto queda en un bucle infinito
#2.Rta: La precondición que se debe cumplir es que sea ordenado pues si la lista no es ordenada el algoritmo de busqueda binaria se estalla