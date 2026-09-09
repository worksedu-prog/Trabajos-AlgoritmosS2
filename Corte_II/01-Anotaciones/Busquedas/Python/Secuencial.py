#Busqueda secuencial
def busqueda_secuencial(v,x):
    for i in range(len(v)):
        if v[i] == x:
            return i
    return -1

v = [123,45,576,678,34,23,12,90]
x = 123
print("Busqueda secuencial")
print(f"El vector de busqueda es: {v}" )
print(f"El elemento {x} se encuentra en la posición: {busqueda_secuencial(v, x)}")
print(f"Cantidad de pasos de la busqueda secuencial: {len(v)}")