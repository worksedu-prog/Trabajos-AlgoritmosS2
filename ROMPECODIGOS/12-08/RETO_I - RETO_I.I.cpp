//RETO 1·El sensor mentiroso   [Básico]
//Contexto: Una estación de calidad del aire del barrio reporta lecturas cada hora, pero el sensor falla de vez en cuando y, 
//cuando falla, escribe el valor -999.
//Se pide: Calcular el promedio real de las lecturas ignorando las lecturas dañadas, e informar cuántas lecturas se descartaron. 
//Usar el arreglo {20, -999, 22, 24, -999, 26}.
//Pista: Necesitan dos contadores: uno para la suma y otro para cuántos datos válidos encontraron. No se puede dividir 
//entre el tamaño del arreglo.



#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Vector con los datos reportados por el sensor de calidad del aire
    vector<int> lecturas = {20, -999, 22, 24, -999, 26};

    // Variables de control:
    // suma_validos: Acumulador para sumar únicamente los datos correctos
    // datos_validos: Contador de lecturas correctas (diferentes de -999)
    // datos_descartados: Contador de lecturas erróneas (-999)
    double suma_validos = 0;
    int datos_validos = 0;
    int datos_descartados = 0;

    // Recorremos cada lectura del vector usando un bucle for-each
    for (int lectura : lecturas) {
        
        // Evaluamos si la lectura actual es una falla del sensor (-999)
        if (lectura == -999) {
            datos_descartados++; // Incrementamos el contador de errores
        } else {
            suma_validos += lectura; // Acumulamos el valor en la suma general
            datos_validos++;         // Incrementamos el contador de lecturas válidas
        }
    }

    // Mostramos los conteos de datos procesados
    cout << "----Análisis del aire----" << endl;
    cout << "Lecturas descartadas: " << datos_descartados << endl;
    cout << "Lecturas válidas encontradas: " << datos_validos << endl;

    // Validación de seguridad para evitar la división entre cero si todos los datos fueran -999
    if (datos_validos > 0) {
        // Promedio calculado solo con la cantidad de datos válidos (no el tamaño total del vector)
        double promedio = suma_validos / datos_validos;
        cout << "Promedio real de lecturas: " << promedio << endl;
    } else {
        cout << "No hubo lecturas válidas para calcular el promedio." << endl;
    }

    return 0;
}



//RETO 1.1: Ahora el usuario debera ingresar los datos a tratar



#include <iostream>
#include <vector>

using namespace std;

int main() {
    int total_lecturas;

    cout << "¿Cuántas lecturas desea ingresar?: ";
    cin >> total_lecturas;

    vector<int> lecturas;
    
    // Bucle para pedir cada dato al usuario
    for (int i = 0; i < total_lecturas; i++) {
        int valor;
        cout << "Ingrese la lectura " << i + 1 << ": ";
        cin >> valor;
        lecturas.push_back(valor); // Se agrega al vector
    }
    // Variables de control:
    // suma_validos: Acumulador para sumar únicamente los datos correctos
    // datos_validos: Contador de lecturas correctas (diferentes de -999)
    // datos_descartados: Contador de lecturas erróneas (-999)
    double suma_validos = 0;
    int datos_validos = 0;
    int datos_descartados = 0;

    // Recorremos cada lectura del vector usando un bucle for-each
    for (int lectura : lecturas) {
        
        // Evaluamos si la lectura actual es una falla del sensor (-999)
        if (lectura <= -999) {
            datos_descartados++; // Incrementamos el contador de errores
        } else {
            suma_validos += lectura; // Acumulamos el valor en la suma general
            datos_validos++;         // Incrementamos el contador de lecturas válidas
        }
    }

    // Mostramos los conteos de datos procesados
    cout << "----Análisis del aire----" << endl;
    cout << "Lecturas descartadas: " << datos_descartados << endl;
    cout << "Lecturas válidas encontradas: " << datos_validos << endl;

    // Validación de seguridad para evitar la división entre cero si todos los datos fueran -999
    if (datos_validos > 0) {
        // Promedio calculado solo con la cantidad de datos válidos (no el tamaño total del vector)
        double promedio = suma_validos / datos_validos;
        cout << "Promedio real de lecturas: " << promedio << endl;
    } else {
        cout << "No hubo lecturas válidas para calcular el promedio." << endl;
    }

    return 0;
}


