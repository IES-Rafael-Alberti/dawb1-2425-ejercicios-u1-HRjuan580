# Definimos el peso de los productos
peso_payaso = 112  # en gramos
peso_muneca = 75   # en gramos

# Solicitar el número de payasos y muñecas
num_payasos = int(input("Introduce el número de payasos vendidos: "))
num_munecas = int(input("Introduce el número de muñecas vendidas: "))

# Calcular el peso total
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

# Mostrar el resultado
print(f"El peso total del paquete a enviar es: {peso_total} gramos.")
