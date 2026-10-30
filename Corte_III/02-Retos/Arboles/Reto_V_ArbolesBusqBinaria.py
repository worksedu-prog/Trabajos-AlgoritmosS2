#Reto 3 — El detector de impostores (reto corchador)
#Escriba esBST(nodo) que determine si un árbol binario cualquiera cumple la invariante. 
#Luego constrúyale este contraejemplo: raíz 50, hijo izquierdo 30, y como hijo DERECHO del 30 ponga un 60. 
#Si su función dice que es un BST, está mal. 
#Pista: Comparar cada nodo solo con sus dos hijos no basta. 
#Cada nodo tiene un rango permitido que se va estrechando al bajar; pásele a la recursión los límites mínimo y máximo admisibles. 
#Resultado esperado: El contraejemplo debe dar falso, porque el 60 está en el subárbol izquierdo del 50 y es mayor que 50.

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None

def esBST(nodo, minValor, maxValor):
    if nodo is None: return True
    if nodo.dato <= minValor or nodo.dato >= maxValor: return False

    return esBST(nodo.izq, minValor, nodo.dato) and esBST(nodo.der, nodo.dato, maxValor)


raiz = Nodo(50)
raiz.izq = Nodo(30)
raiz.der = Nodo(90)

raiz.izq.der = Nodo(60)

#Usa limites

minValor = float('-inf') #Infinitamente negativo
maxValor = float('inf') #Infinitamente positivo

print(f"{esBST(raiz, minValor, maxValor)}")