//Busqueda Binaria en cpp

#include <iostream>

using namespace std;

// Función que realiza la búsqueda binaria
// Parámetros: 
// arreglo[] -> el arreglo ordenado de números donde se buscará
// n         -> el tamaño del arreglo (cantidad de elementos)
// x         -> el elemento que queremos encontrar
int busquedaBinaria(int arreglo[], int n, int x)
{
    // Límite inferior: al inicio apunta a la primera posición (índice 0)
    int bajo = 0;

    // Límite superior: al inicio apunta a la última posición (índice n - 1)
    int alto = n - 1;

    // Mientras el rango de búsqueda sea válido (el límite inferior no supere al superior)
    while (bajo <= alto)
    {
        // Calculamos el punto medio de nuestro rango actual
        int medio = (bajo + alto) / 2;

        // CASO 1: Si el valor del medio es exactamente el que se busca
        if (arreglo[medio] == x)
            return medio; //Retorna su índice inmediatamente.

        // CASO 2: Si el valor del medio es MENOR que el número buscado ('x')
        // Significa que 'x' debe estar en la mitad DERECHA (números más grandes)
        else if (arreglo[medio] < x)
            bajo = medio + 1; // Descartamos la mitad izquierda moviendo el límite 'bajo'

        // CASO 3: Si el valor del medio es MAYOR que el número buscado ('x')...
        // Significa que 'x' debe estar en la mitad IZQUIERDA (números más pequeños)
        else
            alto = medio - 1; // Descartamos la mitad derecha moviendo el límite 'alto'
    }

    // Si el ciclo 'while' se rompe (bajo > alto), significa que acotamos todo el arreglo
    // y el elemento 'x' no existía. Retornamos -1 para indicar "no encontrado".
    return -1;
}

int main()
{
    // Definimos un arreglo de 5 elementos, ORDENADOS de menor a mayor (requisito para la búsqueda binaria)
    int arreglo[] = {2, 4, 6, 8, 10};

    // Calculamos el tamaño del arreglo:
    int n = sizeof(arreglo) / sizeof(arreglo[0]);

    int x = 10; // Elemento que queremos buscar

    // Llamamos a la función y guardamos el resultado (el índice devuelto o -1)
    int resultado = busquedaBinaria(arreglo, n, x);

    // Evaluamos el resultado de la búsqueda
    if (resultado == -1)
    {
        // Si devolvió -1, el elemento no existe en el arreglo
        cout << "Elemento no encontrado" << endl;
    }
    else
    {
        // Si devolvió cualquier otro número, es la posición (índice) donde se halló
        cout << "Elemento " << x << " encontrado en el indice: " << resultado << endl;
        // El número de pasos equivale al índice + 1 (ya que los índices empiezan en 0)
        cout << "Cantidad de pasos realizados: " << resultado + 1 << endl;
    }

    return 0; // Indica que el programa finalizó correctamente
}