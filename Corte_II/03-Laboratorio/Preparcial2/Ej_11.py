#Ejercicio 11 · Mapas y conjuntos  ·  Python  ·  (caso práctico) 
#A partir de los registros de recolección, escriba el código que acumule los kilos por material, determine el material con 
#mayor total y liste los materiales distintos. Indique qué imprime y explique por qué para una de las dos tareas 
#conviene un dict y para la otra un set. 

registros = [("vidrio", 12), ("papel", 8), ("vidrio", 5), ("plastico", 20),
             ("papel", 14), ("metal", 3), ("plastico", 7), ("vidrio", 9)]

# Acumular kilos por material (usando un diccionario)
totales = {}
for material, kilos in registros:
    totales[material] = totales.get(material, 0) + kilos

# Determinar el material con mayor total
mayor_material = max(totales, key=totales.get)

# Listar los materiales distintos (usando un set)
materiales_distintos = set(totales.keys())

print("Totales por material:", totales)
print("Material con mayor total:", mayor_material, "con", totales[mayor_material], "kilos")
print("Materiales distintos:", materiales_distintos)