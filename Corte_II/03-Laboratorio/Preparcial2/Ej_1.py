#Ejercicio 1 · Trazado de recursión  ·  Python  ·  (comprensión + trazado) 
#Dado el siguiente código, determine: (a) qué imprime, (b) cuántos marcos (frames) llega a tener la pila de llamadas en 
#su punto más profundo, y (c) qué ocurre si se elimina la primera condición.

def recoger(n, k):
    if n == 0:
        return 0
    if n % 2 == 0:
        return k + recoger(n - 1, k + 1)
    return recoger(n - 1, k)

print(recoger(5, 1))

#recoger(5, 1) es impar entonces llama a recoger(4, 1)   
# recoger(4, 1) es par entonces ejecuta 1 + recoger(3, 2)   
# recoger(3, 2) es impar entonces llama a recoger(2, 2)   
# recoger(2, 2) es par entonces ejecuta 2 + recoger(1, 3)
# recoger(1, 3) entonces baja a recoger(0, 3)   
# recoger(0, 3) entonces llega al caso base y devuelve 0 
# como llega al 0 vuelve a subir pero agarrando las sumas pendientes por eso:
# Al final  la suma es : 1 + 2 = 3 (denido a los k que se suman)

#Si se elimina la primera condición al no haber caso base n se resta infinitamente por lo tanto concluye en un error

# Su marco más profundo es 6, pues se realizan llamadas recursivas desde n = 5 hasta n = 0 (llegando al caso base)