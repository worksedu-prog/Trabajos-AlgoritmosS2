//Ejercicio 3 · Trazado de búsqueda binaria  ·  C++  ·  (trazado) 
//Sobre el arreglo ordenado de códigos, complete la tabla de iteraciones para buscar 175 y para buscar 160. Indique en 
//cada caso cuántas iteraciones ejecuta el ciclo.

#include <iostream>
#include <vector>

using namespace std;

int v[] = {103, 118, 127, 134, 149, 156, 168, 175, 182, 190, 203, 219};

int buscar(int v[], int n, int x) { 
    int izq = 0, der = n - 1; 
    while (izq <= der) { 
        int medio = (izq + der) / 2; 
        if (v[medio] == x) return medio; 
        if (v[medio] <  x) izq = medio + 1; 
        else der = medio - 1;              
    }
    return -1; 
};


//Para buscar 175 realiza 4 iteraciones
//Para buscar 160 realiza 3 iteraciones 