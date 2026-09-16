//Potencia de a elevado a la b, recursiva. 
// Y después de que funcione, mejórenla: si b es par, a elevado a la b es igual a a elevado a la b dividido entre 2, al cuadrado. 
// Con eso pasan de n llamadas a log n llamadas. Compárenlo midiendo.

#include <iostream>
using namespace std;

int potencia(int a, int b) {
    if (b == 0) {
        return 1; // Cualquier número elevado a la potencia 0 es 1
    } else if (b % 2 == 0) {
        int exponente_par = potencia(a, b / 2);
        return exponente_par * exponente_par; // Si b es par, a^b = (a^(b/2))^2
    } else {
        return a * potencia(a, b - 1); // Si b es impar, a^b = a * a^(b-1)
    }
}

int main() {
    int a, b;
    cout << "Ingrese la base: ";
    cin >> a;
    cout << "Ingrese el exponente: ";
    cin >> b;

    int resultado = potencia(a, b);
    cout << a << " elevado a la " << b << " es: " << resultado << endl;

    return 0;
}