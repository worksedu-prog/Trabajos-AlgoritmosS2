//RETO 3  ·  El espejo   
//Contexto: Los códigos de inventario de una biblioteca comunitaria son válidos solo si se leen igual al derecho y al revés.
//Se pide: Determinar si un arreglo de números es palíndromo, sin crear un segundo arreglo y sin usar funciones de reversa del lenguaje.
//Pista: Dos índices que caminan en sentidos opuestos: uno desde el inicio y otro desde el final. Se detienen cuando se cruzan.

#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Código a probar
    vector<int> codigo = {1, 2, 3, 2, 1};

    // Variable de inicio (posición 0)
    int inicio = 0; 
    // Variable del final (última posición del vector)
    int fin = codigo.size() - 1; 

    // Variable booleana que asume que es palíndromo hasta demostrar lo contrario
    bool es_palindromo = true; 

    // El bucle se ejecuta mientras los índices no se hayan cruzado
    while (inicio < fin) {
        // Comprobamos si los elementos en los extremos son diferentes
        if (codigo[inicio] != codigo[fin]) {
            es_palindromo = false; // Se rompe la regla de simetría
            break; // Salimos del bucle de inmediato porque ya no es necesario seguir revisando
        }

        // Acercamos los índices hacia el centro
        inicio++; // Avanza desde la izquierda
        fin--;    // Retrocede desde la derecha
    }

    // Mostramos el resultado según el valor final de la variable es_palindromo
    cout << "--- Análisis de codigo de inventario ---" << endl;
    if (es_palindromo) {
        cout << "El código ES un palíndromo válido." << endl;
    } else {
        cout << "El código NO es un palíndromo." << endl;
    }

    return 0;
}
