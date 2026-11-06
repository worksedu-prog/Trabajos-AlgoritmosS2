NOMBRES = ["CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE",
           "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"]
ARISTAS = [(0, 1), (1, 4), (0, 2), (0, 3), (1, 5),
           (2, 7), (3, 6), (5, 6), (4, 7), (7, 8), (5, 8), (2, 6), (6, 8), (1, 8), (5, 7), (5, 2)]
N = 9
lista = [[] for _ in range(N)]
for a, b in ARISTAS:
    lista[a].append(b)
    lista[b].append(a)

# Version recursiva del recorrido DFS
def dfs_rec(u, visitado, orden):
    visitado[u] = True  # el hilo de Ariadna
    orden.append(u)
    for v in lista[u]:
        if not visitado[v]:
            dfs_rec(v, visitado, orden)

# Version iterativa del recorrido DFS
def dfs_iter(inicio):
    visitado = [False] * N
    pila = [inicio]
    orden = []
    while pila:
        u = pila.pop()                    # LIFO: sale el ultimo que entro
        if visitado[u]:
            continue                      # pudo entrar dos veces a la pila
        visitado[u] = True
        orden.append(u)
        for v in reversed(lista[u]):      # al reves, para igualar al recursivo
            if not visitado[v]:
                pila.append(v)
    return orden



# Versión iterativa desde el nodo 0 ("CENTRO")
resultado_iter = dfs_iter(0)
print("DFS Iterativo (índices):", resultado_iter)
print("DFS Iterativo (nombres):", [NOMBRES[i] for i in resultado_iter])

# Versión recursiva desde el nodo 0 ("CENTRO")
visitado_rec = [False] * N
resultado_rec = []
dfs_rec(0, visitado_rec, resultado_rec)
print("\nDFS Recursivo (índices):", resultado_rec)
print("DFS Recursivo (nombres):", [NOMBRES[i] for i in resultado_rec])