# Función para calcular el precio final con IVA
def calcular_precio_final(impuesto, importe_final):
    return importe_final * (1 + impuesto / 10%)

#Tipo de IVA
tipo_iva = 10%

# Pedir importe de un articulo
importe_final = float (input("Introduce el importe final"))

#Solicitar el tipo de iva
tipo_iva = float (input("Introduce el tipo de iva a aplicar(en %): "))

# Calcular el precio final con iva
importe_final = calcular_precio_final(importe_final,tipo_iva)
