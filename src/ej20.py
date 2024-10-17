# Preguntar por el número de teléfono
telefono = input("Introduce el número de teléfono (+34-número-extensión): ")

# Verificar que el formato es correcto
if telefono.startswith("+34-") and telefono.count('-') == 2:
    # Separar el número en partes
    partes = telefono.split('-')
    # Obtener el número sin el prefijo y la extensión
    numero_sin_prefijo_y_extension = partes[1]
    
    # Mostrar el resultado
    print(f"Número sin prefijo y extensión: {numero_sin_prefijo_y_extension}")
else:
    print("El formato del número de teléfono no es válido.")
