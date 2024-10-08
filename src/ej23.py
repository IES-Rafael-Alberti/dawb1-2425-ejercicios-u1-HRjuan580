# Pedir el correo electrónico al usuario
correo_original = input("Introduce tu correo electrónico: ")

# Separar el nombre del dominio
nombre, dominio = correo_original.split('@')

# Crear el nuevo correo con el dominio ceu.es
nuevo_correo = f"{nombre}@ceu.es"

# Mostrar el nuevo correo electrónico
print("Tu nuevo correo electrónico es:", nuevo_correo)

