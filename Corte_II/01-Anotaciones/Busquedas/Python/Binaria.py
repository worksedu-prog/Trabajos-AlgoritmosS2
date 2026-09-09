def binaria(v,x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if v[medio] == x: return medio
        elif v[medio] < x : izq = medio + 1
        else:               der = medio - 1
    return -1

v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 8
print("Busqueda binaria")
print(f"El vector de busqueda es: {v}")
#Cantidad de pasos de busqueda binaria
print(f"Cantidad de pasos para la busqueda binaria: {len(v)}")
print(f"El elemento {x} se encuentra en la posición: {binaria(v, x)}")