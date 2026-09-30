#include <iostream>
#include <chrono>   // Proporciona herramientas de medición de tiempo de alta precisión
#include <iomanip>  // Permite dar formato a la salida en consola como el número de decimales)

using namespace std;

/* 
 * 1. BUBBLE SORT (Algoritmo de la Burbuja)
 * Compara elementos y los intercambia si están desordenados.
 * Los elementos más grandes "flotan" hacia el final en cada pasada.
 */
void bubbleSort(int arr[], int n, int &comparaciones, int &intercambios, double &tiempo_ms) {
    // Inicializamos las métricas
    comparaciones = 0;
    intercambios = 0;
    
    // Capturamos el tiempo exacto antes de iniciar el algoritmo
    auto inicio = chrono::high_resolution_clock::now(); 

    // Bucle externo: controla el número de pasadas sobre el arreglo
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false; // Bandera para detectar si hubo al menos un intercambio en esta pasada

        // Bucle interno: compara elementos adyacentes hasta la parte aún no ordenada (n - i - 1)
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++; // Registramos cada comparación realizada entre arr[j] y arr[j + 1]

            // Si el elemento actual es mayor que el siguiente, están desordenados
            if (arr[j] > arr[j + 1]) {
                // Intercambio clásico usando una variable temporal
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                intercambios++; // Registramos el intercambio de posición
                swapped = true; // Confirmamos que el arreglo sufrió modificaciones
            }
        }

        // Optimización: Si no hubo intercambios en esta pasada, el arreglo ya está completamente ordenado
        if (!swapped) break; 
    }

    // Capturamos el tiempo al finalizar
    auto fin = chrono::high_resolution_clock::now(); 
    
    // Calculamos la diferencia de tiempo en milisegundos (ms) y la guardamos en la variable por referencia
    tiempo_ms = chrono::duration<double, milli>(fin - inicio).count();
}

/* 
 * 2. SELECTION SORT (Algoritmo de Selección)
 * Busca repetidamente el elemento mínimo de la lista no ordenada 
 * y lo coloca al principio de la lista
 */

void selectionSort(int arr[], int n, int &comparaciones, int &intercambios, double &tiempo_ms) {
    comparaciones = 0;
    intercambios = 0;

    auto inicio = chrono::high_resolution_clock::now(); 

    // Bucle externo: avanza la frontera del subarreglo ordenado posición por posición
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i; // Asumimos inicialmente que el elemento actual es el menor

        // Bucle interno: busca el índice del verdadero valor mínimo en el resto del arreglo
        for (int j = i + 1; j < n; j++) {
            comparaciones++; // Registramos la comparación
            if (arr[j] < arr[minIdx]) {
                minIdx = j; // Actualizamos la posición del nuevo mínimo encontrado
            }
        }

        // Solo intercambiamos si el mínimo encontrado no estaba ya en la posición 'i'
        if (minIdx != i) {
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;

            intercambios++; // Registramos el intercambio
        }
    }

    auto fin = chrono::high_resolution_clock::now(); 
    tiempo_ms = chrono::duration<double, milli>(fin - inicio).count();
}

/* 
 * 3. INSERTION SORT (Algoritmo de Inserción)
 * Construye el arreglo ordenado elemento por elemento, insertando cada valor
 * en su lugar, desplazando los valores mayores.
 */
