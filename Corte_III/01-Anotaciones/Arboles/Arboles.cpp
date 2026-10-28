/*## Arbol, es una estructura no lineal que permite
# almacenar datos de manera jerárquica. 
# Cada elemento del árbol se llama nodo,
# y cada nodo puede tener cero o más nodos hijos.
# El nodo superior se llama raíz, 
# y los nodos sin hijos se llaman hojas.
# Raiz: Nodo principal del árbol.
# Nodo: cada elemento que almacena datos
# y puede tener hijos.
#ºPadre e hijo: Relación entre nodos, 
# donde un nodo padre tiene uno o más nodos hijos.
#hojas: Nodos que no tienen hijos.
#aristas: Conexiones entre nodos,
# que representan la relación padre-hijo.
tipos:
1. arbol: cada nodo puede tener un número variable de hijos
2. binario: cada nodo puede tener como máximo dos hijos
3. busqueda binaria: árbol binario con la propiedad de que
 para cada nodo, todos los valores en el subárbol 
 izquierdo son menores que el valor del nodo, 
 y todos los valores en el subárbol derecho son
  mayores que el valor del nodo*/

  // Ejemplo  de arbol binario
  struct Nodo {
    int dato;
    Nodo* izquierdo;
    Nodo* derecho;

    // Constructor
    Nodo(int valor) {
        dato = valor;
        izquierdo = nullptr;
        derecho = nullptr;
    }
};
