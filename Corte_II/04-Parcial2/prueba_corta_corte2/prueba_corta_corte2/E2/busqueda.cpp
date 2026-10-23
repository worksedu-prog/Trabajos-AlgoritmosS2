// ============================================================
//  Prueba corta · Segundo corte · EJERCICIO 2  (25 puntos)
//  Tema: busqueda binaria
//  Sistema: RedAcopio — localizacion de codigos de material
//
//  Este archivo NO tiene main(): el main esta en pruebas_e2.cpp
//  NO MODIFIQUE el archivo pruebas_e2.cpp
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_e2 busqueda.cpp pruebas_e2.cpp
//     ./pruebas_e2
//
//  Se reportan DOS fallas:
//   1. Devuelve -1 para codigos que si estan en el arreglo.
//   2. Con algunos valores el sanitizer aborta el programa.
// ============================================================



int buscarCodigo(int v[], int n, int x) {
    int izq = 0, der = n - 1;
    while (izq <= der) {
        int medio = izq + (der - izq) / 2; // Cambio la operación
        
        if (v[medio] == x) 
            return medio;
        
        if (v[medio] < x) {
            izq = medio + 1; // Se le cambia a sumar +1
        } else {
            der = medio - 1; // Se le cambia a sumar -1
        }
    }
    return -1; // No encontrado
}