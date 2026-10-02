# ---- Pila monotonica

#temperaturas diarias
#Para cada dia, calculamos cuantos dias hay que esperar hasta que haga más calor. Es el mismo patrón del ejmeplo 1 pero 
#la respuesta es una distancia en lugard e un valor.

#Entrada: [73, 74, 75, 71, 69, 72, 76, 73]
#Salida: [1, 1, 4, 2, 1, 1, 0, 0]

def pila_monotonica(arr):
    n = len(arr)
    res = [0] * n
    pila = []
    
    for i in range(n):
        while pila and arr[pila[-1]] < arr[i]:
            res[pila.pop()] = i - pila[-1]
        pila.append(i)
    
    return res

prueba = [73, 74, 75, 71, 69, 72, 76, 73]
print(pila_monotonica(prueba))