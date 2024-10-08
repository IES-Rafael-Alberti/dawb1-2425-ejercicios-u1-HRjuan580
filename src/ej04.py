# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solicitar al usuario la temperatura en Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Imprimir el resultado
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F")


def convertir_temperatura():
    # Pedimos al usuario que ingrese la temperatura en Celsius
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    
    # Convertimos a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Retornamos la cadena en el formato requerido
    return f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)"

# Llamamos a la función y mostramos el resultado
resultado = convertir_temperatura()
print(resultado)

