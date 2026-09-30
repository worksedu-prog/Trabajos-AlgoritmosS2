#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <iomanip>

using namespace std;

// Búsqueda binaria: devuelve {posición, comparaciones}
pair<int, int> busquedaBinaria(const vector<int>& v, int x) {
    int comparaciones = 0;
    int izq = 0, der = v.size() - 1;

    while (izq <= der) {
        int medio = (izq + der) / 2;
        comparaciones++;

        if (v[medio] == x) {
            return {medio, comparaciones};
        } else if (v[medio] < x) {
            izq = medio + 1;   // me quedo con la mitad derecha
        } else {
            der = medio - 1;   // me quedo con la mitad izquierda
        }
    }

    // no estaba
    return {-1, comparaciones};
}

// Búsqueda secuencial: revisa uno por uno
pair<int, int> busquedaSecuencial(const vector<int>& v, int x) {
    int comparaciones = 0;

    for (int i = 0; i < v.size(); i++) {
        comparaciones++;
        if (v[i] == x) {
            return {i, comparaciones};
        }
    }

    // no estaba
    return {-1, comparaciones};
}

// para guardar los datos de cada fila de la tabla
struct Resultado {
    string caso;
    int valor;
    int compSecuencial;
    int compBinaria;
};

int main() {
    // tiene que estar ordenado para que funcione la binaria
    vector<int> vec = {10, 20, 30, 40, 50, 60, 70, 80, 90};

    // uso un vector de pares y no un map para que no se cambie el orden
    vector<pair<string, int>> casos = {
        {"Primer elemento", vec[0]},
        {"Elemento del medio", vec[vec.size() / 2]},
        {"Último elemento", vec.back()},
        {"Elemento inexistente", 999}
    };

    // muestro el vector
    cout << "Coleccion de registros (" << vec.size() << " elementos): [";
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i < vec.size() - 1) cout << ", ";
    }
    cout << "]\n\n";

    // corro las dos búsquedas en cada caso y guardo las comparaciones
    vector<Resultado> resultados;

    for (const auto& c : casos) {
        auto sec = busquedaSecuencial(vec, c.second);
        auto bin = busquedaBinaria(vec, c.second);

        resultados.push_back({c.first, c.second, sec.second, bin.second});
    }

    // encabezado de la tabla
    cout << left
         << setw(22) << "Caso de Prueba" << " | "
         << setw(6)  << "Valor" << " | "
         << setw(27) << "Comparaciones en Secuencial" << " | "
         << setw(24) << "Comparaciones en Binaria" << "\n";
    cout << string(90, '-') << "\n";

    // filas
    for (const auto& r : resultados) {
        cout << left
             << setw(22) << r.caso << " | "
             << setw(6)  << r.valor << " | "
             << setw(27) << r.compSecuencial << " | "
             << setw(24) << r.compBinaria << "\n";
    }

    return 0;
}