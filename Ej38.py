# Solicitar al usuario que introduzca la cantidad solicitada (entre 50000 y 800000 euros) y guardarla en la variable 'x'
x = float(input("Introduce la cantidad solicitada (entre 50000 y 800000 euros): "))

# Solicitar al usuario que introduzca el interés (entre 0.5 y 13 por ciento) y guardarlo en la variable 'y'
y = float(input("Introduce el interés (entre 0.5 y 13 por ciento): "))

# Solicitar al usuario que introduzca el número de años y guardarlo en la variable 'z'
z = int(input("Introduce el número de años: "))

# Calcular el capital final usando la fórmula del interés compuesto
cfinal = x * (1 + y/100)**z

# Muestra el resultado en forma de texto(print)
print("El capital {}€ a un interés del {}% a {} años resulta que pagaremos {:.2f}€".format(x, y, z, cfinal))