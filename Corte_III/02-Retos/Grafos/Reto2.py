#Reto 2 — El converso · Obligatorio Escriba matrizALista(m) y listaAMatriz(l) que conviertan una representación en la otra. 
# #Verifique que convertir ida y vuelta devuelve el original. 
# #Pista: La verificación de ida y vuelta es la prueba más barata y más efectiva que existe para este tipo de funciones. 
# #Escríbala antes que las conversiones. Resultado esperado: listaAMatriz(matrizALista(m)) debe ser igual a m para cualquier m válida.

def matrizALista(m):
    #Convierte una matriz de adyacencia en una lista de adyacencia
    lista = []
    for i in range(len(m)):
        vecinos = []
        for j in range(len(m[i])):
            if m[i][j] == 1:
                vecinos.append(j)
        lista.append(vecinos)
    return lista

def listaAMatriz(l):
    #Convierte una lista de adyacencia en una matriz de adyacencia
    n = len(l)
    matriz = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for vecino in l[i]:
            matriz[i][vecino] = 1
            
    return matriz

def test_conversion():
    #Prueba de ida y vuelta
    m_original = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    
    l = matrizALista(m_original)
    m_final = listaAMatriz(l)
    
    # Si todo sale bien pasará sin errores y mostrará el mensaje
    assert m_final == m_original, "Error! La conversión de ida y vuelta no coincide."
    print("Exito en la prueba")

test_conversion()