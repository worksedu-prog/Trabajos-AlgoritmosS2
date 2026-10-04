//Parte B — El deshacer Implementen una pila que registre las últimas operaciones del sistema y permita deshacer la última. 
//Debe deshacer de verdad, no solo borrar el registro: si la operación fue un préstamo, deshacerla devuelve el recurso a disponible.


#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Una solicitud con un estado, que es lo que se va a poder deshacer
struct Solicitud {
    int id;
    string estado;   // "Pendiente" o "Atendida"
};

// Una operación registrada: qué se hizo y sobre cuál solicitud
struct Operacion {
    string tipo;   // "CREAR" o "ATENDER"
    int id;        // id de la solicitud afectada
};

// Nodo de la pila: guarda una operación y apunta a la que está debajo
struct NodoPila {
    Operacion op;
    NodoPila* siguiente;
};

// PILA (LIFO): la última operación registrada es la primera en deshacerse
class Pila {
    NodoPila* tope = nullptr;   // apunta a la última operación registrada

public:
    // APILAR: registra una operación encima de las anteriores. Costo O(1).
    void apilar(Operacion op) {
        tope = new NodoPila{op, tope};   // el nuevo apunta al tope anterior y pasa a ser el tope
    }

    // DESAPILAR: saca y devuelve la última operación
    // Solo llamarlo si la pila NO está vacía.
    Operacion desapilar() {
        NodoPila* viejo = tope;       // guardamos el nodo del tope
        Operacion op = viejo->op;     // copiamos la operación para devolverla
        tope = viejo->siguiente;      // el tope baja al nodo de abajo
        delete viejo;                 // liberamos la memoria
        return op;
    }

    // VACIA: true si no hay operaciones registradas
    bool vacia() {
        return tope == nullptr;
    }
};

// SISTEMA: tiene las solicitudes y la pila con el registro de operaciones
class Sistema {
    vector<Solicitud> solicitudes;
    Pila historial;

    // Busca una solicitud por id y devuelve su posición (-1 si no existe)
    int buscar(int id) {
        for (int i = 0; i < (int)solicitudes.size(); i++) {
            if (solicitudes[i].id == id) return i;
        }
        return -1;
    }

public:
    // CREAR: agrega la solicitud como Pendiente y registra la operación
    void crear(int id) {
        solicitudes.push_back({id, "Pendiente"});
        historial.apilar({"CREAR", id});
        cout << "Creada solicitud " << id << endl;
    }

    // ATENDER: cambia el estado a Atendida y registra la operación
    void atender(int id) {
        int pos = buscar(id);
        if (pos == -1 || solicitudes[pos].estado == "Atendida") {
            cout << "No se puede atender la solicitud " << id << endl;
            return;
        }
        solicitudes[pos].estado = "Atendida";
        historial.apilar({"ATENDER", id});
        cout << "Atendida solicitud " << id << endl;
    }

    // DESHACER: saca la última operación y REVIERTE su efecto de verdad
    void deshacer() {
        if (historial.vacia()) {
            cout << "No hay nada que deshacer." << endl;
            return;
        }
        Operacion op = historial.desapilar();

        if (op.tipo == "CREAR") {
            // Deshacer un crear = la solicitud deja de existir.
            // Por ser LIFO, la solicitud a quitar siempre es la última del vector.
            solicitudes.pop_back();
            cout << "Deshecho CREAR: se elimino la solicitud " << op.id << endl;
        } else if (op.tipo == "ATENDER") {
            // Deshacer un atender = la solicitud vuelve a estar Pendiente
            solicitudes[buscar(op.id)].estado = "Pendiente";
            cout << "Deshecho ATENDER: la solicitud " << op.id << " vuelve a Pendiente" << endl;
        }
    }

    // Muestra todas las solicitudes con su estado
    void mostrar() {
        cout << "Solicitudes: ";
        if (solicitudes.empty()) cout << "(ninguna)";
        for (int i = 0; i < (int)solicitudes.size(); i++) {
            cout << "[" << solicitudes[i].id << ": " << solicitudes[i].estado << "] ";
        }
        cout << endl;
    }
};

int main() {
    Sistema s;

    cout << "--- Crear y atender ---" << endl;
    s.crear(1);
    s.crear(2);
    s.atender(1);
    s.mostrar();     

    cout << "\n--- Deshacer el atender ---" << endl;
    s.deshacer();
    s.mostrar();     

    cout << "\n--- Deshacer un crear ---" << endl;
    s.deshacer();
    s.mostrar();     
    cout << "\n--- Deshacer todo y pasarse ---" << endl;
    s.deshacer();    
    s.mostrar();
    s.deshacer();    

    return 0;
}