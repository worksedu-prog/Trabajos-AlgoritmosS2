//RETO I   
//Contexto: La Sala Knuth registra cuántas personas hay en cada franja horaria (6 franjas) de lunes a viernes (5 días). La coordinación quiere reorganizar los horarios de monitoría.
//Se pide: Construir la matriz y responder tres cosas: cuál fue la franja más congestionada de toda la semana (con su día y hora), qué día tuvo mayor ocupación total, y cuáles franjas estuvieron siempre por debajo de 5 personas.
//Pista: Para la franja más congestionada necesitan guardar no solo el máximo, sino también en qué fila y columna lo encontraron.




#include <iostream>
#include <string>

using namespace std;

int main() {

    string dias[5] = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"}; // Dias de la semana

    int matriz_sala[5][6] = //Una matriz de 5 dias x 6 franjas
    {
        {11, 42, 3, 0, 5, 42},
        {21, 5, 0, 3, 4, 5},
        {2, 4, 6, 9, 6, 5},
        {4, 6, 17, 3, 2, 1},
        {3, 3, 2, 4, 1, 3}
    };


    // Ubicar la franja mas congestionada
    
    int MaxOcupacion = -1;
    int hora = 0;
    int diaMx = 0;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            if (matriz_sala[i][j] > MaxOcupacion) { // Actualizacion de variables
                MaxOcupacion = matriz_sala[i][j];
                diaMx = i;
                hora = j;
            }
        }
    }


    //Dia con mayor ocupacion

    int maxSumaDia = -1;
    int diaMasOcupado = 0;

    for (int i = 0; i < 5; i++) {
        int sumaFila = 0;
        for (int j = 0; j < 6; j++) {
            sumaFila += matriz_sala[i][j];
        }
        if (sumaFila > maxSumaDia) {
            maxSumaDia = sumaFila;
            diaMasOcupado = i;
        }
    }

    //Resultados 
    
    cout << "---- Resultados de la sala ----" << endl;
    cout << "1. Franja mas congestionada: " << dias[diaMx] 
         << " en la Franja " << (hora + 1) 
         << " con " << MaxOcupacion << " personas." << endl;

    cout << "2. Dia con mayor ocupacion total: " << dias[diaMasOcupado] 
         << " con un total de " << maxSumaDia << " personas." << endl;


    // Franjas siempre < 5 personas

    cout << "3. Franjas siempre por debajo de 5 personas: ";
    bool algunaFranja = false;

    // Recorremos columna por columna (franja por franja)
    for (int j = 0; j < 6; j++) {
        bool siempreBajo = true; // Asumimos que esta franja cumple
        
        for (int i = 0; i < 5; i++) { // Revisamos todos los dias para esta franja
            if (matriz_sala[i][j] >= 5) {
                siempreBajo = false; // Si algun dia llega a 5 o mas, falla
                break; // No hace falta seguir revisando este dia
            }
        }

        if (siempreBajo) {
            cout << "Franja " << (j + 1) << " ";
            algunaFranja = true;
        }
    }

    if (!algunaFranja) {
        cout << "Ninguna franja se mantuvo siempre por debajo de 5 personas.";
    }
    cout << endl;

    return 0;
}
