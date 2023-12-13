# Definir una función llamada 'taula_multiplicar' que imprime la tabla de multiplicar de un número dado
def taula_multiplicar(a):
    # Bucle que itera desde 0 hasta 19
    for i in range(20):
        # Mostrar el resultado de la multiplicación
            print("{} x {} = {}".format(i+1, a, (i+1)*a))

# Función principal
# Solicitar al usuario que introduzca un número para calcular su tabla de multiplicar
x = int(input("Introduce un número para calcular su tabla de multiplicar: "))

# Llama a la función 'taula_multiplicar' con el número ingresado
taula_multiplicar(x)