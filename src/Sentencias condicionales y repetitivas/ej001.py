
#Actividad 1: Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, (mas adelante veremos como detectar los fallos usando try y except)

#Introduzca un número: 4
#Introduzca un número: 5
#Introduzca un número: dato erróneo
#Entrada inválida
#Introduzca un número: 7
#Introduzca un número: fin
#16 3 5.33333333333


def comprobar_numero(entrada: str):
    if entrada.startswith("."):
        entrada = entrada [1:]

    return entrada.isdigit()


def main(): 
    cont = 0
    suma = 0 
    media = 0

    encuentra_fin = False
    while not salir:
       entrada = input("Introduce un numero").strip
    if entrada_correcta (entrada)
         numero = int(entrada)
         cont += 1
         suma += numero
    elif entrada.lower() == "fin"
     encuentra_fin = True
    else:
        print("Entrada valida")
if cont > 0:
   media = suma/





if __name__ == "__main__":
    print()
