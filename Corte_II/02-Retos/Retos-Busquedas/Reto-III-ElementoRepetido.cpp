//**Tres: si hay elementos repetidos, la binaria devuelve uno cualquiera de ellos. 
//Háganla devolver siempre el PRIMERO de los repetidos.

#include <iostream>
#include <vector> // Necesario para usar std::vector

using namespace std;

// Función que busca un elemento y devuelve su posición actual 
// o la posición exacta donde debería insertarse si no existe.
int busquedaBinaria(const vector<int>& vec, int elemento) {
    int izquierda = 0;                  // Inicio del rango de búsqueda
    int derecha = vec.size() - 1;       // Fin del rango de búsqueda

    while (izquierda <= derecha) {
        // Punto medio calculado de forma segura contra desbordamientos de enteros
        int medio = izquierda + (derecha - izquierda) / 2;

        if (vec[medio] == elemento) {
            return medio; // ¡Encontrado! Devuelve la posición exacta del elemento
        } 
        else if (vec[medio] < elemento) {
            izquierda = medio + 1; // El objetivo es mayor, descartamos la mitad izquierda
        } 
        else {
            derecha = medio - 1; // El objetivo es menor, descartamos la mitad derecha
        }
    }

    // Si el bucle termina (izquierda > derecha), el elemento NO existía.
    // La variable 'izquierda' queda apuntando exactamente al índice 
    // donde DEBE insertarse para mantener el vector ordenado.
    return izquierda;
}