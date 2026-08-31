# 1. Pedir al usuario cuántos puntos de acopio nuevos se van a registrar
espacio = int(input("¿Cuantos puntos de acopio nuevos se van a registrar? "))

# 2. Crear una lista vacía. 
# En Python no existe 'new' ni 'delete[]'; el lenguaje solicita la memoria 
# al sistema operativo de forma automática cuando agregamos elementos.
arreglo = []

# 3. Llenar la lista con los pesos de la jornada especial
for i in range(espacio):
    peso = float(input(f"Ingrese el peso de la jornada especial para el punto {i + 1}: "))
    arreglo.append(peso) # .append() añade el elemento y agranda la lista dinámicamente

# 4. Calcular el promedio sumando los valores y dividiendo entre la cantidad
# Usamos un 'if' inline por seguridad para evitar una división por cero si 'espacio' es 0
promedio = sum(arreglo) / espacio if espacio > 0 else 0
print(f"El promedio de recoleccion es: {promedio} kg")

# Nota: No necesitas usar 'delete' ni 'nullptr' porque el recolector de basura 
# de Python (garbage collector) borra la lista de la memoria automáticamente 
# cuando el programa termina o la variable deja de usarse.
