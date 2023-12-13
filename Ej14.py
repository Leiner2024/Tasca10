# Definimos una función llamada 'gran' para encontrar el número más grande entre tres valores
def gran(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

# En el uso de la función:
# Solicitamos al usuario que introduzca tres números para comparar
x = int(input("Introduce el primer número a comparar: "))
y = int(input("Introduce el segundo número a comparar: "))
z = int(input("Introduce el tercer número a comparar: "))

# Llamamos a la función 'gran' para encontrar el número más grande
c = gran(x, y, z)

# Hacmos que muestre el resultado
print("El número más grande es: {}".format(c))
