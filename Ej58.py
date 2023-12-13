# Definimos una función para verificar si un número es primo.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# En el programa principal:
# Comenzamos la cuenta de números primos y la lista 'b'
nnumersprimers = 0
b = []

# Iteramos sobre los números del 1 al 100 y verificamos si son primos.
for num in range(1, 101):
    if es_primo(num):
        b.append(num)
        nnumersprimers += 1

# Mostramos el resultado.
print("Hay {} números primos y son {}".format(nnumersprimers, b))