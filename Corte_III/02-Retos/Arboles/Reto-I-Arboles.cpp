//Reto 1 — El catálogo que se imprime solo Escriba una función imprimirJerarquia(nodo, nivel) 
//que recorra el árbol en preorden e imprima cada nombre con dos espacios de sangría por nivel, 
//de modo que el resultado se vea como un índice de documento. Debe funcionar para cualquier árbol, no solo para el del ejemplo
#include <iostream>
#include <string>

using namespace std;

struct Nodo {
    string dato; //Dato que va a guardar el nodo
    Nodo*  der;
    Nodo* izq;
    Nodo(string d) : dato(d), izq(nullptr), der(nullptr) {} //Constructor
};

void imprimirJerarquia(Nodo* nodo, int nivel){ //recorre el arbol por niveles y les da doble espacio acada vez que baja de nivel
    if (nodo == nullptr) { //Caso base
        return;
    } 
    for (int i = 0; i < nivel * 2; i++){ 
        cout << " ";
    }

    cout << nodo->dato << endl;

    imprimirJerarquia(nodo->der, nivel +1);
    imprimirJerarquia(nodo->izq, nivel + 1 );
}