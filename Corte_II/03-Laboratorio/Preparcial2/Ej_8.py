#Ejercicio 8 · Comparación de alternativas  ·  Python  ·  (razonamiento + complejidad) 
#Las dos funciones cuentan cuántos elementos de la lista ya habían aparecido antes. Indique la complejidad de cada 
#una, explique de dónde sale la diferencia y estime cuál será el factor de diferencia con n = 8000.


def dup_lista(datos):
    vistos=[]   #lista
    d = 0
    for x in datos:
        if x in vistos:
            d+=1
        else: vistos.append(x)
    return d


def dup_conjunto(datos):
    vistos = set()  #Conjunto
    d = 0
    for x in datos:
        if x in vistos: d +=1
        else: vistos.add(x)
    return d

#Complejidad en cada función:

#def dup_lista tiene una complejidad de O(n^{2}) siendo cuadratica debido a su composición por parte del for, donde la busqueda de un elemento
#es propocional a las comparaciones
#def dup_conjunto tiene una complejidad de O(n) siendo lineal debido a su composición por parte del for

#Diferencia:
#En dup_lista, vistos es una lista. La operación x in vistos recorre la lista en una busqueda secuencial, en el peor de los tiempos tiene un
#tamaño proporcional a la lista, lo cual acumula un O(n^{2}) 
#En dup_conjunto, vistos es un conjunto. Usando set() como una tabla hash. La operacion x en vistas tiene una complejidad de O(1) por lo tanto su complejidad
#es de O(n)

#En 8000
#La diferencia en dup_conjunto tiene una complejidad de 8000 operaciones
#Por otro lado, dup_lista (8000^{2})/2. La división entre 2 surge porque la lista vistos no está llena desde el principio, 
# sino que comienza vacía y va creciendo elemento por elemento a medida que avanza el bucle
