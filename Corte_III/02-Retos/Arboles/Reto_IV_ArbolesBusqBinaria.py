#Reto 2 — El rango · Obligatorio Escriba enRango(nodo, a, b) que imprima todas las claves entre a y b, 
#ambas incluidas, en orden ascendente. La gracia está en que NO debe visitar todo el árbol: 
#si la clave del nodo es menor que a, no tiene sentido bajar por la izquierda. 
#Pista: Es un inorden con dos podas. Agregue un contador de nodos visitados y compare contra el total del árbol: debe ser menor. 
#Resultado esperado: Con el árbol del ejemplo y el rango [35, 65], debe imprimir 35, 40, 50, 60 visitando menos de 8 nodos.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def enRango(nodo, a, b):
    if nodo is None:
        return
    if nodo.dato > a: enRango(nodo.izq, a, b)
    if a <= nodo.dato and nodo.dato <= b: print(f"{nodo.dato}")
    if nodo.dato < b: enRango(nodo.der, a, b)

# Árbol Binario de Búsqueda de prueba:
#          50
#        /    \
#      30      70
#     /  \    /  \
#    20  40  60  80
#       /
#      35

raiz = Nodo(50)
raiz.izq = Nodo(30)
raiz.der = Nodo(70)

raiz.izq.izq = Nodo(20)
raiz.izq.der = Nodo(40)
raiz.izq.der.izq = Nodo(35)

raiz.der.izq = Nodo(60)
raiz.der.der = Nodo(80)

a = 35
b = 65

print(f"Claves en el rango [{a},{b}] \n")
enRango(raiz, a, b)
print("")
