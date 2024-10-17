# Pedir al usuario que ingrese los productos
productos_input = input("Introduce los productos de la cesta de la compra, separados por comas: ")

# Separar los productos usando la coma como delimitador
productos = productos_input.split(',')

# Mostrar cada producto en una línea distinta
for producto in productos:
    print(producto.strip())  # Usar strip() para eliminar espacios en blanco
