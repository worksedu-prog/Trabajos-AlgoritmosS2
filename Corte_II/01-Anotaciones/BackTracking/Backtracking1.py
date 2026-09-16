def resolver(f, c, laberinto, camino):
    FILAS = len(laberinto)
    COLS = len(laberinto[0])

    # 1. ¿Me salí del tablero?
    if f < 0 or f >= FILAS or c < 0 or c >= COLS:
        return False

    # 2. ¿Es muro o ya pasé por aquí?
    if laberinto[f][c] == 1 or camino[f][c] == 1:
        return False

    # 3. Marco esta casilla como parte del camino
    camino[f][c] = 1

    # 4. CASO BASE: Llegué a la salida
    if f == FILAS - 1 and c == COLS - 1:
        return True

    # 5. CASO RECURSIVO: Pruebo las cuatro direcciones (Abajo, Derecha, Arriba, Izquierda)
    if resolver(f + 1, c, laberinto, camino): return True
    if resolver(f, c + 1, laberinto, camino): return True
    if resolver(f - 1, c, laberinto, camino): return True
    if resolver(f, c - 1, laberinto, camino): return True

    # 6. BACKTRACKING: Ninguna sirvió, desmarco y me devuelvo
    camino[f][c] = 0
    return False



#Prueba

laberinto = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

# Matriz del mismo tamaño inicializada en 0s
camino = [[0] * len(laberinto[0]) for i in range(len(laberinto))]

if resolver(0, 0, laberinto, camino):
    print("Ruta encontrada")
    for fila in camino:
        print(fila)
else:
    print("No hay solución")