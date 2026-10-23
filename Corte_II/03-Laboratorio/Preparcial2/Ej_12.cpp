#include <iostream>
#include <vector>
#include <list>

using namespace std;

int main() {
    int M = 7;
    vector<list<int>> tabla(M);
    vector<int> claves = {23, 15, 42, 9, 36, 51, 28, 17};
    
    int colisiones = 0;
    
    // Inserción en la tabla hash con función h(k) = k % 7
    for (int k : claves) {
        int h = k % M;
        if (!tabla[h].empty()) {
            colisiones++; // Si el bucket ya tiene elementos, cuenta como colisión
        }
        tabla[h].push_back(k);
    }
    
    // Mostrar el contenido de cada bucket
    for (int i = 0; i < M; i++) {
        cout << "Bucket " << i << ": [";
        auto it = tabla[i].begin();
        while (it != tabla[i].end()) {
            cout << *it;
            it++;
            if (it != tabla[i].end()) cout << ", ";
        }
        cout << "]" << endl;
    }
    
    cout << "Numero total de colisiones: " << colisiones << endl;
    
    return 0;
}