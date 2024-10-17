
def main():
    
    nombre = input("Ingrese su nombre: ")
    
    
    if nombre.strip() == "":
        nombre = "Desconocido"
    
    
    while True:
        try:
            edad = int(input("Ingrese su edad (0-125): "))
            if 0 <= edad <= 125:
                break  
            else:
                print("Por favor, ingrese una edad válida entre 0 y 125.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    
    años_restantes = 125 - edad

    
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años_restantes} años por cumplir.")


if __name__ == "__main__":
    main()
