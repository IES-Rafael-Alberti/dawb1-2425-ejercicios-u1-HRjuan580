def calcular_importe_total(horas, coste_por_hora):
    #Calcula el importe total del servicio.
    return horas * coste_por_hora

def main():
    try:
        # Solicitar horas de trabajo
        horas = float(input("Introduce las horas de trabajo: "))
        # Solicitar precio por hora
        coste_por_hora = float(input("Introduce el precio por hora: "))
        
        # Calcular el importe total
        total = calcular_importe_total(horas, coste_por_hora)
        
        # Mostrar el resultado
        print(f"El importe total del servicio es: {total:.2f}")
    
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()

    




