#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct SolicitudProyecto {
    int id;
    string estudiante;
    int urgencia;
};

//Reto dos: ordenen los registros de su proyecto por el criterio que su línea necesite. Los de la uno, por veces prestado. Los de la dos, por saturación. Los de la tres, por urgencia.
//Reto tres: hagan la tabla de comparaciones e intercambios con SUS datos reales, no con estos ocho

// RETO 2 y 3: BUBBLE SORT CON BANDERA
void bubbleSortUrgencia(vector<SolicitudProyecto>& vec, int& comps, int& swaps) {
    comps = 0; swaps = 0;
    int n = vec.size();
    bool huboIntercambio;
    
    for (int i = 0; i < n - 1; i++) {
        huboIntercambio = false;
        for (int j = 0; j < n - i - 1; j++) {
            comps++;
            if (vec[j].urgencia < vec[j + 1].urgencia) { // Orden descendente
                swap(vec[j], vec[j + 1]);
                swaps++;
                huboIntercambio = true;
            }
        }
        if (!huboIntercambio) break; // Optimizacion por bandera
    }
}

// RETO 4: BUSQUEDA SECUENCIAL
int busquedaSecuencial(const vector<SolicitudProyecto>& vec, int idBuscado, int& comps) {
    comps = 0;
    for (size_t i = 0; i < vec.size(); i++) {
        comps++;
        if (vec[i].id == idBuscado) {
            return i;
        }
    }
    return -1;
}

// RETO 4: BUSQUEDA BINARIA
int busquedaBinaria(const vector<SolicitudProyecto>& vec, int idBuscado, int& comps) {
    comps = 0;
    int inicio = 0;
    int fin = vec.size() - 1;
    
    while (inicio <= fin) {
        int medio = inicio + (fin - inicio) / 2;
        comps++;
        if (vec[medio].id == idBuscado) {
            return medio;
        }
        if (vec[medio].id < idBuscado) {
            inicio = medio + 1;
        } else {
            fin = medio - 1;
        }
    }
    return -1;
}