#include <iostream>
using namespace std;

int main() {
    // 1. Declarar e inicializar la matriz estática de 4 filas (puntos) x 6 columnas (días)
    double matriz[4][6] = {
        {12.5, 0.0, 15.0, 8.5, 20.0, 14.0},
        {5.0, 10.0, 0.0, 22.5, 18.0, 11.5},
        {30.0, 25.5, 19.0, 0.0, 14.5, 20.0},
        {8.0, 12.0, 10.5, 15.0, 0.0, 25.0}
    };

    // 2. Arreglos para guardar la suma total de cada fila y de cada columna, inicializados en 0
    double totalPunto[4] = {0};
    double totalDia[6] = {0};
    int ceros = 0; // Contador para días sin recolección

    // 3. Recorrer toda la matriz con ciclos anidados (filas y columnas)
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 6; j++) {
            totalPunto[i] += matriz[i][j]; // Suma el valor al total de ese punto (fila)
            totalDia[j] += matriz[i][j];   // Suma el valor al total de ese día (columna)
            
            // 4. Si el valor es 0, sumamos 1 al contador de días sin operar
            if(matriz[i][j] == 0.0) {
                ceros++;
            }
        }
    }

    // 5. Imprimir el total acumulado por cada punto de acopio
    cout << "--- TOTAL POR PUNTO DE ACOPIO ---\n";
    for(int i = 0; i < 4; i++) {
        cout << "Punto " << i + 1 << ": " << totalPunto[i] << " kg\n";
    }

    // 6. Imprimir el total acumulado por cada día de la semana
    cout << "\n--- TOTAL POR DIA ---\n";
    for(int j = 0; j < 6; j++) {
        cout << "Dia " << j + 1 << ": " << totalDia[j] << " kg\n";
    }

    // 7. Encontrar el punto más productivo (el valor mayor en totalPunto)
    int maxPunto = 0;
    for(int i = 1; i < 4; i++) {
        if(totalPunto[i] > totalPunto[maxPunto]) {
            maxPunto = i; // Guarda el índice del punto con más kilos
        }
    }
    cout << "\nPunto mas productivo: Punto " << maxPunto + 1 << " (" << totalPunto[maxPunto] << " kg)\n";

    // 8. Encontrar el día de menor recolección (el valor menor en totalDia)
    int minDia = 0;
    for(int j = 1; j < 6; j++) {
        if(totalDia[j] < totalDia[minDia]) {
            minDia = j; // Guarda el índice del día con menos kilos
        }
    }
    cout << "Dia de menor recoleccion: Dia " << minDia + 1 << " (" << totalDia[minDia] << " kg)\n";

    // 9. Mostrar cuántos días tuvieron 0 kilos de recolección
    cout << "Registros con valor 0 (dias sin operar): " << ceros << "\n";

    return 0;
}
