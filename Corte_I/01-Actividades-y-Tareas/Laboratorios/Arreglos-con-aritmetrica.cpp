#include <iostream>
using namespace std;

int main (){

    // 1. Declarar la variable para el tamaño dinámico del arreglo
    int espacio;

    // 2. Pedir al usuario el tamaño que tendrá el arreglo en tiempo de ejecución
    cout << "¿Cuanto espacio desea tener?" << endl;
    cin >> espacio;

    // 3. Reservar memoria dinámica en el heap usando 'new'
    double* arreglo = new double[espacio];

    // 4. Bucle para que el usuario ingrese los valores de cada posición
    for (int i=0; i<espacio; i++){
        cout << "Ingrese el valor " << i+1 << ": ";
        cin >> arreglo[i];
    }

    // 5. Inicializar la variable acumuladora para la suma
    double suma = 0;
    
    // 6. Crear un puntero auxiliar que apunte al inicio del arreglo
    double* aux = arreglo;
    
    // 7. Recorrer el arreglo usando aritmética de punteros (*aux para el valor y aux++ para avanzar)
    for(int i=0; i<espacio; i++){
        suma += *aux; // Suma el valor actual al acumulador
        aux++;        // Mueve el puntero a la siguiente casilla de memoria
    }

    // 8. Mostrar el resultado de la suma total
    cout << "La suma es: " << suma << endl;
    
    // 9. Liberar la memoria dinámica reservada con 'new[]' para evitar fugas de memoria
    delete[] arreglo;
    
    // 10. Apuntar el puntero a nullptr para dejarlo seguro y evitar punteros colgantes
    arreglo = nullptr;

    return 0;
}
