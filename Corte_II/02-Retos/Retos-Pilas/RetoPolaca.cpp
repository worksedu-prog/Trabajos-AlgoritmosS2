#include <iostream>
#include <sstream>
#include <string>

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


int evaluarRPN(const string& expresion){
    Pila pila;
    istringstream ss(expresion);   // Permite leer la cadena token por token
    string token;

    while(ss >> token){ // Saca el número del texto hasta encontar un espacio para luego moverlo y operarlo
        // Si es operador: sacar dos operandos y calcular
        if(token == "+" || token == "-" || token == "*" || token == "/"){
            int b = pila.top(); pila.pop();   // lee el operador derecho para luego quitarlo de la pila
            int a = pila.top(); pila.pop();   // lee el operador izzquiewrdo para luego quitarlo de la pila

            switch(token[0]){
                case '+': pila.push(a + b); break;
                case '-': pila.push(a - b); break;
                case '*': pila.push(a * b); break;
                case '/': pila.push(a / b); break;
            }
        }
        // Si no, es un número: convertirlo y apilarlo
        else {
            pila.push(stoi(token));
        }
    }
    return pila.top();   // El resultado queda en la cima
}

int main() {
    string expresion;

    cout << "Ingrese la expresion en Polaca (separada por espacios): ";
    getline(cin, expresion);

    cout << "Resultado: " << evaluarRPN(expresion) << endl;

    return 0;
}