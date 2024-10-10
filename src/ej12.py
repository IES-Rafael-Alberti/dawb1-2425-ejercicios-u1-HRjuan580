# Solicitar peso y estatura al usuario
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Redondear el IMC a dos decimales
imc_redondeado = round(imc, 2)

# Mostrar el resultado
print(f"Tu índice de masa corporal es: {imc_redondeado}")

