//Implementen el deshacer de su proyecto con una pila. Los de la tres, la última asignación de monitoría. Ese es un requerimiento explícito de su línea.


#include <iostream>
#include <sstream>
#include <string>

using namespace std;// Deshace la última asignación realizada



//void deshacerAsignacion(PilaAsignaciones& historial) {
//    if (historial.isEmpty()) {
//        cout << "No hay asignaciones para deshacer." << endl;
//        return;
//    }
//
//    Asignacion ultima = historial.top();   // Leer la cima
//    historial.pop();                       // Quitarla de la pila
//
//    // Restaurar la materia anterior
//    ultima.monitor->asignarMateria(ultima.materiaAnterior);
//    
//    cout << "Se deshizo la asignacion de " << ultima.materiaNueva
//    << " a " << ultima.monitor->getNombres() << "." << endl;
//}