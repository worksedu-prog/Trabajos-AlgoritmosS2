#Cuatro: Recorran e impriman su lista enlazada de forma recursiva, en orden inverso, sin usar ninguna estructura auxiliar. 
# Cuando les salga, van a entender por qué la recursión y las estructuras enlazadas van juntas.
#PISTA PARA EL RETO 4: Si imprimen antes de la llamada recursiva sale en orden normal; si imprimen después, sale invertido. 
# Ese descubrimiento es el que prepara los recorridos preorden y postorden de árboles en la Sesión 35. No se los diga: déjelos encontrarlo.

class Vagon:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None  # Enganche al siguiente vagón

# Función recursiva
def imprimir_tren_inverso(vagon):
    # Caso Base: Si no hay más vagones (llegamos al fin de la vía)
    if vagon is None:
        return
    
    # 1. PASO RECURSIVO: Caminamos hasta el fondo PRIMERO
    imprimir_tren_inverso(vagon.siguiente)
    
    # 2. IMPRESIÓN: Ocurre al REGRESAR del recorrido
    print(vagon.numero)

# --- Armamos un tren --- Me queda más facil entenderlo así, que con una lista de vagones.
vagon1 = Vagon(10)
vagon2 = Vagon(20)
vagon3 = Vagon(30)

# Enganchamos los vagones
vagon1.siguiente = vagon2
vagon2.siguiente = vagon3

# Ejecutamos la función iniciando desde el primer vagón
imprimir_tren_inverso(vagon1)