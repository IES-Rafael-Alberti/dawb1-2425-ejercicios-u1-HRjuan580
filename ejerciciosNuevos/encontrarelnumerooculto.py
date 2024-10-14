#encontrar el numero ocuto

import random

def adivina_el_numero():
    numero_oculto = random.randint(1, 100)  # Genera un número entre 1 y 100
    intentos = 15
    adivinado = False

    print("¡Bienvenido al juego de Adivina el Número!")
    print("He seleccionado un número entre 1 y 100.")
    print(f"Tienes {intentos} intentos para adivinarlo.")

    while intentos > 0 and not adivinado:
        try:
            suposicion = int(input("Introduce tu suposición: "))

            if suposicion < 1 or suposicion > 100:
                print("Por favor, introduce un número entre 1 y 100.")
                continue  # Volver a pedir entrada

            intentos -= 1

            if suposicion == numero_oculto:
                adivinado = True
                print("¡Felicidades! Eres un mago .")
            elif suposicion < numero_oculto:
                print(f"Congelado. Te quedan {intentos} intentos.")
            else:
                print(f"Ardiendo. Te quedan {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    if not adivinado:
        print(f"Lo siento, no has adivinado el número. Era: {numero_oculto}")

if __name__ == "__main__":
    adivina_el_numero()