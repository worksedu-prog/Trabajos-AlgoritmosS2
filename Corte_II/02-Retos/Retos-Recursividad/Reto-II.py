#Potencia de a elevado a la b, recursiva. 
# Y después de que funcione, mejórenla: si b es par, a elevado a la b es igual a a elevado a la b dividido entre 2, al cuadrado. 
# Con eso pasan de n llamadas a log n llamadas. Compárenlo midiendo.

def potencia(a, b):
    if b == 0: #Caso base donde b = 0
        return 1
    elif b % 2 == 0: #Caso donde b es par
        return potencia(a, b // 2) ** 2 #Propiedad de exponente par: a^b = (a^{b/2})^2
    else: #Caso donde b es impar
        return a * potencia(a, b - 1) #Propiedad de exponente impar: a^b = a * a^{b-1}), el exponente b va bajando de 1 en 1

a = int(input("Ingrese la base: "))
b = int(input("Ingrese el exponente: "))

resultado = potencia(a, b)
print(f"{a} elevado a la {b} es: {resultado}")