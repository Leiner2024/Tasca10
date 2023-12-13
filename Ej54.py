""" Al prinpio no había entendido lo que pedía pero le pedí que ChatGPT me lo explicara,
    pensaba que era una simple suma pero enrealidad se suma el primer número dado,
    el segundo y los que hay entre estos.
    Ejemplo: 5+10=45 | 5+6+7+8+9+10=45
""" 

# Definimos una función para sumar todos los números entre dos valores dados
def sumar(a, b):
    suma = 0
    
    # Verificamos si 'a' es mayor que 'b'
    if a > b:
        # Iteramos desde 'b' hasta 'a' (inclusive) y sumamos cada número
        for i in range(b, a + 1, 1):
            suma += i
    elif b > a:
        # Iteramos desde 'a' hasta 'b' (inclusive) y sumamos cada número
        for i in range(a, b + 1, 1):
            suma += i
    else:
        # Si 'a' y 'b' son iguales, la suma es cero
        suma = 0
    
    return suma

# En la parte principal del programa:
# Solicitamos al usuario que introduzca dos números
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

# Llamamos a la función para sumar los números entre 'a' y 'b'
c = sumar(a, b)

# Mostramos el resultado
print("La suma de los números entre {} y {} es {}".format(a, b, c))