capital = float(input("Introcuce la cantidad de dinero despositada: "))
interes = 4/100
capital_anio_1 = capital + (capital+ interes / 100)
capital_anio_2 = capital_anio_1 * (1 + interes)
capital_anio_3 = capital_anio_2 * (1 + interes)

print("Ahorros primer año")