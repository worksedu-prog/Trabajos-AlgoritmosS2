//#La jerarquía honesta
//Contexto. Casi todos van a manejar entidades parecidas pero no iguales: estudiantes y administradores, recursos prestables y consumibles, sensores fijos y móviles.
//Se pide. Diseñar una jerarquía de al menos dos niveles donde la hija redefina un método del padre y aporte un atributo propio. En C++ usar virtual y destructor virtual. Justificar en tres líneas por qué era herencia y no composición.
//Pista: Herencia significa «es un». Si no pueden decir con naturalidad «un LibroDigital es un Recurso», lo que necesitan es que una clase contenga a la otra.

#include <iostream>

using namespace std;

class Usuario {
    private:
        string nombre;
        string correo;
    public:
        //Funcion de constructor de la clase Usuario
        Usuario(string nombre, string correo) : nombre(nombre), correo(correo) {}
        
        virtual string obtener_rol(){
            return "Usuario creado en el sistema";
        }
        virtual ~Usuario() = default;

        string get_nombre() {
            return nombre;
        }
        string get_correo() {
            return correo;
        }
};

class Estudiante : public Usuario {
    private:
        string carrera;
    public:
        //Funcion de constructor de la clase Estudiante
        Estudiante(string nombre, string correo, string carrera) : Usuario(nombre, correo), carrera(carrera) {}
        
        //Carrera del estudiante
        string obtener_rol() override {
            return "---Datos del estudiante---\nNombre: " + get_nombre() + "\nCorreo: " + get_correo() + "\nCarrera: " + carrera;
        }
};

int main() {

    Estudiante prueba("Juan Perez", "Sizaña@urgmail.com", "Ingeniería de Software");
    cout << prueba.obtener_rol() << endl;

    return 0;
}
