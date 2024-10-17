# Pedir al usuario que ingrese los datos del producto
nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio unitario del producto: "))
unidades = int(input("Introduce el número de unidades: "))

# Calcular el coste total
coste_total = precio_unitario * unidades

# Mostrar la información formateada
print(f"{nombre_producto}: Precio unitario: {precio_unitario:06.2f}, Unidades: {unidades:03d}, Coste total: {coste_total:08.2f}")
