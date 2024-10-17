def sumar_enteros(n):
    # Calcular la suma utilizando la fórmula
    suma = n * (n + 1) // 2
    
    # Imprimir el resultado
    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")

# Solicitar al usuario un entero positivo
n = int(input("Introduce un entero positivo: "))

# Verificar que n sea positivo
if n > 0:
    # Llamar a la función
    sumar_enteros(n)
else:
    print("Por favor, introduce un número entero positivo.")
