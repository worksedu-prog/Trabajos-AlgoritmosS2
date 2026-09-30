# PARTE B: Búsqueda con contadores de comparaciones

pruebas = [
    (12324638621, "Julian"), (100372362754, "Isabella"), (14527463725, "Enrique"),
    (67670932176563, "Paulo"), (1021837261873, "Sofia"), (405387126, "Jose"),
    (150183721665, "Lopez"), (145035427168, "Fernando"), (10138726318, "Fernanda")
]


# devuelve el número de cada par, para ordenar por él
def obtener_numero(p):
    return p[0]


# la binaria necesita la lista ordenada, así que ordeno por el número
vector = sorted(pruebas, key=obtener_numero)


def busqueda_binaria(v, x):
    comparaciones = 0
    izq, der = 0, len(v) - 1

    while izq <= der:
        medio = (izq + der) // 2
        comparaciones += 1  # una comparación por vuelta

        if v[medio][0] == x:
            return medio, comparaciones
        elif v[medio][0] < x:
            izq = medio + 1
        else:
            der = medio - 1

    return -1, comparaciones


def busqueda_secuencial(v, x):
    comparaciones = 0
    for i in range(len(v)):
        comparaciones += 1  # una comparación por elemento revisado
        if v[i][0] == x:
            return i, comparaciones

    return -1