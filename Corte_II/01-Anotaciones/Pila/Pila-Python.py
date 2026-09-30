## Pilas:(stack) LIFO last in first out el ultimo en entrar es el primero en salir
## solo se accede al tope de la pila, no se puede acceder a los elementos intermedios
## operaciones: push(x): colocar x al tope, 
# pop(): eliminar el elemento del tope precondicion la pila no este vacia, 
# peek(): ver el elemento del tope precondicion la pila no este vacia,
# is_empty: verificar si la pila está vacía, 
# size: obtener el tamaño de la pila, 
# top(): obtener el elemento del tope
# tres 3 operaciones apilar desapilar y ver el tope(cima) sin sacarla 
# O(1) tiempo constante
class Pila:
    def __init__(self):self.items = []
    def apilar(self,x):self.items.append(x)
    def desapilar(self):
        if self.vacia():return None
        return self.items.pop()
    def cima(self):return None if self.vacia() else self.items[-1]
    def vacia(self):return len(self.items) == 0
    # apilar sobre un array apilo al final O(1) sobre una 
    # lista enlazada apilo al inicio O(1) 
    # desapilar sobre un array desapilo al final O(1) 
    # sobre una lista enlazada desapilo al inicio O(1)
    

#1. (a[b]c) y (a[b)c] 

#Rta: El segundo esta mal dedido a la organización de los parentesis, este problema se arreglaria con una pila

def balanceados(s):
    p = Pila()
    pares = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            p.apilar(c)
        elif c in ')]}':
            if p.vacia() or p.desapilar() != pares[c]:
                return False
    return p.vacia()

# Pruebas organizadas en una lista
print("\nPrimera lista de casos")
casos = [
    "()",
    "([]{})",
    "([)]",
    "((())",
    "{}[]()"
]

# Imprimir cada caso junto a su resultado
for cadena in casos:
    print(f"{cadena:<10} valor de verdad: {balanceados(cadena)}")
    
#-------------------------------------------------------------------------------------------

#([]{})
#([)]
#((()
#{}[]()

print("\nSegunda lista de casos")
casos_2 = [
    "([]{})",
    "([)]",
    "((()",
    "{}[]()"
]

#Imprimir cada segundo caso junto a su resultado
for cadena_2 in casos_2:
    print(f"{cadena_2:<10} valor de verdad: {balanceados(cadena_2)}")

#----------------------------------------------------------------------------------------------

def balanceados_sin_vacia(s):
    p = Pila()
    pares = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            p.apilar(c)
        elif c in ')]}':
            if p.vacia() or p.desapilar() != pares[c]:
                return False
    return True

print("\nTercera lista de casos sin vacia en la función de balanceados")

casos_3 = [
    "([]{})",
    "([)]",
    "((()",
    "{}[]()"
]

#Imprimir cada segundo caso junto a su resultado
for cadena_3 in casos_3:
    print(f"{cadena_3:<10} valor de verdad: {balanceados_sin_vacia(cadena_3)}")