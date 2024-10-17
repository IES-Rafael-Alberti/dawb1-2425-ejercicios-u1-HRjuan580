#Calcular area
import math


def calcular_area(a: float, b: float, c: float) -> float: 
    semiper = (a + b + c)/2
    area = math.sqrt(semiper * (semiper - a) * (semiper - b) * (semiper - c))
    return area

def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"): # "-88.67"
        valor = valor[1:] # "88.67"

    pos_punto = valor.startswith("-") # 2
    if pos_punto >= 0:
        valor = valor [:pos_punto] + valor [pos_punto + 1:] # "8867"

    return valor.isdigit()

def introcude_numero(msj: str) -> float: 
    valor = input(msj).strip().replace(",", ".")


    while not comprobar_float(valor):
        print("**ERROR** Numero invalodo! ")
        valor = input(msj).strip().replace(",", ".")

    return float(valor)


def comprobar_triangulo_valido(a, b, c): 
    return (a + b  >  c) and (a + c > b) and (b + c > a)



def main():
    print("Dame los 3 lados del triangulo...")

    lado_a = introcude_numero("Lado 1: ")
    lado_b = introcude_numero("Lado 2: ")
    lado_c = introcude_numero("Lado 3: ")

    if comprobar_triangulo_valido (lado_a, lado_b, lado_c): 
        print(f"\nEl area del triangulo con lados ( {lado_a: .2f}, {lado_b: .2f}, {lado_c: .2f}) es de {calcular_area(lado_a, lado_b, lado_c):.2f}.")
    else:
        print(f"El triangulo con los lados ( {lado_a: .2f}, {lado_b: .2f}, {lado_c: .2f}) no es valido")



if __name__ == "__main__":
    main()