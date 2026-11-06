#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

//Enumerar los lugares que es como convertirlos en enteros
enum Lugares {
    CENTRO = 0,
    NORTE,
    SUR,
    ORIENTE,
    OCCIDENTE,
    CHAPINERO,
    USAQUEN,
    BOSA,
    VEREDA
};

const int N = 9;
vector<vector<int>> lista(N);

// Frncuión BFS
void bfs(int inicio, vector<int>& orden, vector<int>& dist, vector<int>& padre) {
    vector<bool> vis(N, false);
    dist.assign(N, -1); 
    padre.assign(N, -1); 
    orden.clear();
    
    queue<int> cola;
    cola.push(inicio); 
    vis[inicio] = true; 
    dist[inicio] = 0;
    
    while (!cola.empty()) {
        int u = cola.front(); 
        cola.pop();    // FIFO
        orden.push_back(u);
        
        for (int v : lista[u]) {
            if (!vis[v]) {
                vis[v] = true;                 // Se Encola
                dist[v] = dist[u] + 1;
                padre[v] = u;
                cola.push(v);
            }
        }
    }
}

// Función para el camino más corto
vector<int> reconstruir_camino(int destino, const vector<int>& padre) {
    vector<int> camino;
    for (int v = destino; v != -1; v = padre[v]) {
        camino.push_back(v);
    }
    reverse(camino.begin(), camino.end());
    return camino;
}

// Nombres
string nombreLugar(int id) {
    string nombres[] = {"CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"};
    return nombres[id];
}

int main() {
    // Lista adyacente
    // CENTRO conectado con NORTE, SUR, ORIENTE
    lista[CENTRO].push_back(NORTE);
    lista[CENTRO].push_back(SUR);
    lista[CENTRO].push_back(ORIENTE);

    // Conexiones de NORTE, SUR, ORIENTE
    lista[NORTE].push_back(OCCIDENTE);
    lista[SUR].push_back(BOSA);
    lista[ORIENTE].push_back(USAQUEN);
    
    // Prueba de conexiones de ejemplo
    lista[OCCIDENTE].push_back(BOSA);
    lista[USAQUEN].push_back(VEREDA);

    vector<int> orden, dist, padre;
    
    // BFS desde CENTRO
    bfs(CENTRO, orden, dist, padre);

    cout << "Caminos cortos desde el CENTRO:\n";
    int destinos[] = {BOSA, USAQUEN, OCCIDENTE};
    
    for (int d : destinos) {
        vector<int> camino = reconstruir_camino(d, padre);
        cout << "Hacia " << nombreLugar(d) << " (" << dist[d] << " tramos): ";
        for (size_t i = 0; i < camino.size(); ++i) {
            cout << nombreLugar(camino[i]);
            if (i + 1 < camino.size()) cout << " -> ";
        }
        cout << "\n";
    }

    return 0;
}
/*
NIVELES (todos los que estan a la misma distancia)
  nivel 0: CENTRO
  nivel 1: NORTE, SUR, ORIENTE
  nivel 2: OCCIDENTE, CHAPINERO, USAQUEN, BOSA
  nivel 3: VEREDA
 
CAMINO MAS CORTO desde CENTRO (en numero de tramos)
  hacia BOSA      : CENTRO -> SUR -> BOSA   (2 tramos)
  hacia USAQUEN   : CENTRO -> ORIENTE -> USAQUEN   (2 tramos)
  hacia OCCIDENTE : CENTRO -> NORTE -> OCCIDENTE   (2 tramos)
 
  DFS hacia BOSA : CENTRO -> NORTE -> OCCIDENTE -> BOSA   (3 tramos)
  BFS hacia BOSA : CENTRO -> SUR -> BOSA   (2 tramos)
  BFS garantiza el minimo numero de tramos; DFS solo garantiza que llega.


*/