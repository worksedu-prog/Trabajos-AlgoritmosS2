#De centro a vereda

from collections import deque

NOMBRES = ["CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE",
           "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"]
ARISTAS = [(0, 1), (1, 4), (0, 2), (0, 3), (1, 5),
           (2, 7), (3, 6), (5, 6), (4, 7), (7, 8), (5, 8), (2, 6), (6, 8), (1, 8), (5, 7), (5, 2)]
N = 9

# Construcción de la lista de adyacencia
lista = [[] for a in range(N)]
for a, b in ARISTAS:
    lista[a].append(b)
    lista[b].append(a)

def bfs(inicio, destino):
    visitado = [False] * N
    cola = deque([inicio])
    visitado[inicio] = True
    orden = []
    
    # Vector para reconstruir el camino exacto
    padre = [-1] * N

    while cola:
        u = cola.popleft()  # Saca el elemento del frente de la cola (FIFO)
        orden.append(u)

        
        if u == destino:
            pass

        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                padre[v] = u
                cola.append(v)
                
    return orden, padre

# BFS desde CENTRO (0) buscando llegar a VEREDA (8)
inicio_idx = 0  # CENTRO
destino_idx = 8 # VEREDA

orden_bfs, padre = bfs(inicio_idx, destino_idx)

print("Recorrido BFS desde CENTRO a VEREDA:")
print("Índices:", orden_bfs)
print("Nombres:", [NOMBRES[i] for i in orden_bfs])

# Reconstruir el camino más corto desde CENTRO hasta VEREDA
camino = []
actual = destino_idx
while actual != -1:
    camino.append(NOMBRES[actual])
    actual = padre[actual]
camino.reverse()

print("\nCamino más corto:")
print(" -> ".join(camino))