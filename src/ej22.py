# Pedir al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Pedir al usuario que introduzca una vocal
vocal = input("Introduce una vocal: ")

# Comprobar que se ha introducido solo una vocal
if len(vocal) == 1 and vocal.lower() in 'aeiou':
    # Reemplazar la vocal en la frase por su versión en mayúscula
    frase_modificada = frase.replace(vocal, vocal.upper())
    frase_modificada = frase_modificada.replace(vocal.upper(), vocal.upper())  # Para reemplazar si se da la vocal en mayúscula
    print("Frase modificada:", frase_modificada)
else:
    print("Por favor, introduce una sola vocal válida (a, e, i, o, u).")
