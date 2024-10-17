def main():

    nombre = input("Ingrese un nombre: ")

    if nombre.strip() == "":
        nombre = "Desconocido"


    while True: 
        try:
            edad = int(input("Introduce su edad entre 0-125: "))
            if 0 <= edad <= 125:
                break
            else:
                print("Por favor, ingrese una edad valida entre 0-125. ")
        except ValueError:
            print("Por favor, ingrese un numero entero. ")

    años_restantes = 125 - edad

    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aun {años_restantes} años por cumplir. ")

if __name__ == "__main__": 
    main()