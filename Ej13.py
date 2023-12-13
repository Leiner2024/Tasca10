# Definimos una función llamada 'Messi' para imprimir el número mayor entre dos valores
def Messi(a, b):
    if a > b:
        print(a)
    else:
        print(b)

# En el programa principal:
# Le pedimos al usuario que introduzca dos números
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

# Llamamos a la función 'Messi' para imprimir el número mayor
Messi(a, b)
