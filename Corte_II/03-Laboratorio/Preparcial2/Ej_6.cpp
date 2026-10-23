//Ejercicio 6 · Escritura de código  ·  C++  ·  (implementación) 
//Escriba la función fusionar, que recibe dos vectores ya ordenados de forma no decreciente y devuelve un vector 
//nuevo con todos sus elementos ordenados. Es el paso de combinación de Merge Sort. No use sort ni ningún algoritmo 
//de ordenamiento: aproveche que las entradas ya están ordenadas. 

#include <iostream>
#include <vector>

using namespace std;

vector<int> fusionar(const vector<int>& a, const vector<int>& b) {
    vector <int> resultado;
    int i = 0; //Indice para el vector a
    int j = 0; //indice para el vector b



    while (i < a.size() && j < b.size()){
        if (a[i] <= b[j]) {
            resultado.push_back(a[i]);
            i++;
        } else {
            resultado.push_back(b[j]);
            j++;
        }
    }

    //Si sobraron elementos en el vector a, agregarlos todos
    while (i < a.size()) {
        resultado.push_back(a[i]);
        i++;
    }

    while (j < b.size()){
        resultado.push_back(b[j]);
        j++;
    }

    return resultado;
}

int main(){
    vector <int> a = {5, 18, 27, 40};
    vector <int> b = {9, 18, 33};

    vector <int> resultado = fusionar(a, b);

    //Debido a que es un vector se debe imprimir por un bucle for

    cout << "Vector fusionado es: ";
    for( int x : resultado) {
        cout << x << " ";
    }

    cout << endl;

    return 0;
}


// Caso de prueba: 
//   a = {5, 18, 27, 40}   b = {9, 18, 33} 
//   resultado esperado: 5 9 18 18 27 33 40   (tamaño 7) 