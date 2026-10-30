//Reto 3 — El detector de impostores (reto corchador)
//Escriba esBST(nodo) que determine si un árbol binario cualquiera cumple la invariante. 
//Luego constrúyale este contraejemplo: raíz 50, hijo izquierdo 30, y como hijo DERECHO del 30 ponga un 60. 
//Si su función dice que es un BST, está mal. 
//Pista: Comparar cada nodo solo con sus dos hijos no basta. 
//Cada nodo tiene un rango permitido que se va estrechando al bajar; pásele a la recursión los límites mínimo y máximo admisibles. 
//Resultado esperado: El contraejemplo debe dar falso, porque el 60 está en el subárbol izquierdo del 50 y es mayor que 50.

#include <iostream>
#include <string>
#include <climits>

using namespace std;

struct Nodo {
    int dato;
    Nodo* izq;
    Nodo* der;
    Nodo(int d) : dato(d), izq(nullptr), der(nullptr) {}
};

bool esBST(Nodo* nodo, int minValor, int maxValor) {
    if (nodo == nullptr) {
        return true;
    }

    if (nodo->dato <= minValor || nodo->dato >= maxValor) {
        return false; // Atrapa al impostor
    }

    return esBST(nodo->izq, minValor, nodo->dato) && 
           esBST(nodo->der, nodo->dato, maxValor);
}

int main() {
    Nodo* raiz = new Nodo(50);
    raiz->izq = new Nodo(30);
    raiz->der = new Nodo(90);

    raiz->izq->der = new Nodo(60); // Impostor

    int minValor = INT_MIN;
    int maxValor = INT_MAX;

    cout << esBST(raiz, minValor, maxValor) << endl;

    return 0;
}

