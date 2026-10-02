#Entrada [2,1,2,4,3]
#Salida de forma decreciente [4,2,4,-1,-1]

#Explicación: 
# 1. Comparar el 3 con lo que tiene a la derecha, como no tiene nada no coloca nada en la salida
# 2. Comparar el 4 con lo que tiene a la derecha, como 4 es mayor a 3, coloca 4 en la salida
# 3. Comparar el 2 con lo que tiene a la derecha, como 4 esta en la salida, 2 lo compara con nada y como 2 es mayor a nada coloca a 2 en la salida
# 4. En la salida compara el 4 con lo que la derecha que es el 2, como 4 es mayor a 2 coloca otro 4 en la salida
# 5. Devuelta en la entrada compara el 1 con el otro 4 que aparecio en la salida, como 4 es mayor a 1 coloca un -1 en la salida
# 6. Otra vez en la entrada compara el 2 con el mismo 4 que comparö con el 1, como 4 es mayor a 2 coloca otro -1 en la salida

def pila_monotonica(a):
    n=len(a)
    res=[-1]*n
    pila=[]
    for i in range (n):
        while pila and a[pila[-1]]<a[i]:
            res[pila.pop()]=a[i]
        pila.append(i)
    return res


prueba = [1, 3, 5, 7, 3, 4]
print(pila_monotonica(prueba))