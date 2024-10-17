
def main():
    
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    
    if num1 == num2:
        print("Los números no pueden ser iguales.")
    else:
        
        menor = min(num1, num2)
        mayor = max(num1, num2)

        
        cantidad = mayor - menor - 1

        
        print(f"El número menor es el {menor} y entre ellos existen {cantidad} números enteros.")


if __name__ == "__main__":
    main()
