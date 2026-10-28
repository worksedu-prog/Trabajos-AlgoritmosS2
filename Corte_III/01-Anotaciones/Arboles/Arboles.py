#El árbol es una estructura no lineal teniendo muchos caminos para resolver una necesidad, almacena datos de manera jerárquica. 
# Cada elemento del árbol se llamada nodo, y cada nodo puede tener cero o más nodos hijos. El nodo superior se llama raíz, y los nodos sin hijos se llaman hojas
#La diferencia entre árbol binario y el árbol normal, es que le árbol normal puede tener n cantidades de nodos, mientras que el binario máximo tiene dos nodos
#Raíz: Nodo principal del árbol
#Nodo: Cada elemento que almacena datos y puede tener hijos
#Padre e hijo: Relación que hay entre nodos, donde un padre puede tener uno o más hijos
#Hojas: Nodos que no tienen hijos, pero están conectados a otros nodos


#Ejemplo de nodo binario:

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Crear la raíz y los primeros nodos
raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)