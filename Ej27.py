# Definimos una función llamada contar_mayusculas que toma una cadena como entrada y cuenta las letras mayúsculas.
def contar_mayusculas(cadena):
    # Utilizamos la expresión generadora sum(1 for letra in cadena if letra.isupper()) para contar las letras mayúsculas.
    # Por cada letra en la cadena, generamos 1 si la letra es mayúscula, luego sumamos esos 1s para obtener el recuento total.
    return sum(1 for letra in cadena if letra.isupper())

# Ejemplos de uso

# Primero, con la cadena "Messi"
cadena_ejemplo1 = "Messi"
resultado_ejemplo1 = contar_mayusculas(cadena_ejemplo1)
# Mostramos el resultado en un mensaje.
print(f'En "{cadena_ejemplo1}" hay {resultado_ejemplo1} letras mayúsculas.')

# Luego, con la cadena "StackOverflow"
cadena_ejemplo2 = "StackOverflow"
resultado_ejemplo2 = contar_mayusculas(cadena_ejemplo2)
# Mostramos el resultado en un mensaje.
print(f'En "{cadena_ejemplo2}" hay {resultado_ejemplo2} letras mayúsculas.')


#Manera 1
"""def Mayusculas_Frase(s):
    num_mayor = 0
    num_menor = 0
    for e in s:
        if e.isupper(e):
            num_mayor +=1
        elif e.islower(e):
            num_menor +=1
        else:
            print("La fase {} tiene {} meyor y {} agfsf".format(s, num_mayor, num_menor))"""