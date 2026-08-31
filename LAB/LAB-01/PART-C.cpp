#include <iostream>
#include <string>
using namespace std;

// 1. Definición de la clase base (PuntoAcopio) que sirve como plantilla general
class PuntoAcopio {
protected:
    // Atributos protegidos: accesibles para esta clase y sus clases hijas (herencia)
    string codigo;
    string barrio;
    double totalRecogido;

public:
    // 2. Constructor: inicializa los atributos cuando se crea un objeto de la clase base
    PuntoAcopio(string cod, string barr, double total) {
        codigo = cod;
        barrio = barr;
        totalRecogido = total;
    }

    // 3. Destructor virtual: indispensable al usar herencia y punteros para liberar 
    // correctamente la memoria de las clases hijas y evitar fugas.
    virtual ~PuntoAcopio() {}

    // 4. Método para sumar kilos a la recolección acumulada del punto
    void registrarRecoleccion(double kilos) {
        totalRecogido += kilos;
    }

    // 5. Método para evaluar si el total recogido es mayor o igual a una meta dada
    bool superaMeta(double meta) {
        return totalRecogido >= meta;
    }

    // 6. Método virtual: permite aplicar polimorfismo. Las clases hijas pueden sobrescribirlo.
    virtual void mostrarDescripcion() {
        cout << "Punto [Codigo: " << codigo << ", Barrio: " << barrio << ", Total: " << totalRecogido << " kg]\n";
    }
};

// 7. Definición de la clase derivada (MaterialEspecial) que hereda de PuntoAcopio
class MaterialEspecial : public PuntoAcopio {
private:
    string tipoMaterial; // Atributo exclusivo y privado de esta clase hija

public:
    // 8. Constructor de la clase hija: reutiliza el constructor del padre usando ':' 
    // y añade la inicialización de su propio atributo.
    MaterialEspecial(string cod, string barr, double total, string material) 
        : PuntoAcopio(cod, barr, total) {
        tipoMaterial = material;
    }

    // 9. Sobrescritura (override): adapta el método del padre para mostrar el material especial
    void mostrarDescripcion() override {
        cout << "Material Especial [Codigo: " << codigo << ", Barrio: " << barrio << ", Material: " << tipoMaterial << ", Total: " << totalRecogido << " kg]\n";
    }
};

int main() {
    // 10. Declarar un arreglo de punteros a la clase base (PuntoAcopio*). 
    // Esto permite almacenar tanto objetos del padre como de la clase hija (Polimorfismo).
    PuntoAcopio* central[4];
    
    // 11. Instanciar objetos dinámicamente en el heap usando 'new'
    central[0] = new PuntoAcopio("P01", "Chico", 150.5);
    central[1] = new PuntoAcopio("P02", "Usaquen", 90.0);
    central[2] = new MaterialEspecial("M01", "Teusaquillo", 210.0, "Electronicos");
    central[3] = new MaterialEspecial("M02", "Chapinero", 305.5, "Pilas y Baterias");

    // 12. Recorrer el arreglo y llamar a la función. 
    // Gracias a la palabra 'virtual', C++ ejecuta la versión correcta del método según el objeto.
    cout << "--- REPORTE DE PUNTOS Y MATERIALES ---\n";
    for(int i = 0; i < 4; i++) {
        central[i]->mostrarDescripcion();
    }

    // 13. Liberar explícitamente la memoria de cada objeto creado con 'new' para evitar fugas (memory leaks)
    for(int i = 0; i < 4; i++) {
        delete central[i];
    }

    return 0;
}
