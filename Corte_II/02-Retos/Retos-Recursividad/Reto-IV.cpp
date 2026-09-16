//Cuatro: Recorran e impriman su lista enlazada de forma recursiva, en orden inverso, sin usar ninguna estructura auxiliar. 
// Cuando les salga, van a entender por qué la recursión y las estructuras enlazadas van juntas.
// PISTA PARA EL RETO 4: Si imprimen antes de la llamada recursiva sale en orden normal; si imprimen después, sale invertido. 
// Ese descubrimiento es el que prepara los recorridos preorden y postorden de árboles en la Sesión 35. No se los diga: déjelos encontrarlo.

#include <iostream>

using namespace std;

// Definición de la estructura de un Nodo (Vagón)
struct Nodo {
    int valor;          // El contenido/número del vagón
    Nodo* siguiente;    // El puntero al siguiente nodo
    
    // Constructor para crear cajitas fácilmente
    Nodo(int val) : valor(val), siguiente(nullptr) {}
};

// Función recursiva del Reto 4
void imprimirInverso(Nodo* vagon) {
    // 1. Caso Base: Si el puntero es nulo (llegamos al final del tren)
    if (vagon == nullptr) {
        return; // Detiene la ida
    }
    
    // 2. Paso Recursivo: Viajamos hasta el fondo PRIMERO
    imprimirInverso(vagon->siguiente);
    
    // 3. Impresión: Se ejecuta al REGRESAR de la llamada recursiva
    cout << vagon->valor << std::endl;
}

int main() {
    // Creamos las 3 cajitas en memoria
    Nodo* vagon1 = new Nodo(10);
    Nodo* vagon2 = new Nodo(20);
    Nodo* vagon3 = new Nodo(30);

    // Enganchamos los vagones usando la flecha ->
    vagon1->siguiente = vagon2;
    vagon2->siguiente = vagon3;
    // vagon3->siguiente ya es nullptr por el constructor

    // Ejecutamos la función iniciando desde el primer vagón
    imprimirInverso(vagon1);

    // Liberación de memoria (buena práctica en C++)
    delete vagon1;
    delete vagon2;
    delete vagon3;

    return 0;
}