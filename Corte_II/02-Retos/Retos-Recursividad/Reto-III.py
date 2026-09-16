#Invertir una cadena de texto recursivamente

def invertir_cadena(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter, se devuelve tal cual
    if len(cadena) <= 1:
        return cadena
    else:
        # Llamada recursiva: se toma el último carácter y se concatena con la inversión del resto de la cadena
        return cadena[-1] + invertir_cadena(cadena[:-1])
        #cadena[-1] Toma la última letra del texto
        #cadena [:-1] Toma el texto sin la última letra

cadena_de_prueba = "Hola"
invertida = invertir_cadena(cadena_de_prueba)
print(f"La cadena original es: {cadena_de_prueba}")
print(f"La cadena invertida es: {invertida}")