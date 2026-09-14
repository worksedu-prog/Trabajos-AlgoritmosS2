def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

prueba_de_fibonacci = 15
print(f"fibonacci({prueba_de_fibonacci}) =", fibonacci(prueba_de_fibonacci))

#Tiempo de ejecución de fibonacci(5) : 0.082
#Tiempo de ejecución de fibonacci(10) : 0.077
#Tiempo de ejecución de fibonacci(15) : 0.092

