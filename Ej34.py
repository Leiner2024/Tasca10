def es_de_traspas(año):
    # Un año es de traspàs si es divisible por 4 y no es divisible por 100, o es divisible por 400.
    return (año % 4 == 0 and año % 100 != 0) or (any % 400 == 0)

# Ejemplo de uso
año = 2024
if es_de_traspas(año):
    print("{} es un año bisiesto.".format(año))
else:
    print("{} no es un año bisiesto.".format(año))