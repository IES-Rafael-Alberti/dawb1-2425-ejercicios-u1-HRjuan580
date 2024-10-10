# Precio habitual de una barra de pan
PRECIO_BARRA = 3.49

# Descuento en porcentaje
DESCUENTO_PORCENTAJE = 0.60

# Solicitar al usuario el número de barras vendidas que no son del día
num_barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))

# Calcular el descuento
descuento = PRECIO_BARRA * DESCUENTO_PORCENTAJE

# Calcular el precio con descuento
precio_con_descuento = PRECIO_BARRA - descuento

# Calcular el coste total
coste_total = precio_con_descuento * num_barras_no_frescas

# Mostrar los resultados
print(f"Precio habitual de una barra de pan: {PRECIO_BARRA}€")
print(f"Descuento por no ser fresca: {descuento:.2f}€")
print(f"Coste total de las barras no frescas: {coste_total:.2f}€")
