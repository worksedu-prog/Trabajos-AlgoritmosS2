#Un arbol es balanceado si maximo la diferencia entre las alturas de sus subarboles es de 1
#Se calcula con 1.44(long2 N)

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None

# Balanceo de árboles: introducción y rotaciones AVL
def alt(n):
    return -1 if n is None else n.alt      # arbol vacio: -1
 
def fe(n):                                  # factor de equilibrio
    return 0 if n is None else alt(n.izq) - alt(n.der)
 
def recalc(n):
    n.alt = 1 + max(alt(n.izq), alt(n.der))