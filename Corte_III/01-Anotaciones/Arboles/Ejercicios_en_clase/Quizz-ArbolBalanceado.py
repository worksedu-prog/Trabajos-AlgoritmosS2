#Quizz 30/10

#Reto: Rotacion Manual
#Escriba un pequeño programa que lea por teclado tres claves en el orden en que se insertarían, construya el árbol SIN balancear, diagnostique cuál de los cuatro casos es (o si está equilibrado) y aplique la rotación correcta. Debe imprimir el árbol antes y después.
#Pista: El diagnóstico sale de dos números: el fe del nodo y el fe de su hijo del lado pesado. No necesita más.
#Resultado esperado: Con 30, 10, 20 debe diagnosticar LR. Con 10, 20, 30 debe diagnosticar RR. Con 10, 30, 20 debe diagnosticar RL.


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
        self.altura = 0

def altura(nodo):
    if nodo is None:
        return -1          # arbol vacio: -1 (un solo nodo: 0)
    return nodo.altura

def recalc(nodo):
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))

def rotarIzquierda(x):
    y = x.der
    B = y.izq
    y.izq = x
    x.der = B
    recalc(x)
    recalc(y)
    return y

def rotarDerecha(y):
    x = y.izq
    B = x.der
    x.der = y
    y.izq = B
    recalc(y)
    recalc(x)
    return x

# Inserción SIN balancear
def insertar(nodo, dato):
    if nodo is None:
        return Nodo(dato)
    if dato < nodo.dato:
        nodo.izq = insertar(nodo.izq, dato)
    elif dato > nodo.dato:
        nodo.der = insertar(nodo.der, dato)
    recalc(nodo)
    return nodo

# El diagnosticoq ue analiza los casos
def diagnostico(nodo):
    if nodo is None:
        return "Equilibrado"

    fe = altura(nodo.izq) - altura(nodo.der)

    if fe == 2:
        fe_hijo = altura(nodo.izq.izq) - altura(nodo.izq.der)
        return "LL" if fe_hijo >= 0 else "LR"
    elif fe == -2:
        fe_hijo = altura(nodo.der.izq) - altura(nodo.der.der)
        return "RR" if fe_hijo <= 0 else "RL"
    return "Equilibrado"

# Rotación
def rotar(nodo, caso):
    if caso == "LL":
        return rotarDerecha(nodo)
    if caso == "LR":
        nodo.izq = rotarIzquierda(nodo.izq)
        return rotarDerecha(nodo)
    if caso == "RR":
        return rotarIzquierda(nodo)
    if caso == "RL":
        nodo.der = rotarDerecha(nodo.der)
        return rotarIzquierda(nodo)
    return nodo   # equilibrado: no se hace nada

# Función de imprimir
def mostrar(nodo, nivel=0):
    if nodo is None:
        return
    mostrar(nodo.der, nivel + 1)
    print("    " * nivel + str(nodo.dato))
    mostrar(nodo.izq, nivel + 1)





raiz = None
for i in range(3):
    clave = int(input(f"Clave {i + 1}: "))
    raiz = insertar(raiz, clave)

print("\nÁrbol de antes:")
mostrar(raiz)

caso = diagnostico(raiz)
print("\nDiagnóstico:", caso)

raiz = rotar(raiz, caso)

print("\nÁrbol después:")
mostrar(raiz)