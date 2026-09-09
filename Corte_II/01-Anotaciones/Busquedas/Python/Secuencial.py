# Búsqueda secuencial PARA NÚMEROS EN DESORDEN
def busqueda_secuencial(v, x): # Declara la función que recibe el vector 'v' y el elemento a buscar 'x'
    for i in range(len(v)): # Recorre los índices 'i' desde 0 hasta el tamaño del vector menos 1
        if v[i] == x: # Si el elemento en la posición 'i' es igual a 'x'
            return i # Devuelve el índice 'i' donde se encontró el elemento
    return -1 # Devuelve -1 si el elemento 'x' no existe en el vector

v = [123, 45, 576, 678, 34, 23, 12, 90] # Vector de prueba desordenado
x = 123 # Dato a encontrar

print("Búsqueda secuencial")
print(f"El vector de búsqueda es: {v}") # Imprime el vector en el que va a buscar
print(f"El elemento {x} se encuentra en la posición: {busqueda_secuencial(v, x)}") 

# Nota: len(v) representa el tamaño total del vector (peor caso posible), no los pasos reales ejecutados.
print(f"Tamaño del vector (máximo de pasos posibles): {len(v)}")
