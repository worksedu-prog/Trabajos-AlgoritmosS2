#Un arbol binario de búsqueda: todas las claves del subarbol izquierdo deben ser menores que las claves
# del derecho deben ser mayores

#Ejemplo de lo que NO se puede hacer
#         10
#        /  \
#       5    15
#      /
#     17

#Si un arbol ya esta en inorden NO se debe ordenar
#Si hay llaves duplicadas se guardan a la derecha con un contador o se eliminan
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
        
def insertar(n, clave):
    if n is None:                     # llegamos a un hueco: aqui va
        return Nodo(clave)
    if clave < n.clave:
        n.izq = insertar(n.izq, clave)   # el retorno se REENGANCHA
    elif clave > n.clave:
        n.der = insertar(n.der, clave)
    return n                           # clave repetida: no se inserta
# eliminar nodo (hoja) se boraa y su lugar queda nulo
# el nodo tiene un hijo el hijo debe subir aocupar el lugar del padre y el subarblo se reengancha al abuelo
# el nodo tiene dos hijos se busca un sucesor inorden (minimo del subarbol derecho) secopia la clave
# en  el nodo y se elimina el sucesor inorden (que es hoja o tiene un hijo derecho)