def solicitar_nombre():
    nombre = input("Por favor, ingresa tu nombre: ")
    return nombre

def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido."

# Programa principal
if __name__ == "__main__":
    nombre_usuario = solicitar_nombre()
    saludo = saludar(nombre_usuario)
    print(saludo)


