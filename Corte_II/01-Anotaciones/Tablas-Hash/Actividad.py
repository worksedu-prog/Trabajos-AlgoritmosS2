def calcular_mod11(palabra):
    # Convertir la palabra a mayusculas
    palabra = palabra.upper()
    
    # Letra y su valor (A=1, B=2, ..., Z=26)
    suma = sum(ord(letra) - ord('A') + 1 for letra in palabra if 'A' <= letra <= 'Z')
    
    modulo = suma % 11
    
    return suma, modulo

nombre = input("Ingresar el nombre: ")
total, resultado_mod = calcular_mod11(nombre)

print(f"\nPalabra: {nombre}")
print(f"Suma total: {total}")
print(f"Módulo 11: {resultado_mod}")
