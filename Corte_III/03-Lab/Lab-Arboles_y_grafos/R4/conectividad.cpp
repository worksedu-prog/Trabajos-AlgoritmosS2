// ============================================================
//  Laboratorio integrador · Corte 3 · RETO 4  (25 puntos)
//  Sesiones 41 y 43 — DFS, componentes conexas y vias criticas
//  Sistema: RedAcopio — que vias no pueden cerrarse
//
//  Este archivo NO tiene main(): el main esta en pruebas_r4.cpp
//  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r4.cpp ni red.h
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_r4 conectividad.cpp pruebas_r4.cpp
//     ./pruebas_r4
//
//      ESTUDIANTE: Julian Hernández
// ============================================================
#include <vector>
#include <string>
#include "red.h"
using namespace std;


int cuantasComponentes(const vector<vector<int>>& g) { 
    int n = g.size();
    vector<bool> visitado(n, false);
    int componentes = 0;

    for (int i = 0; i < n; ++i) {
        // Si el vértice no fue visitado se inicia un nuevo DFS
        if (!visitado[i]) {
            componentes++;
            
            vector<int> pila;
            pila.push_back(i);
            visitado[i] = true;

            // DFS iterativo usando la pila explícita
            while (!pila.empty()) {
                int u = pila.back();
                pila.pop_back();

                for (int v : g[u]) {
                    if (!visitado[v]) {
                        visitado[v] = true;
                        pila.push_back(v);
                    }
                }
            }
        }
    }

    return componentes;
}


vector<string> viasCriticas() {
    vector<string> criticas;

    int n = NOMBRES.size();

    for (size_t i = 0; i < ARISTAS.size(); ++i) {
        vector<vector<int>> g(n);

        for (size_t j = 0; j < ARISTAS.size(); ++j) {
            if (j == i) continue;                 

            int u = ARISTAS[j].first;             
            int v = ARISTAS[j].second;           
            g[u].push_back(v);
            g[v].push_back(u);
        }

        if (cuantasComponentes(g) > 1) {
            criticas.push_back(NOMBRES[ARISTAS[i].first] + "-" +      
                               NOMBRES[ARISTAS[i].second]);
        }
    }

    return criticas;
}