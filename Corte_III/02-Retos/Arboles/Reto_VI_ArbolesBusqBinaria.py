#Reto 1 — El índice de recursos · Obligatorio Modifique el nodo para que guarde código y nombre. 
# Inserte al menos diez recursos de su línea de proyecto. 
# Implemente listarOrdenado() e informe(codigo) que imprima el nombre o un mensaje de no encontrado, 
# cuántas comparaciones hizo. Pista: La comparación se hace siempre sobre el código, nunca sobre el nombre. 
# Si compara por nombre, la invariante se rompe para las búsquedas por código. Resultado esperado: 
# El listado debe salir ordenado por código sin llamar a ningún sort.

class Nodo:
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.izq = None
        self.der = None

def insertar(nodo, codigo, nombre):
    if nodo is None: return Nodo(codigo, nombre)
    if (codigo < nodo.codigo): nodo.izq = insertar(nodo.izq, codigo, nombre)
    elif (codigo > nodo.codigo): nodo.der = insertar(nodo.der, codigo, nombre)
    return nodo

def listaOrdenada(nodo):
    if nodo is None: return
    listaOrdenada(nodo.izq)
    print(f"Código: {nodo.codigo} - Nombre: {nodo.nombre}")
    listaOrdenada(nodo.der)

def informe(codigo, nodo, comparaciones):
    if nodo is None: 
        print(f"No encontrado. Comparaciones realizadas: {comparaciones}")
        return
    
    comparaciones += 1
    
    if nodo.codigo == codigo:
        print(f"¡Encontrado! Nombre: {nodo.nombre} (Comparaciones: {comparaciones})")
        return
    elif codigo < nodo.codigo:
        return informe(codigo, nodo.izq, comparaciones)
    else:
        return informe(codigo, nodo.der, comparaciones)


raiz = None

recursos = [
    (105, "Guía de Cálculo Diferencial"),
    (102, "Tutoría de Programación C++"),
    (110, "Ejercicios de Estructuras de Datos"),
    (101, "Introducción a Python"),
    (108, "Manual de Git y GitHub"),
    (103, "Taller de Inducción Matemática"),
    (107, "Resolución de Límites y Derivadas"),
    (109, "Práctica de Algoritmos de Búsqueda"),
    (104, "Fundamentos de Bases de Datos"),
    (106, "Apuntes de Lógica Proposicional")
]

for codigo, nombre in recursos:
    raiz = insertar(raiz, codigo, nombre)
    
print("=" * 50)
print(" 1. LISTADO ORDENADO DE RECURSOS (In-Order)")
print("=" * 50)
listaOrdenada(raiz)

print("\n" + "=" * 50)
print(" 2. PRUEBAS DE INFORME (Búsqueda por código)")
print("=" * 50)

print("Buscando el código 107:")
informe(107, raiz, 0)

print("\nBuscando el código 101 (el primero):")
informe(101, raiz, 0)

print("\nBuscando un código que NO existe (999):")
informe(999, raiz, 0)