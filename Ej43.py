# Empezamos con la suma en 0
suma = 0

# Le pedimos al usuario que introduzca un número y mostramos la cantidad de dígitos en el número
a = input("Introduce un número: ")
print("{} tiene {} dígitos".format(a, len(a)))

# Recorremos cada dígito en el número y sumamos sus valores
for i in a:
    suma = suma + int(i)

# Mostramos la suma de los dígitos.
print("La suma de los dígitos del número {} es {}".format(a, suma))

# Verificamos si la suma de los dígitos es par o impar y luego mostramos el texto que corresponda segúnn el caso
if suma % 2 == 0:
    print("La suma de los dígitos del número {} es par".format(a))
else:
    print("La suma de los dígitos del número {} es impar".format(a))