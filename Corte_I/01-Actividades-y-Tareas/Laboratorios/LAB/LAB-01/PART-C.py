# 1. Definición de la clase base (PuntoAcopio)
class PuntoAcopio:
    # El constructor (__init__) inicializa los atributos cuando se crea el objeto
    def __init__(self, codigo, barrio, total_recogido):
        self.codigo = codigo
        self.barrio = barrio
        self.total_recogido = total_recogido

    # Método para registrar más recolección sumando kilos
    def registrar_recoleccion(self, kilos):
        self.total_recogido += kilos

    # Método para verificar si supera una meta dada
    def supera_meta(self, meta):
        return self.total_recogido >= meta

    # Método para mostrar la descripción básica del punto
    def mostrar_descripcion(self):
        print(f"Punto [Codigo: {self.codigo}, Barrio: {self.barrio}, Total: {self.total_recogido} kg]")

# 2. Definición de la clase derivada (MaterialEspecial) que hereda de PuntoAcopio
class MaterialEspecial(PuntoAcopio):
    # Constructor de la clase hija
    def __init__(self, codigo, barrio, total_recogido, tipo_material):
        # super().__init__() llama al constructor de la clase padre para heredar sus atributos
        super().__init__(codigo, barrio, total_recogido)
        # Atributo propio y exclusivo de esta clase hija
        self.tipo_material = tipo_material

    # Redefinición del método (Polimorfismo: adapta el comportamiento para incluir el material)
    def mostrar_descripcion(self):
        print(f"Material Especial [Codigo: {self.codigo}, Barrio: {self.barrio}, Material: {self.tipo_material}, Total: {self.total_recogido} kg]")

# 3. Crear una lista mezclando objetos de ambas clases (clase base y clase derivada)
central = [
    PuntoAcopio("P01", "Chico", 150.5),
    PuntoAcopio("P02", "Usaquen", 90.0),
    MaterialEspecial("M01", "Teusaquillo", 210.0, "Electronicos"),
    MaterialEspecial("M02", "Chapinero", 305.5, "Pilas y Baterias")
]

# 4. Recorrer la lista llamando al método. 
# Gracias al polimorfismo, Python identifica automáticamente si debe ejecutar 
# la versión del padre o la del hijo para cada elemento.
print("--- REPORTE DE PUNTOS Y MATERIALES ---")
for item in central:
    item.mostrar_descripcion()
