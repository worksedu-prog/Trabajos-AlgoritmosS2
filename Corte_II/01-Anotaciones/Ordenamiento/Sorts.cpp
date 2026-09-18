#include <iostream>

using namespace std;

/* Bubble Sort */
void bubbleSort(int arr[], int n, int &comparaciones, int &intercambios) {
    comparaciones = 0;
    intercambios = 0;
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++; // Se realiza la comparación
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                intercambios++; // Se realiza el intercambio
                swapped = true;
            }
        }
        if (!swapped) break; // Optimización si ya está ordenado
    }
}

/* Selection Sort */
void selectionSort(int arr[], int n, int &comparaciones, int &intercambios) {
    comparaciones = 0;
    intercambios = 0;

    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++; // Se realiza la comparación para hallar el mínimo
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        // Solo cuenta el intercambio si realmente cambia de posición
        if (minIdx != i) {
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
            intercambios++;
        }
    }
}

/* Insertion Sort */
void insertionSort(int arr[], int n, int &comparaciones, int &desplazamientos) {
    comparaciones = 0;
    desplazamientos = 0; // Representa los desplazamientos de elementos

    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0) {
            comparaciones++; // Se evalúa la condición de comparación
            if (arr[j] > key) {
                arr[j + 1] = arr[j];
                desplazamientos++; // Se desplaza el elemento a la derecha
                j--;
            } else {
                break;
            }
        }
        arr[j + 1] = key;
    }
}

// Función auxiliar para copiar arreglos nativos
void copiarArreglo(const int origen[], int destino[], int n) {
    for (int i = 0; i < n; i++) {
        destino[i] = origen[i];
    }
}

// Función auxiliar para imprimir el arreglo
void imprimirArreglo(const int arr[], int n) {
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << (i < n - 1 ? ", " : "");
    }
    cout << "]";
}

int main() {
    int datosOriginales[] = {64, 25, 12, 22, 11, 90, 45, 33};
    int n = sizeof(datosOriginales) / sizeof(datosOriginales[0]);
    
    // Arreglo donde crearemos las copias para cada prueba
    int datosCopia[n];
    int comp, inter;

    // 1. Bubble Sort
    copiarArreglo(datosOriginales, datosCopia, n); // Creamos el "clon"
    bubbleSort(datosCopia, n, comp, inter);
    cout << "Bubble Sort  ---> Resultado: ";
    imprimirArreglo(datosCopia, n);
    cout << " | Comparaciones: " << comp << " | Intercambios: " << inter << endl;

    // 2. Selection Sort
    copiarArreglo(datosOriginales, datosCopia, n); // Creamos el "clon"
    selectionSort(datosCopia, n, comp, inter);
    cout << "Selection Sort -----> Resultado: ";
    imprimirArreglo(datosCopia, n);
    cout << " | Comparaciones: " << comp << " | Intercambios: " << inter << endl;

    // 3. Insertion Sort
    copiarArreglo(datosOriginales, datosCopia, n); // Creamos el "clon"
    insertionSort(datosCopia, n, comp, inter);
    cout << "Insertion Sort ----> Resultado: ";
    imprimirArreglo(datosCopia, n);
    cout << " | Comparaciones: " << comp << " | Desplazamientos: " << inter << endl;

    return 0;
}