//Reto 2 — El rango · Obligatorio Escriba enRango(nodo, a, b) que imprima todas las claves entre a y b, 
//ambas incluidas, en orden ascendente. La gracia está en que NO debe visitar todo el árbol: 
//si la clave del nodo es menor que a, no tiene sentido bajar por la izquierda. 
//Pista: Es un inorden con dos podas. Agregue un contador de nodos visitados y compare contra el total del árbol: debe ser menor. 
//Resultado esperado: Con el árbol del ejemplo y el rango [35, 65], debe imprimir 35, 40, 50, 60 visitando menos de 8 nodos.

#include <iostream>
#include <string>

using namespace std;

struct Nodo {
    int dato; //Dato se va a guardar en el nodo
    Nodo*  der;
    Nodo* izq;
    Nodo(int d) : dato(d), izq(nullptr), der(nullptr) {} //Constructor
};

void enRango(Nodo* nodo, int a, int b){
    if (nodo == nullptr){return;}

    if (nodo->dato > a){enRango(nodo->izq, a, b); }
    if (a <= nodo->dato && nodo->dato <= b ){cout << nodo->dato << endl;}
    if (nodo->dato < b ){enRango(nodo->der, a, b);}

}

int main() {
    //  Árbol Binario de Búsqueda de prueba:
    //          50
    //        /    \
    //      30      70
    //     /  \    /  \
    //    20  40  60  80
    //       /
    //      35

    Nodo* raiz = new Nodo(50);
    raiz->izq = new Nodo(30);
    raiz->der = new Nodo(70);
    
    raiz->izq->izq = new Nodo(20);
    raiz->izq->der = new Nodo(40);
    raiz->izq->der->izq = new Nodo(35); 
    
    raiz->der->izq = new Nodo(60);
    raiz->der->der = new Nodo(80);

    int a = 35;
    int b = 65;

    cout << "Claves en el rango [" << a << ", " << b << "]:\n";
    enRango(raiz, a, b);
    cout << endl;

    return 0;
}