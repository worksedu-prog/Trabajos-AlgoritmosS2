#Busqueda Recursiva
#PREFERENCIALMENTE NO USARLA
#@Julian_H

def busqueda_recursiva(lista, objetivo, indice=0):
    if indice >= len(lista):
        return False
    elif lista[indice] == objetivo:
        return True
    else:
        return busqueda_recursiva(lista, objetivo, indice + 1)

lista_prueba = [1,2,3,4,5,6,7,8,9,10]
objetivo_prueba = 8
resultado_busqueda =  busqueda_recursiva(lista_prueba, objetivo_prueba, indice=0)
print(f"El resultado de la busqueda es: {resultado_busqueda}")