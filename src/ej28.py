def main(): 

    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese un segundo numero entero: "))

    if num1 == num2:
        print("Los numeros no pueden ser iguales. ")
    else:
        menor = min(num1, num2)
        mayor = max(num1, num2)

        cantidad = mayor - menor -1

        print(f"El numero menor es el {menor} y entre ellos existen {cantidad} numeros enteros. ")


if __name__ == "__main__":
    main()

