#include <iostream>
using namespace std;

int main() {
    // 1. Declarar la variable para almacenar el número de puntos de acopio nuevos
    int espacio;

    // 2. Solicitar al usuario la cantidad de elementos que tendrá el arreglo dinámico
    cout << "¿Cuantos puntos de acopio nuevos se van a registrar? ";
    cin >> espacio;

    // 3. Reservar memoria dinámica en el heap para el arreglo de tipo double usando 'new'
    double* arreglo = new double[espacio];

    // 4. Bucle para llenar cada posición del arreglo con el peso ingresado por el usuario
    for(int i = 0; i < espacio; i++) {
        cout << "Ingrese el peso de la jornada especial para el punto " << i + 1 << ": ";
        cin >> arreglo[i];
    }

    // 5. Inicializar el acumulador para la suma total
    double suma = 0;
    
    // 6. Crear un puntero auxiliar que apunte al inicio del arreglo
    double* aux = arreglo;
    
    // 7. Recorrer el arreglo usando aritmética de punteros (sin usar corchetes)
    for(int i = 0; i < espacio; i++) {
        suma += *aux; // Suma el valor actual ubicado en la dirección de 'aux'
        aux++;        // Avanza el puntero a la siguiente casilla de memoria
    }

    // 8. Calcular el promedio dividiendo la suma total entre la cantidad de elementos
    double promedio = suma / espacio;
    cout << "El promedio de recoleccion es: " << promedio << " kg\n";

    // 9. Liberar la memoria reservada con 'new[]' para evitar fugas de memoria
    delete[] arreglo;
    
    // 10. Asignar nullptr al puntero para dejarlo seguro y evitar un puntero colgante
    arreglo = nullptr;

    return 0;
}
