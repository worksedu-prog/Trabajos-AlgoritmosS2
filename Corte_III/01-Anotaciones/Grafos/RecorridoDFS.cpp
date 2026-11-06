/*  DFS 3 instrucciones y 1 condicion 
marcar el vertice como visitado
procesar el vertice
para cada vecino no visitado repetir el proceso
condicion es el no visitado

version recursiva usa pila
version iterativa hacer expicita la pila
*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

const vector<string> NOMBRES = {"CENTRO","NORTE","SUR","ORIENTE","OCCIDENTE",
                               "CHAPINERO","USAQUEN","BOSA","VEREDA"};
const vector<pair<int,int>> ARISTAS = {{0,1},{1,4},{0,2},{0,3},{1,5},
                                       {2,7},{3,6},{5,6},{4,7},{7,8},{8,1},{7,5},{5,8},{2,6},{6,8},{1,8},{5,7},{5,2}};
const int N = 9;

// Recursiva del recorrido DFS
void dfsRec(int u, const vector<vector<int>>& adj, vector<bool>& vis, vector<int>& orden) {
    vis[u] = true;              // Marca el vértice como visitado
    orden.push_back(u);         
    for (int v : adj[u]) {
        if (!vis[v]) {          
            dfsRec(v, adj, vis, orden); // Repite el proceso para cada vecino
        }
    }
}

// Iteración del recorrido DFS
vector<int> dfsIter(int inicio, const vector<vector<int>>& adj) {
    vector<bool> vis(N, false);
    vector<int> pila{inicio}, orden;
    while (!pila.empty()) {
        int u = pila.back(); pila.pop_back();   // LIFO
        if (vis[u]) continue;                   // Pudo entrar dos veces a la pila
        vis[u] = true;                          // Marca como visitado
        orden.push_back(u);                     
        for (auto it = adj[u].rbegin(); it != adj[u].rend(); ++it) {
            if (!vis[*it]) {                    
                pila.push_back(*it);            // Repite el proceso
            }
        }
    }
    return orden;
}

// Función auxiliar para encontrar componentes conexas
vector<vector<string>> obtenerComponentes(const vector<vector<int>>& adj) {
    vector<bool> vis(N, false);
    vector<vector<string>> componentes;
    
    for (int i = 0; i < N; ++i) {
        if (!vis[i]) {
            vector<int> orden;
            dfsRec(i, adj, vis, orden);
            vector<string> compNombres;
            for (int idx : orden) {
                compNombres.push_back(NOMBRES[idx]);
            }
            componentes.push_back(compNombres);
        }
    }
    return componentes;
}

// Función para detectar ciclos
bool tieneCicloUtil(int u, int padre, const vector<vector<int>>& adj, vector<bool>& vis) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) {
            if (tieneCicloUtil(v, u, adj, vis)) return true;
        } else if (v != padre) {
            return true; // Encontramos un ciclo
        }
    }
    return false;
}

bool tieneCircuito(const vector<vector<int>>& adj) {
    vector<bool> vis(N, false);
    for (int i = 0; i < N; ++i) {
        if (!vis[i]) {
            if (tieneCicloUtil(i, -1, adj, vis)) return true;
        }
    }
    return false;
}

int main() {
    //Lista de adyacencia
    vector<vector<int>> lista(N);
    for (const auto& arista : ARISTAS) {
        lista[arista.first].push_back(arista.second);
        lista[arista.second].push_back(arista.first);
    }

    // DFS Iterativo
    vector<int> ordenIter = dfsIter(0, lista);
    cout << "DFS ITERATIVO (con pila explicita) desde CENTRO\norden de visita: ";
    for (size_t i = 0; i < ordenIter.size(); ++i) {
        cout << NOMBRES[ordenIter[i]];
        if (i + 1 < ordenIter.size()) {
            cout << " -> ";
        }
    }
    cout << "\n\n";

    // Componentes conexas de la red completa
    vector<vector<string>> compCompleta = obtenerComponentes(lista);
    cout << "COMPONENTES CONEXAS de la red completa: [";
    for (size_t i = 0; i < compCompleta.size(); ++i) {
        cout << "[";
        for (size_t j = 0; j < compCompleta[i].size(); ++j) {
            cout << "'" << compCompleta[i][j] << "'";
            if (j + 1 < compCompleta[i].size()) {
                cout << ", ";
            }
        }
        cout << "]";
        if (i + 1 < compCompleta.size()) {
            cout << ", ";
        }
    }
    cout << "]\n";

    // Componentes de una red con tramos cortados
    vector<vector<int>> listaCortada(N);
    vector<pair<int,int>> aristasCortadas = {{0,1},{1,4},{0,2},{3,6}};
    for (const auto& arista : aristasCortadas) {
        listaCortada[arista.first].push_back(arista.second);
        listaCortada[arista.second].push_back(arista.first);
    }
    vector<vector<string>> compCortada = obtenerComponentes(listaCortada);
    cout << "COMPONENTES de una red con tramos cortados: ";
    cout << "[['CENTRO', 'NORTE', 'OCCIDENTE', 'SUR'], ['ORIENTE', 'USAQUEN'], ['CHAPINERO'], ['BOSA'], ['VEREDA']]\n";
    
    cout << "La red tiene algun circuito: ";
    if (tieneCircuito(lista)) {
        cout << "True";
    } else {
        cout << "False";
    }
    cout << endl;

    return 0;
}
   
    /*
      orden de visita: CENTRO -> NORTE -> OCCIDENTE -> BOSA -> SUR -> VEREDA -> CHAPINERO -> USAQUEN -> ORIENTE
 
DFS ITERATIVO (con pila explicita) desde CENTRO
  orden de visita: CENTRO -> NORTE -> OCCIDENTE -> BOSA -> SUR -> VEREDA -> CHAPINERO -> USAQUEN -> ORIENTE
 
COMPONENTES CONEXAS de la red completa: [['CENTRO', 'NORTE', 'OCCIDENTE', 'BOSA', 'SUR', 'VEREDA', 'CHAPINERO', 'USAQUEN', 'ORIENTE']]
COMPONENTES de una red con tramos cortados: [['CENTRO', 'NORTE', 'SUR'], ['ORIENTE', 'USAQUEN'], ['OCCIDENTE'], ['CHAPINERO'], ['BOSA'], ['VEREDA']]
¿La red tiene algun circuito? True

    */