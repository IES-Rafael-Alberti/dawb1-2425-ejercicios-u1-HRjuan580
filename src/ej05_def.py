
def calcular_precio_final(importe_sin_iva, tipo_iva):
# Calcular el precio final aplicando el IVA
    precio_final = importe_sin_iva * (1 + tipo_iva / 100)
    
# Imprimir el precio final
    print(f"El precio final del artículo es: {precio_final:.2f}€")

# Solicitar el importe sin IVA y el tipo de IVA
importe = float(input("Introduce el importe sin IVA del artículo: "))
tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en %): "))

# Llamar a la función
calcular_precio_final(importe, tipo_iva)
