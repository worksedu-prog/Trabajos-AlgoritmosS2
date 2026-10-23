#Ejercicio 5 · Trazado de Insertion Sort  ·  Python  ·  (trazado) 
#Muestre el contenido del arreglo después de cada pasada del ciclo externo y cuente el total de comparaciones que 
#realiza el ciclo interno. 

v = [42, 17, 93, 8, 55, 31] 
for i in range(1, len(v)): 
    actual = v[i] 
    j = i - 1 
    while j >= 0 and v[j] > actual: 
        v[j + 1] = v[j] 
        j -= 1 
    v[j + 1] = actual 

#Hace un total de 11 iteraciones para poder ordenar esa lista 
#Empieza por v[1] osea 17 - RECORDARRR 