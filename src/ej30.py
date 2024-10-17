
def main():
    
    inicio = int(input("Ingrese el número de inicio: "))
    

    while True:
        try:
            incremento = int(input("Ingrese el incremento (mayor que 0): "))
            total = int(input("Ingrese el total (mayor que 0): "))
            
            if incremento <= 0 or total <= 0:
                print("Error: tanto el incremento como el total deben ser mayores que cero. Intente de nuevo.")
            else:
                break 
        except ValueError:
            print("Error: por favor, ingrese números enteros válidos.")

    
    serie = []
    for i in range(inicio, total + 1, incremento):
        serie.append(str(i))

    
    resultado = "SERIE => " + "..".join(serie[:-1]) + "-" + serie[-1]
    
    
    print(resultado)


if __name__ == "__main__":
    main()
