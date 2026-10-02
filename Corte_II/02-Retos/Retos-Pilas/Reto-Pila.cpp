#include <iostream>

using namespace std;

// Nodo de la lista enlazada
struct Nodo{
    int info;
    Nodo* siguiente;
    Nodo(int var) : info(var), siguiente(nullptr){}
};

// Pila (LIFO) implementada con lista enlazada
class Pila{
    private:
        Nodo* tope;
    public:
        Pila() : tope(nullptr){}

        // Inserta un elemento en la cima
        void push(int var){
            Nodo* nuevo = new Nodo(var);
            nuevo->siguiente = tope;
            tope = nuevo;
        }

        // Elimina el elemento de la cima
        void pop(){
            if(tope != nullptr){
                Nodo* temp = tope;
                tope = tope->siguiente;
                delete temp;
            }
        }

        // Devuelve el elemento de la cima sin eliminarlo
        int top(){
            if(tope != nullptr){
                return tope->info;
            }
            return -1; // Return -1 si la pila esta vacia
        }

        bool isEmpty(){
            return tope == nullptr;
        }

    // Libera todos los nodos al destruir la pila
    ~Pila(){
        while(!isEmpty()){
            pop();
        }
    }
};

int main() {

    Pila mipila;
    mipila.push(400);
    mipila.push(10);

    cout << "El valor tope de mi pila es: " << mipila.top() << endl;

    return 0;
}