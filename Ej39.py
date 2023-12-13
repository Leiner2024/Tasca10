#Solicitar al usuario que introduzca un número natural(1,2,3...) (menor que 100) y guardarlo en la variable 'x'
x = int(input("Introduce un número natural (<100): "))

# iniciar la variable 'suma' a 0
suma = 0

# Usar un bucle 'for' para iterar desde 1 hasta 'x' con un paso de -4
for i in range(1, x, -4):
    # Sumar el cuadrado de 'i' al valor acumulado en 'suma'
    suma = suma + (i**2)

# Mostrar el resultado como un mensaje
print("La suma de los cuadrados de las posiciones múltiplos de 4 menores que {} es {} ".format(x, suma))