//RETO 2 - La racha de lluvia
//Contexto: Se tiene el registro de un mes donde 1 significa que llovió y 0 que no. Un ingeniero ambiental necesita saber cuál fue el periodo más largo de días seguidos con lluvia.
//Se pide: Encontrar la longitud de la racha más larga de unos consecutivos en el arreglo {0,1,1,0,1,1,1,0,1}.
//Pista: Se resuelve con un solo recorrido y dos variables: la racha actual y la mejor racha vista hasta ahora. Cuando aparece un 0, la racha actual vuelve a cero.

#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Registro de días con lluvia (1) y sin lluvia (0)
    vector<int> llovias_rg = {0, 1, 1, 0, 1, 1, 1, 0, 1};
    
    // racha_actual: Cuenta cuántos '1' consecutivos van en la secuencia en curso
    // max_racha: Almacena la racha más larga registrada durante todo el recorrido
    int racha_actual = 0;
    int max_racha = 0;

    // Recorremos el arreglo de días usando un bucle for-each
    for (int diagnostico : llovias_rg) {
        
        // Caso 1: Si fue un día lluvioso (1)
        if (diagnostico == 1) {
            racha_actual++; // Incrementamos la racha actual en 1
            
            // Si la racha actual supera al récord histórico, actualizamos el récord
            if (racha_actual > max_racha) {
                max_racha = racha_actual;
            }
        } 
        // Caso 2: Si no llovió (0)
        else {
            // Se rompe la secuencia de días lluviosos, por lo que la racha vuelve a 0
            racha_actual = 0;
        }
    }

    // Mostramos el resultado final almacenado en el récord máximo
    cout << "Racha mas larga de lluvia: " << max_racha << " dias" << endl;

    return 0;
}
