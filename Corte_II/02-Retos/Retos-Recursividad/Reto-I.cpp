//SumaLista recursiva. Reciba una lista y devuelva la suma de sus elementos, sin ciclos. 
// Piensar en la definición recursiva de una lista, la que dijimos al principio: una lista es un elemento seguido de una lista.

#include <iostream>
#include <list>

using namespace std;

int sumalista(list<int> l) {
    if (l.empty()) {
        return 0; // Caso base: si la lista está vacía, la suma es 0
    } else {
        int primer_elemento = l.front(); // Obtener el primer elemento de la lista
        l.pop_front(); // Eliminar el primer elemento de la lista
        return primer_elemento + sumalista(l); // Sumar el primer elemento con la suma del resto de la lista
    }

}

int main() {

    list<int> L={1, 2, 3, 4, 5}; // Ejemplo de lista
    int suma = sumalista(L); // Llamada a la función recursiva
    cout << "La suma de la lista es: " << suma << endl; // Imprimir el resultado
    return 0;
}