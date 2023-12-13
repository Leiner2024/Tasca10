# Solicitar al usuario que introduzca la primera palabra y guardarla en la variable 'x'
x = input("Introduce la primera palabra: ")

# Solicitar al usuario que introduzca la segunda palabra y guardarla en la variable 'y'
y = input("Introduce la segunda palabra: ")

# Comparar las tres últimas letras de ambas palabras
if x[-3:] == y[-3:]:
    print("Las palabras {} y {} riman en las últimas tres letras: {}".format(x, y, x[-3:]))
# Si no riman en las últimas tres letras, verificar si riman en las dos últimas letras
elif x[-2:] == y[-2:]:
    print("Las palabras {} y {} riman en las últimas dos letras: {}".format(x, y, x[-2:]))
# Si no riman en las últimas dos letras, verificar si riman en la última letra
elif x[-1:] == y[-1:]:
    print("Las palabras {} y {} riman en la última letra: {}".format(x, y, x[-1:]))
# Si no hay coincidencias en ninguna de las anteriores, indicar que las palabras no riman
else:
    print("Las palabras {} y {} no riman".format(x, y))