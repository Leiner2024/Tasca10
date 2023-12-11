def binario_a_entero(binario):
    if all(digito in '01' for digito in binario):
        return int(binario, 2)
    else:
        return "No es un número binario válido."

# Solicitamos al usuario que ingrese un número binario
binario_input = input("Escribe un número binario: ")

# Mostramos el resultado
print("El número binario {} en decimal es: {}".format(binario_input, binario_a_entero(binario_input)))