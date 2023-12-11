def mostrar_majors_que(tupla, limite):
    print(f"Números mayores que {limite}:")
    for numero in tupla:
        if numero > limite:
            print(numero)

# Programa principal
valores = []

# Solicitar al usuario que ingrese valores enteros (ingresar 'fin' para finalizar)
while True:
    entrada = input("Ingresa un valor entero (o escribe 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        valor = int(entrada)
        valores.append(valor)
    except ValueError:
        print("Error: Ingresa un valor entero válido.")

# Llamar a la función para mostrar los números mayores de 18
mostrar_majors_que(valores, 18)