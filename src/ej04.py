# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solicitar al usuario la temperatura en Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Imprimir el resultado
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F")
