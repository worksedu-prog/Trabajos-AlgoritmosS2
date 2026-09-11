//**Dos: modifíquenla para que, si el elemento no está, 
//devuelva la posición donde DEBERÍA ir. Eso sirve para insertar manteniendo el orden,
// y lo van a necesitar en su proyecto.

#include <iostream>
#include <vector>

using namespace std;

#include <vector>
using namespace std;

// Función de búsqueda binaria que devuelve el índice del elemento si existe,
// o la posición adecuada de inserción si no se encuentra.
int busquedaBinaria(const vector<int>& vec, int elemento) {
    int izquierda = 0;                  // Límite inferior del rango de búsqueda
    int derecha = vec.size() - 1;       // Límite superior del rango de búsqueda

    // El bucle continúa mientras el rango de búsqueda sea válido
    while (izquierda <= derecha) {
        // Cálculo del punto medio (evita desbordamiento de entero a diferencia de '(izq + der) / 2')
        int medio = izquierda + (derecha - izquierda) / 2;

        // Si el elemento objetivo está exactamente en la posición media
        if (vec[medio] == elemento) {
            return medio; // Elemento encontrado, retorna su índice actual
        } 
        // Si el elemento objetivo es mayor que el valor medio
        else if (vec[medio] < elemento) {
            izquierda = medio + 1; // Descartamos la mitad izquierda y buscamos a la derecha
        } 
        // Si el elemento objetivo es menor que el valor medio
        else {
            derecha = medio - 1; // Descartamos la mitad derecha y buscamos a la izquierda
        }
    }

    // Si el bucle termina sin encontrar el elemento (izquierda > derecha),
    // la variable 'izquierda' almacena el índice donde DEBERÍA insertarse 
    // el elemento para mantener el vector ordenado.
    return izquierda;
}