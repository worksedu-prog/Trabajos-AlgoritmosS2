#Ejercicio 10 · Escritura de código  ·  Python  ·  (implementación con pila) 
#Escriba la función balanceada(s) que devuelve True si los paréntesis, corchetes y llaves de la cadena s están 
#correctamente balanceados y anidados, y False en caso contrario. Los demás caracteres se ignoran. Use una pila. 

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def vacia(self):
        return len(self.items) == 0


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


print("\nCasos")

casos = [
    "(a[b]{c})",
    "([)]",
    "((",
    "a)b("
]

for cadena in casos:
    print(f"{cadena:<10} valor de verdad: {balanceados(cadena)}")