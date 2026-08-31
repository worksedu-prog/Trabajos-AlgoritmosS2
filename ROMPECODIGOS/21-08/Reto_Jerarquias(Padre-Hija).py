#La jerarquía honesta
#Contexto. Casi todos van a manejar entidades parecidas pero no iguales: estudiantes y administradores, recursos prestables y consumibles, sensores fijos y móviles.
#Se pide. Diseñar una jerarquía de al menos dos niveles donde la hija redefina un método del padre y aporte un atributo propio. En C++ usar virtual y destructor virtual. Justificar en tres líneas por qué era herencia y no composición.
#Pista: Herencia significa «es un». Si no pueden decir con naturalidad «un LibroDigital es un Recurso», lo que necesitan es que una clase contenga a la otra.
# Clase base (padre)
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Atributo del padre
        self.email = email    # Atributo del padre



    # Método base para ser redefinido (Es una función NO Confundir con def __init__)
    def obtener_rol(self):
        return "Usuario creado en el sistema"  #Con esta funcion se crea el polimorfismo y asi se crea "las distintas carreras"
    #POLIMORFISMO: MUCHAS FORMAS
    #El metodo devuelve unicamente una cadena de texto
    
    
# Clase hija que hereda de Usuario
class Estudiante(Usuario):
    def __init__(self, nombre, email, carrera):
        super().__init__(nombre, email)  # Reutiliza la inicialización del padre
        self.carrera = carrera          # Atributo propio del hijo

    # Redefinición o sobreescribe el método del padre usando, devolviendo o returnando la carrera
    def obtener_rol(self):
        return f"Estudiante de {self.carrera}"


# Ejecución directa del código
estudiante = Estudiante("Sofía", "sofia@universidad.edu", "Ingeniería de Sistemas") #Se crea una estudiante como ejemplo

print("Nombre:", estudiante.nombre)
print("Rol:", estudiante.obtener_rol())
print("Email:", estudiante.email)
