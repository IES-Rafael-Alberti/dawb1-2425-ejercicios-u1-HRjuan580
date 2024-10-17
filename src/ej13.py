# Solicitar al usuario los dos números enteros
n = int(input("Introduce el primer número entero (n): "))
m = int(input("Introduce el segundo número entero (m): "))

# Comprobar si m es cero para evitar la división por cero
if m == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Calcular el cociente y el resto
    cociente = n // m
    resto = n % m
    # Mostrar el resultado
    print(f"La división de {n} entre {m} da un cociente {cociente} y un resto {resto}.")

