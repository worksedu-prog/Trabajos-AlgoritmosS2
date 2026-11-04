/*Un grafo es una conexión o conjunto de nodos, donde cada nodo puede estar conectado a otros nodos mediante aristas (tambien llamados hilos)
A diferencia de un árbol, un grafo puede tener ciclos y no tiene una raíz definida
Un grafo puede tener desde 0 hasta n(n-1)/2 aristas ciclicas, donde n es el número de nodos
Grado: números de aristas que inciden en un nodo
No dirigido: Las aristas no tienen dirección, es decir, si hay una arista entre el nodo A y el nodo B, se puede ir de A a B y de B a A
Dirigido: Las aristas tienen dirección, es decir, si hay una arista entre el nodo A y el nodo B, se puede ir de A a B pero NO de B a A
Ponderado: Aristas tienen un peso o valor asociado, que puede representar como distancia, peso, etc..
Caminos: Secuencia de aristas que conectan nodos
Ciclos: Camino que empieza y termina en el mismo nodo
Conexo: Si existe un camino entre cada par de nodos

Matriz de adyacencia: Matriz cuadrada de n x n nodos, donde n es el número de nodos,
si hay una arista entre el nodo i y j, entonces la posición (i,j) es 1, sino el resto de sera 0
Lista de adyacencia: Lista de listas donde cada lista contiene los nodos adyacentes a un nodo
*/

#include <iostream>
#include <vector>
using namespace std;


vector<vector<int>> matriz(N, vector<int>(N, 0));
for (auto [u, v] : ARISTAS) {
    matriz[u][v] = 1;
    matriz[v][u] = 1;         // no dirigido: la matriz es simetrica
}
bool hayVia(int u, int v) { return matriz[u][v] == 1; }  // O(1)
