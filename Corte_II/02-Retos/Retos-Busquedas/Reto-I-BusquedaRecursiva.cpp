//Busqueda recursiva
//@Julian_H
//PREFERIBLEMENTE NO USARLA
#include <iostream>

using namespace std;    

int busquedaRecursiva(int arr[], int n, int x) {
    if (n == 0) {
        return -1; // Elemento no encontrado
    }
    if (arr[n - 1] == x) {
        return n - 1; // Elemento encontrado en la posición n-1
    }
    return busquedaRecursiva(arr, n - 1, x); // Llamada recursiva con tamaño reducido
}

int main (){
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 6;

    int resultado = busquedaRecursiva(arr, n, x);
    if (resultado != -1) {
        cout << "Elemento encontrado en la posicion: " << resultado << endl;
    } else {
        cout << "Elemento no encontrado" << endl;
    }

    return 0;
}