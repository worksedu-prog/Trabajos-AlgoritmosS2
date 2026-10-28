//Reto 2 — El espejo Escriba espejo(nodo) que intercambie el hijo izquierdo y el derecho de TODOS los nodos del árbol. 
//Luego imprima el inorden del árbol original y el del árbol espejado

#include <iostream>
#include <string>

using namespace std;

struct Nodo {
    string dato;
    Nodo* der;
    Nodo* izq;
    Nodo(string d) : dato(d), izq(nullptr), der(nullptr) {} //Constructor
};

void espejo(Nodo* nodo){
    if (nodo == nullptr){
        return;}

    swap(nodo->izq, nodo->der); //Swap es una función que cambia de posición l

    espejo(nodo->izq);
    espejo(nodo->der);
}  

void inorden(Nodo* nodo){ //Función inorden del árbol original
    if (nodo == nullptr){return;}

    inorden(nodo->izq);
    cout << nodo->dato << " ";
    inorden(nodo->der);
}

int main() {
    Nodo* raiz = new Nodo("Agua");
    raiz->izq = new Nodo("Fuego");  
    raiz->der = new Nodo("Aire");
    raiz->der->izq = new Nodo("Tierra");    
    raiz->der->der = new Nodo("Cemento");

    //Imprimime el inorden del árbol original
    cout << "Inorden original: ";
    inorden(raiz);
    cout << endl;

    //Imprime la función espejo
    espejo(raiz);

    // 3. Imprimimos el inorden después de aplicar el espejo
    cout << "Inorden espejado: ";
    inorden(raiz);
    cout << endl;

    return 0;
}