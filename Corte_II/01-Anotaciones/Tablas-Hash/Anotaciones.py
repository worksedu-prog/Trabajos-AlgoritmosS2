# Busqueda por código REC-00042
# O(n)recorrer la lista
# O(log n)ordenar la lista y busqueda 
# O(1)hashing (conjuntos/mapas)

#Conjunto:
# Guarda elementos sin repeticion y sin orden 
# Mapa: (dicionario) Guarda elementos 
# sin repeticion y con orden (clave:valor)
# funcion hash: recibe un elemento y devuelve un numero entero
# determinista: para un mismo elemento, 
# siempre devuelve el mismo valor
# Rapida: si calula es mas costoso que recorrer.
# esta bien repartida:usa todas las cubetas parejo sin repeticion
# y sin amontonar
a={"papel","lapiz","cuaderno"}
b={"vidrio","madera","plastico","papel"}

print(a.union(b)) #union
print(a.intersection(b)) #interseccion
print(a.difference(b)) #diferencia

print(a | b) #union
print(a & b) #interseccion
print(a - b) #diferencia

mapa={"REC-00042": 42}
print(mapa["REC-00042"])

set1=set()
dict1=dict()

def hash(self,clave):
    h=0
    for c in str(clave):
        h=(h*31+ord(c))%100
    return h


#1. funcion hash para los nombres de los alumnos

#colisiones: cuando dos elementos tienen el mismo valor hash
#encadenamiento: cuando dos elementos tienen el mismo valor hash, 
# se guarda en una lista enlazada
#Direccionaamiento abierto: cuando dos elementos tienen el mismo valor 
# hash, se busca la siguiente cubeta vacia para guardar el elemento,
# todo esto se aloja en un arreglo de cubetas, 
# cada cubeta puede guardar un elemento o una lista enlazada de elementos

# factor de carga: cantidad de elementos en la tabla / cantidad de cubetas
# factorCarga=n(elementos)/m(cubetas)
# lambda=0.5 n o hay colisiones, lambda>0.5 hay colisiones
# lambda=5 cada busquedarecorre 5 claves.
# si lambda>0.75 se recomienda redimensionar la tabla de hash,
# para reducir el factor de carga y 
# mejorar el rendimiento de la tabla de hash. (rehash)
# clave->hash->cubeta->elemento->(si hay colision)
# lista enlazada de elementos y recorre la lista corta de esa cubeta   