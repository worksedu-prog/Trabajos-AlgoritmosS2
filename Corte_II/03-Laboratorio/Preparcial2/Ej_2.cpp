//Ejercicio 2 · Detección de errores en recursión  ·  C++  ·  (depuración) 
//La función debe devolver cuántos elementos de v[0..n-1] son mayores o iguales que umbral. Se invoca con contar(v, 
//v.size(), 20) sobre v = {12, 45, 7, 38, 60, 19, 23}. Identifique los dos defectos, explique por qué el programa es 
//incorrecto y escriba la versión corregida. 

#include <iostream> 
#include <vector> 
using namespace std; 



//int contar(const vector <int>& v, int n, int umbral) {
//    if (n < 0) return 0; //El caso base nos comenta que 0 es mayor a n cuando deberia ser n == 0
//    if (v[n] >= umbral) //La maxima posición que se puede acceder es n - 1 en la lista deb
//        return 1 + contar(v, n - 1, umbral);
//    return contar(v, n-1, umbral);
//}


//Corrección del codigo

int contar(const vector <int>& v, int n, int umbral) {
    if (n == 0) return 0;
    if (v [n -1] >= umbral)
        return 1 + contar(v, n - 1, umbral);
    return contar(v, n - 1, umbral);
}

int main() {
    vector <int> v = {12, 45, 7, 38, 60, 19, 23};

    int resultado = contar(v, v.size(), 20);
    cout << "Cantidad de elementos mayores o iguales al umbral: " << resultado << endl;

return 0;
}