void insertionSort(int arr[], int n, int &comparaciones, int &desplazamientos, double &tiempo_ms) {
    comparaciones = 0;
    desplazamientos = 0; // Se cuentan desplazamientos en lugar de intercambios dobles

    auto inicio = chrono::high_resolution_clock::now(); 

    // Empezamos desde el segundo elemento (índice 1), asumiendo que el primero ya está "ordenado"
    for (int i = 1; i < n; i++) {
        int key = arr[i]; // El elemento que intentaremos insertar en la sublista ordenada
        int j = i - 1;    // Índice para recorrer la parte ordenada de derecha a izquierda

        // Movemos los elementos del subarreglo ordenado que son mayores a 'key' una posición a la derecha
        while (j >= 0) {
            comparaciones++; // Evaluamos si el elemento en 'j' es mayor que 'key'
            if (arr[j] > key) {
                arr[j + 1] = arr[j]; // Desplazamiento hacia la derecha
                desplazamientos++;
                j--; // Avanzamos hacia la izquierda
            } else {
                break; // Si encontramos un valor menor o igual a 'key', detenemos la búsqueda
            }
        }
        
        // Insertamos la 'key' en su posición ordenada correspondiente
        arr[j + 1] = key;
    }

    auto fin = chrono::high_resolution_clock::now(); 
    tiempo_ms = chrono::duration<double, milli>(fin - inicio).count();
}

/* 
 * Función que copia los elementos del arreglo origen al arreglo destino.
 * Permite reiniciar los datos para evaluar cada algoritmo bajo exactamente las mismas condiciones.
 * (como el .copy() ewn python)
 */
void copiarArreglo(const int origen[], int destino[], int n) {
    for (int i = 0; i < n; i++) {
        destino[i] = origen[i];
    }
}

/* 
 * Función que imprime el arreglo en formato [e1, e2, e3, ...]
 */
void imprimirArreglo(const int arr[], int n) {
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << (i < n - 1 ? ", " : "");
    }
    cout << "]";
}

/* 
 * Función para generar un arreglo inverso para poder hacer pruebas (peor caso).
 */
void generarRangoInverso(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = n - i; // Genera elementos desde 'n' hasta 1
    }
}

int main() {
    int comp, inter;
    double tiempo;

    cout << fixed << setprecision(4);

    // Parte C:
    int datosOriginales[] = {64, 25, 12, 22, 11, 90, 45, 33};
    int n = sizeof(datosOriginales) / sizeof(datosOriginales[0]);
    int datosCopia[n];

    cout << "Parte C: pruebas basicas" << endl;
    copiarArreglo(datosOriginales, datosCopia, n);
    bubbleSort(datosCopia, n, comp, inter, tiempo);
    cout << "Bubble Sort    | Comp: " << comp << " | Inter: " << inter << " | Tiempo: " << tiempo << " ms" << endl;

    copiarArreglo(datosOriginales, datosCopia, n);
    selectionSort(datosCopia, n, comp, inter, tiempo);
    cout << "Selection Sort | Comp: " << comp << " | Inter: " << inter << " | Tiempo: " << tiempo << " ms" << endl;

    copiarArreglo(datosOriginales, datosCopia, n);
    insertionSort(datosCopia, n, comp, inter, tiempo);
    cout << "Insertion Sort | Comp: " << comp << " | Despl: " << inter << " | Tiempo: " << tiempo << " ms" << endl;


    // Parte E: Medición de listas con rangos
    cout << "\nParte E: Medición de listas con rangos con (Insertion Sort)" << endl;
    
    int tamanios[] = {1000, 2000, 4000};
    double tiempos_rangos[3];

    for (int k = 0; k < 3; k++) {
        int N = tamanios[k];
        int* arregloRango = new int[N]; // Asignación dinámica para arreglos grandes

        generarRangoInverso(arregloRango, N); // Rango de N hasta 1
        insertionSort(arregloRango, N, comp, inter, tiempo);

        tiempos_rangos[k] = tiempo;
        cout << "Rango = " << N << " | Tiempo: " << tiempo << " ms" << endl;

        delete[] arregloRango; // Liberamos la memoria
    }

    // Cálculo de los factores
    double factor1 = tiempos_rangos[1] / tiempos_rangos[0];
    double factor2 = tiempos_rangos[2] / tiempos_rangos[1];

    cout << "\nFactor 1 (2000 / 1000): " << factor1 << endl;
    cout << "Factor 2 (4000 / 2000): " << factor2 << endl;

    return 0;
}