#SumaLista recursiva. Reciba una lista y devuelva la suma de sus elementos, sin ciclos. 
# Piensar en la definición recursiva de una lista, la que dijimos al principio: una lista es un elemento seguido de una lista.


def sumaLista(lista):
    # Caso Base: Si la lista está vacía, no hay nada que sumar y devolvemos 0.
    # Esto evita que la función siga llamándose a sí misma infinitamente.
    if len(lista) == 0:
        return 0
    
    # Caso Recursivo: Tomamos el primer elemento (lista[0]) y se lo sumamos
    # al resultado de llamar a sumaLista con el resto de los elementos (lista[1:]).
    else:
        return lista[0] + sumaLista(lista[1:])

# Ejemplo de uso:
mi_lista = [3, 5, 2]
resultado = sumaLista(mi_lista)
print(f"La suma de la lista es: {resultado}")  # Imprime: 10