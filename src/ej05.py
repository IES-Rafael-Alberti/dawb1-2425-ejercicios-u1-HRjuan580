# Función para calcular el precio final con IVA
def calcular_precio_final(impuesto, precio_sin_iva):
    return precio_sin_iva * (1 + impuesto / 100)

# Solicitar al usuario el importe sin IVA
precio_sin_iva = float(input("Introduce el importe sin IVA del artículo: "))

# Solicitar el tipo de IVA a aplicar
tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en %): "))

# Calcular el precio final
precio_final = calcular_precio_final(tipo_iva, precio_sin_iva)

# Imprimir el resultado
print(f"El precio final del artículo con IVA es: {precio_final:.2f}€")
