//Invertir una cadena de texto recursivamente

#include <iostream>
#include <string>

using namespace std;

// Función que invierte un texto de forma recursiva
string invertir_cadena(string cadena) {
    // Caso base: si el texto tiene 0 o 1 carácter, se devuelve tal cual
    if (cadena.length() <= 1) {
        return cadena;
    } else {
        // Caso recursivo: se toma el último carácter y se concatena con la inversión del resto de la cadena
        return cadena.back() + invertir_cadena(cadena.substr(0, cadena.length() - 1));
        //cadena.back(): Obtiene el último carácter del texto actual.
        //cadena.substr(0, cadena.length() - 1): Obtiene una subcadena que excluye el último carácter.
    }
}

int main() {
    string cadena;
    cout << "Ingrese una cadena de texto: ";
    
    getline(cin, cadena); // Se usa getline para leer toda la línea, incluyendo espacios
    
    // Llamal a la función recursiva
    string cadena_invertida = invertir_cadena(cadena);
    
    // Muestra el resultado final en pantalla
    cout << "La cadena invertida es: " << cadena_invertida << endl;
    
    return 0;
}