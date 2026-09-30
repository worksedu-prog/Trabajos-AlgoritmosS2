#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <iomanip>
#include <utility>

using namespace std;

// Selection sort: ordena el mismo vector que recibe
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        int minIdx = i;
        // busco el menor del resto del vector
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        swap(arr[i], arr[minIdx]);
    }
}

// Quicksort: este no ordena el original, devuelve un vector nuevo
vector<int> quicksort(const vector<int>& arr) {
    if (arr.size() <= 1) {
        return arr;
    }

    int pivot = arr[arr.size() / 2];

    // separo en menores, iguales y mayores al pivote
    vector<int> left, middle, right;
    for (int x : arr) {
        if (x < pivot) left.push_back(x);
        else if (x == pivot) middle.push_back(x);
        else right.push_back(x);
    }

    // left ordenado + middle + right ordenado
    vector<int> resultado = quicksort(left);
    resultado.insert(resultado.end(), middle.begin(), middle.end());
    vector<int> derecha = quicksort(right);
    resultado.insert(resultado.end(), derecha.begin(), derecha.end());

    return resultado;
}

int main() {
    // números aleatorios entre 1 y 100000
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(1, 100000);

    vector<int> tamanos = {1000, 5000, 10000};

    // encabezado de la tabla
    cout << left
         << setw(13) << "Tamaño (n)" << " | "
         << setw(16) << "Selección (s)" << " | "
         << setw(15) << "Quicksort (s)" << "\n";
    cout << string(48, '-') << "\n";

    for (int n : tamanos) {
        vector<int> datos(n);
        for (int i = 0; i < n; i++) {
            datos[i] = dist(gen);
        }

        // tiempo de selection sort
        vector<int> copiaSel = datos;
        auto inicio = chrono::steady_clock::now();
        selectionSort(copiaSel);
        chrono::duration<double> tiempoSel = chrono::steady_clock::now() - inicio;

        // tiempo de quicksort (guardo el resultado para que no lo descarte el compilador)
        vector<int> copiaQuick = datos;
        inicio = chrono::steady_clock::now();
        vector<int> ordenado = quicksort(copiaQuick);
        chrono::duration<double> tQuick = chrono::steady_clock::now() - inicio;

        // imprimo la fila con 4 decimales
        cout << left << fixed << setprecision(4)
             << setw(13) << n << " | "
             << setw(16) << tiempoSel.count() << " | "
             << setw(15) << tQuick.count() << "\n";
    }

    return 0;
}