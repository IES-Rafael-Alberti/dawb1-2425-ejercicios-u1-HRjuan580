def convertir_temperatura():
    # Pedir al usuario que introduzca la temperatura en Celsius
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    
    # Convertir Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Formatear la cadena de salida
    resultado = f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)"
    
    return resultado

# Llamar a la función y mostrar el resultado
print(convertir_temperatura())
