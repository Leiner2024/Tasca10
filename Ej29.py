def calcular_edad(anyo_actual, anyo_nacimiento):
    return anyo_actual - anyo_nacimiento

def imprimir_datos(personas):
    print("Nombre\t\tFecha de nacimiento\tEdad que cumplirá este año")
    for persona in personas:
        print(f"{persona['Nombre']}\t\t{persona['Anyo_Nacimiento']}\t\t{persona['Edad']}")

# Para que pongas el año, actual o el que quieras
anyo_actual = int(input("Ingresa el año actual: "))

# Definir los datos de las personas, esto lo puedes cambiar si quieres Joan.
personas = [
    {"Nombre": "Tinelli", "Anyo_Nacimiento": 1960},
    {"Nombre": "Dibu", "Anyo_Nacimiento": 1992},
    {"Nombre": "Messi", "Anyo_Nacimiento": 1987}
]

# Calcular la edad para cada persona
for persona in personas:
    persona["Edad"] = calcular_edad(anyo_actual, persona["Anyo_Nacimiento"])

# Imprimir los datos tabulados
imprimir_datos(personas)