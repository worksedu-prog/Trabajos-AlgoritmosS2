
# PARTE B: Búsque de comparaciones con contadores


def busqueda_binaria(v, x):
    comparaciones = 0
    izq, der = 0, len(v) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        comparaciones += 1  # Se realiza una comparación
        
        if v[medio] == x: 
            return medio, comparaciones
        elif v[medio] < x: 
            izq = medio + 1
        else: 
            der = medio - 1
            
    return -1, comparaciones


def busqueda_secuencial(v, x):
    comparaciones = 0
    for i in range(len(v)):
        comparaciones += 1  # Se realiza una comparación
        if v[i] == x:
            return i, comparaciones
            
    return -1, comparaciones



# Casos de pruebas

# La colección DEBE estar ordenada para la búsqueda binaria
vector = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Definición de los 4 casos de prueba requeridos
casos = {
    "Primer elemento": vector[0],                 # 10
    "Elemento del medio": vector[len(vector)//2], # 50
    "Último elemento": vector[-1],                # 90
    "Elemento inexistente": 999                   # No existe
}

print(f"Colección de registros ({len(vector)} elementos): {vector}\n")


# Ejecución y creación de la tabla

resultados = []

for nombre_caso, valor_buscado in casos.items():
    posicion_secuencial, comp_sec = busqueda_secuencial(vector, valor_buscado)
    possicion_binaria, comp_bin = busqueda_binaria(vector, valor_buscado)
    
    resultados.append({
        "Caso": nombre_caso,
        "Valor": valor_buscado,
        "Comparaciones en Secuencial": comp_sec,
        "Comparaciones en Binaria": comp_bin
    })

# Imprimir Tabla Comparativa
print(f"{'Caso de Prueba':<22} | {'Valor':<6} | {'Comparaciones en Secuencial':<16} | {'Comparaciones en Binaria':<13}")
print("-" * 65)

for r in resultados:
    print(f"{r['Caso']:<22} | {r['Valor']:<6} | {r['Comparaciones en Secuencial']:<16} | {r['Comparaciones en Binaria']:<13}")