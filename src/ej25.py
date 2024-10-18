# Función para pedir y procesar la fecha de nacimiento
def obtener_fecha_nacimiento():
    fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    
    # Asegurarse de que la fecha tenga la estructura correcta
    try:
        dia, mes, anio = fecha.split('/')
        # Completar con ceros a la izquierda si es necesario
        dia = dia.zfill(2)
        mes = mes.zfill(2)

        # Validar que la fecha tenga el formato correcto
        if len(dia) > 2 or len(mes) > 2 or len(anio) != 4:
            raise ValueError("Formato de fecha incorrecto")

        print(f"Día: {dia}")
        print(f"Mes: {mes}")
        print(f"Año: {anio}")

    except ValueError as e:
        print(f"Error: {e}. Asegúrate de introducir la fecha en el formato dd/mm/aaaa.")

# Llamar a la función
obtener_fecha_nacimiento()


