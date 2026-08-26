class Usuario:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def obtener_rol(self) -> str:
        return "Usuario base del sistema"


class Estudiante(Usuario):
    def __init__(self, nombre: str, email: str, carrera: str):
        super().__init__(nombre, email)
        self.carrera = carrera  # Atributo propio

    def obtener_rol(self) -> str:  # Redefinición / Override
        return f"Estudiante de {self.carrera}"


# Ejemplo de uso
if __name__ == "__main__":
    estudiante = Estudiante("Sofía", "sofia@universidad.edu", "Ingeniería de Sistemas")
    print(f"Nombre: {estudiante.nombre}")
    print(f"Rol: {estudiante.obtener_rol()}")
