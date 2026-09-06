#include <iostream>
using namespace std;

class Objeto {
private:
    //Atributo estatico privado para que solo en uno se cuenten todos
    static int contador;

public:
    // Un constructor que se ejecuta solo cada vez que nace un objeto
    Objeto() {
        contador++; // Le suma 1 al contador
    }

    // Metodo que consultar el conteo y pues lo obtiene
    static int obtenerContador() {
        return contador;
    }
};

// Inicializamos la variable estática afuera (OBLIGATORIO en C++), usando el :: que es como decir "busca esto dentro de esta clase"
int Objeto::contador = 0;

int main() {
    // Consultamos la libreta antes de crear objetos, de la misma forma el ::
    cout << "Inicio: " << Objeto::obtenerContador() << endl; // Imprime 0

    // Creamos 3 objetos
    Objeto obj1;
    Objeto obj2;
    Objeto obj3;

    // Consultamos la cuenta final
    cout << "Objetos creados: " << Objeto::obtenerContador() << endl; // Imprime 3

    return 0;
}
