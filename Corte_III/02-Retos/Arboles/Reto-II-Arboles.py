#Reto 2 — El espejo Escriba espejo(nodo) que intercambie el hijo izquierdo y el derecho de TODOS los nodos del árbol. 
#Luego imprima el inorden del árbol original y el del árbol espejado

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def espejo(nodo):
    if nodo == None:
        return

    #Primero recursividad para no intercambiar dos veces, por ejemplo:
    # 1. nodo.izq, nodo.der = nodo.der, nodo.izq
    # espejo(nodo.der)
    # espejo(nodo.izq)
    #Haria que se intercambaiaran dos veces

    espejo(nodo.der)
    espejo(nodo.izq)

    nodo.izq, nodo.der = nodo.der, nodo.izq #Cambian de posición


def inorden(nodo):
    if nodo == None:
        return
    
    inorden(nodo.izq)
    print( "" + nodo.dato)
    inorden(nodo.der)



raiz = Nodo("CATALOGO")
raiz.izq = Nodo("HERRAMIENTA"); raiz.der = Nodo("LIBRO")
raiz.izq.izq = Nodo("TALADRO");  raiz.izq.der = Nodo("SIERRA")
raiz.der.izq = Nodo("ARTE");     raiz.der.der = Nodo("TECNICO")
raiz.der.der.der = Nodo("REDES")

espejo(raiz)
print("\n")
inorden(raiz)