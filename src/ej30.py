def obtener_valores():
    while True:
        try:
            inicio = int(input("Introduce el número de inicio: "))
            incremento = int(input("Introduce el incremento (debe ser mayor que 0): "))
            total = int(input("Introduce el total (debe ser mayor que 0): "))
            
            if incremento <= 0 or total <= 0:
                print("Error: El incremento y el total deben ser mayores que cero. Inténtalo de nuevo.")
                continue
            
            return inicio, incremento, total
        except ValueError:
            print("Error: Por favor, introduce números válidos.")

def generar_serie(inicio, incremento, total):
    serie = []
    for i in range(inicio, total + 1, incremento):
        serie.append(str(i))
    return serie

def main():
    inicio, incremento, total = obtener_valores()
    serie = generar_serie(inicio, incremento, total)
    print("SERIE => " + "..".join(serie))

if __name__ == "__main__":
    main()
