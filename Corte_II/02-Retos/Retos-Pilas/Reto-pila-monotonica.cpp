
//temperaturas diarias
//Para cada dia, calculamos cuantos dias hay que esperar hasta que haga más calor. Es el mismo patrón del ejmeplo 1 pero 
//la respuesta es una distancia en lugard e un valor.

//Entrada: {73, 74, 75, 71, 69, 72, 76, 73}
//Salida: {1, 1, 4, 2, 1, 1, 0, 0}


#include <bits/stdc++.h>

using namespace std;

vector<int> siguienteMayor(const vector<int>& a) {
    int n = a.size();
    vector<int> result(n, 0);
    stack<int> pila;

    for (int i = 0; i < n; ++i) {
        while (!pila.empty() && a[i] > a[pila.top()]) {
            result[pila.top()] = i - pila.top();
            pila.pop();
        }
        pila.push(i);
    }

    return result;
}

int main() {
    vector<int> a={73, 74, 75, 71, 69, 72, 76, 73};
    for (int x: siguienteMayor(a)) cout<<x<<" ";
}

