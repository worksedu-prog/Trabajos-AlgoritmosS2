//Parte A — La cola de atención
//Implementen la cola de espera de su sistema, sobre lista enlazada, con encolar, desencolar, consultar el frente y saber cuántos hay. Encolar y desencolar deben costar O de uno los dos, y el tamaño también.
//Prueben explícitamente el caso de vaciar la cola y volver a encolar. Ese caso vale puntos.

//Nuestro programa de proyecto usa vectores para tener una urgencia por lo tanto NO listas enlazas, 
//este codigo es probable que solo se usen una partes o quiza no se use


#include <iostream>   
#include <string>    
using namespace std;  


struct Nodo {
    string dato;       
    Nodo* siguiente;   
};

class Cola {
    Nodo* frenteNodo = nullptr;   // apunta al primer nodo, el que sale primero
    Nodo* finalNodo = nullptr;    // apunta al último nodo, permite encolar sin recorrer la lista
    int tamano = 0;               // Cantidad de elementos en la cola
public:
    // ENCOLAR: agrega un elemento al final de la cola
    void encolar(string dato) {
        // Se crea un nodo nuevo en memoria con el dato y sin siguiente
        Nodo* nuevo = new Nodo{dato, nullptr};

        if (finalNodo == nullptr) {
            // La cola estaba vacía: el nodo nuevo es el primero y el último a la vez
            frenteNodo = nuevo;
        } else {
            // La cola tenía elementos: el último actual ahora apunta al nuevo
            finalNodo->siguiente = nuevo;
        }

        finalNodo = nuevo;   // el nodo nuevo pasa a ser el último
        tamano++;            // hay un elemento más
    }

    // DESENCOLAR: saca el primer elemento y lo devuelve
    // Importante: solo llamarlo si la cola NO está vacía
    string desencolar() {
        Nodo* viejo = frenteNodo;        // guardamos el nodo del frente para no perderlo
        string dato = viejo->dato;       // copia el dato para devolverlo al final
        frenteNodo = viejo->siguiente;   // el frente avanza al siguiente nodo

        if (frenteNodo == nullptr) {
            // Si no hay nodos, la cola queda vacia asi que pues es in nullptr
            // El final también debe ser nullptr. Si no, apuntaría a un nodo borrado
            // y el próximo encolar fallaría.
            finalNodo = nullptr;
        }

        delete viejo;   // libera la memoria del nodo que salió
        tamano--;       // hay un elemento menos
        return dato;    // Se devuelve lo que había en el frente
    }

    // FRENTE: muestra quién es el primero sin sacarlo de la cola. Costo O(1).
    // Importante: solo llamarlo si la cola NO está vacía.
    string frente() {
        return frenteNodo->dato;
    }

    // CUANTOS: devuelve cuántos elementos hay en la cola
    int cuantos() {
        return tamano;
    }

    // VACIA: devuelve true si no hay elementos, false si hay al menos uno
    bool vacia() {
        return tamano == 0;
    }
};

int main() {
    Cola c;   // se crea una cola vacía

    cout << "--- Prueba 1: cola vacia ---" << endl;
    cout << "Esta vacia? " << (c.vacia() ? "Si" : "No") << endl;   
    cout << "Cuantos hay? " << c.cuantos() << endl;               

    cout << "\n--- Prueba 2: encolar y consultar ---" << endl;
    c.encolar("A");
    c.encolar("B");
    cout << "Cuantos hay? " << c.cuantos() << endl;   
    cout << "Frente: " << c.frente() << endl;         

    cout << "\n--- Prueba 3: desencolar ---" << endl;
    cout << "Sale: " << c.desencolar() << endl;       
    cout << "Sale: " << c.desencolar() << endl;       
    cout << "Esta vacia? " << (c.vacia() ? "Si" : "No") << endl;   

    cout << "\n--- Prueba 4: vaciar y volver a encolar ---" << endl;
    c.encolar("C");
    c.encolar("D");
    cout << "Cuantos hay? " << c.cuantos() << endl;   
    cout << "Frente: " << c.frente() << endl;         
    cout << "Sale: " << c.desencolar() << endl;       
    cout << "Sale: " << c.desencolar() << endl;       
    cout << "Esta vacia? " << (c.vacia() ? "Si" : "No") << endl; 

    return 0;
}