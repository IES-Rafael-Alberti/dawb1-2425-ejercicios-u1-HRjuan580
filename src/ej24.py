# Pedir el precio del producto
precio = input("Introduce el precio del producto en euros (con dos decimales): ")

# Convertir el precio a float
precio_float = float(precio)

# Separar euros y céntimos
euros = int(precio_float)
centimos = int((precio_float - euros) * 100) 

# Mostrar el resultado
print(f"Número de euros: {euros}")
print(f"Número de céntimos: {centimos}")

