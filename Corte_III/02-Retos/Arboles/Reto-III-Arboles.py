#Reto 3 — ¿Son iguales? (reto corchador) Escriba sonIguales(a, b) que devuelva verdadero si dos árboles 
# tienen la misma forma Y los mismos datos en las mismas posiciones. 
#Pruébelo con el árbol original contra su propio espejo: debe dar falso.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def sonIguales (nodo_a , nodo_b):
    if nodo_a == None and nodo_b != None:
        return False

    elif nodo_b == None and nodo_a != None:
        return False
    
    elif nodo_a == None and nodo_b == None:
        return True
    
    elif nodo_a.dato == nodo_b.dato: #Si los datos son iguales
        return sonIguales(nodo_a.izq, nodo_b.izq) and sonIguales(nodo_a.der, nodo_b.der) #Compara los hijos de cada uno
    else:
        return False


# Crear un arbol 
raiz = Nodo("CATALOGO")
raiz.izq = Nodo("HERRAMIENTA"); raiz.der = Nodo("LIBRO")

# Creamos otro árbol o una copia de este
raiz2 = Nodo("CATALOGO")
raiz2.izq = Nodo("HERRAMIENTA"); raiz2.der = Nodo("LIBRO")

# 1. Árboles iguales (debe dar True)
print(sonIguales(raiz, raiz2)) 

# 2. Árbol original contra su propio espejo (debe dar False)
arbol_espejo = Nodo("CATALOGO")
arbol_espejo.izq = Nodo("LIBRO"); arbol_espejo.der = Nodo("HERRAMIENTA")

print(sonIguales(raiz, arbol_espejo))