#include <iostream>
#include <string>

  struct Nodo {
    int clave;
    Nodo* izq;
    Nodo* der;

    // Constructor
    Nodo(int valor) {
        clave = valor;
        izq = nullptr;
        der = nullptr;
    }
};


    Nodo* insertar(Nodo* n, int clave) {
        if (n == nullptr) return new Nodo(clave);
        if (clave < n->clave)      n->izq = insertar(n->izq, clave);
        else if (clave > n->clave) n->der = insertar(n->der, clave);
        return n;                        // clave repetida: no se inserta
    }