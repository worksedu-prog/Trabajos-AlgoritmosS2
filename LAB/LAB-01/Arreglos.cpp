#include <iostream>
using namespace std;

int main (){

    int espacio;

    cout << "¿Cuanto espacio desea tener?" << endl;
    cin >> espacio;

    double* arreglo = new double[espacio];

    for (int i=0; i<espacio; i++){
        cout << "Ingrese el valor " << i+1 << ": ";
        cin >> arreglo[i];
    }

    //Suma
    double suma = 0;
    double* aux= arreglo;
    for(int i=0; i<espacio; i++){
        suma += *aux;
        aux++;
    }
    cout << "La suma es: " << suma << endl;
    delete[] arreglo;
    arreglo = nullptr;

    return 0;
}
