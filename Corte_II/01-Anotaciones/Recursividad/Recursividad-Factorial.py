nivel = 0

def factorial(n):
    global nivel
    print("|  " * nivel + f"factorial({n}) entra")
    nivel += 1
    r = 1 if n <= 1 else n * factorial(n - 1)
    nivel -= 1
    print("|  " * nivel + f"factorial({n}) devuelve {r}")
    return r


print("--- traza de la pila de llamadas ---")
prueba_de_factorial = 15
r = factorial(prueba_de_factorial)
print(f"Resultado: {r}")
#Factorial de 5 : Tiempo de ejecución 0.124
#Factorial de 10 : Tiempo de ejecución 0.072
#Factorial de 15 : Tiempo de ejecución 0.082