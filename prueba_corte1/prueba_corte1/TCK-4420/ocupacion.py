# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    for j in range(len(m[0])):
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales


def dia_mas_flojo(m): #Se crea una función donde cuenta los puntos inactivos
    """Devuelve el indice del dia con MENOR recoleccion total. 
       PENDIENTE: implementar."""
    totales_dias = total_por_dia(m)
    min_valor = totales_dias[0]
    min_indice = 0
    for j in range(1, len(totales_dias)):
        if totales_dias[j] < min_valor:
            min_valor = totales_dias[j]
            min_indice = j
    return min_indice


def puntos_inactivos(m): #Se crea la difinicion de “dia más flojo” devolviendo el índice menor 
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
       PENDIENTE: implementar."""
    contador = 0
    for fila in m:
        for v in fila:
            if v == 0:
                contador += 1
    return contador