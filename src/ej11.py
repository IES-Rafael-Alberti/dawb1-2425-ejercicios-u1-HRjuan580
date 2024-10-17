# Leer un entero positivo del usuario
n = int(input("Introduce un entero positivo: "))

# Validar que n sea positivo
if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Calcular la suma usando la fórmula
    suma = n * (n + 1) // 2
    print(f"La suma de los primeros {n} enteros es: {suma}")
