# Comenzamos con la suma en 0
suma = 0

# Le pedimos al usuario que introduzca un número y mostramos la cantidad de dígitos en el número.
a = input("Introduce un número: ")
print("{} tiene {} dígitos".format(a, len(a)))

# Recorremos cada dígito y su índice en el número.
for i, e in enumerate(a):
    # Verificamos si el índice es par y mostramos el dígito correspondiente.
    if i % 2 == 0:
        print("El dígito en la posición par {} es {}".format(i, e))