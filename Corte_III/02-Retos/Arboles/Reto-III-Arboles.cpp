//Reto 3 — ¿Son iguales? (reto corchador) Escriba sonIguales(a, b) que devuelva verdadero si dos árboles 
//tienen la misma forma Y los mismos datos en las mismas posiciones. 
//Pruébelo con el árbol original contra su propio espejo: debe dar falso.

#include <iostream>
#include <string>

using namespace std;

struct Nodo {
    string dato;
    Nodo* der;
    Nodo* izq;
    Nodo(string d) : dato(d), izq(nullptr), der(nullptr) {} //Constructor
};

bool sonIguales(Nodo* a, Nodo* b){
    if (a == nullptr && b != nullptr) {
        return false;
    }
    else if (b == nullptr && a != nullptr) {
        return false;
    }
    else if (a == nullptr && b == nullptr){
        return true;
    }
    else if (a->dato == b->dato){ //Si los datos son iguales
        return sonIguales(a->izq, b->izq) && sonIguales(a->der, b->der); //Compara los hijos de cada uno
    } else {
        return false;
    }
}