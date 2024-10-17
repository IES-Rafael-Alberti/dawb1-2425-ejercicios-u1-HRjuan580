def convertir_a_binario(valor,base):
    cociente = valor
    resultado =""

    while cociente >= base:
        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base

    resultado += str(cociente)
    resultado = resultado[::-1]

    return resultado

def main():
    valor = int(input("Introduce un numero: "))


if __main__ == " __main__":
    print() 