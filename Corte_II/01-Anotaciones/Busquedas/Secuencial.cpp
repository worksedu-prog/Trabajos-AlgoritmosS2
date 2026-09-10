// Busqueda secuencial en C++
#include <iostream>

using namespace std;

// Función que realiza la búsqueda secuencial
// Parámetros: 
// arreglo[] -> el arreglo de números donde se buscará
// n         -> el tamaño del arreglo (cantidad de elementos)
// x         -> el elemento que queremos encontrar
int busquedaSecuencial(int arreglo[], int n, int x)
{
    // Recorremos el arreglo desde el índice 0 hasta el n-1
    for (int i = 0; i < n; i++)
    {
        // Si el elemento actual es igual al que buscamos...
        if (arreglo[i] == x)
            return i; // Retornamos el índice 'i' e interrumpimos la función inmediatamente
    }
    
    // Si el ciclo terminó y NUNCA encontró el elemento 'x',
    // ejecutamos esta línea y retornamos -1 indicando "no encontrado"
    return -1;
}

int main()
{
    // Definimos un arreglo de 5 elementos
    int arreglo[] = {2, 40, 36, 55, 30};
    
    // Calculamos el tamaño del arreglo:
    //Nota: Una variable int ocupa normalmente 4 bytes en memoria, y el arreglo tiene 5 elementos, por lo que el total de bytes es 20.
    // sizeof(arreglo) = total de bytes del arreglo (20 bytes)
    // sizeof(arreglo[0]) = bytes de un solo entero (4 bytes)
    // 20 / 4 = 5 elementos
    int n = sizeof(arreglo) / sizeof(arreglo[0]);
    
    int x = 55; // Elemento que queremos buscar
    
    // Llamamos a la función y guardamos el resultado (el índice devuelto o -1)
    int resultado = busquedaSecuencial(arreglo, n, x);
    
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