#Agréguenle a Bubble una bandera que detecte si en una pasada completa no hubo ningún intercambio, y en ese caso corte. 
# Después midan cuántas comparaciones hace sobre datos ordenados. Van a ver que baja de veintiocho a siete

def bubble_sort_comparaciones_e_intercambios(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            comparaciones += 1  # Se realiza la comparación
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1  # Se realiza el intercambio
                intercambio = True
        if not intercambio:
            break
            
    return arr, comparaciones, intercambios


#Pruebas

datos_prueba1 = [11,34,556,98,10]
datos1, comparaciones1, intercambios1 = bubble_sort_comparaciones_e_intercambios(datos_prueba1)
print(f"\nArreglo ordenado por bubble_sort: {datos1}")
print(f"Cantidad de comparaciones realizadas: {comparaciones1}")
print(f"Cantidad de intercambios: {intercambios1}")

datos_prueba2 = [1,2,3,4,5,6,7,8,9,10]
datos2, comparaciones2, intercambios2 = bubble_sort_comparaciones_e_intercambios(datos_prueba2)
print(f"\nArreglo ordenado por bubble_sort: {datos2}")
print(f"Cantidad de comparaciones realizadas: {comparaciones2}")
print(f"Cantidad de intercambios: {intercambios2}")