# Clase base (padre)
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Atributo del padre
        self.email = email    # Atributo del padre

    # Método base para ser redefinido
    def obtener_rol(self):
        return "Usuario base del sistema"


# Clase hija que hereda de Usuario
class Estudiante(Usuario):
    def __init__(self, nombre, email, carrera):
        super().__init__(nombre, email)  # Reutiliza la inicialización del padre
        self.carrera = carrera          # Atributo propio del hijo

    # Redefinición (override) del método del padre
    def obtener_rol(self):
        return "Estudiante de " + self.carrera


# Ejecución directa del código
estudiante = Estudiante("Sofía", "sofia@universidad.edu", "Ingeniería de Sistemas")

print("Nombre:", estudiante.nombre)
print("Rol:", estudiante.obtener_rol())
