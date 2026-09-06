class Objeto:
    # Atributo estatico que se pone fuera de las funciones para que solo halla uno
    contador = 0

    def __init__(self):
        # Cada vez que nace un objeto, le suma 1 al contador de la clase (Si el contador estuviera aca habria un contador
        # para cada objeto y no se quiere eso)
        Objeto.contador += 1

    # Método para obtener el contador del contador
    def obtener_contador(self):
        return Objeto.contador


# Hacemos una prueba

# Creamos 3 objetos
obj1 = Objeto()
obj2 = Objeto()
obj3 = Objeto()

print("Objetos creados:", obj3.obtener_contador())  # Imprime 3
