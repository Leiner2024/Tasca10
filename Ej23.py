# Definimos una función llamada 'menu' para mostrar un menú y obtener la opción del usuario.
def menu():
    print("""
    Menú:
        1. Dibujar uno
        2. Dibujar dos
        0. Salir
    """)
    opcion = input("Seleccione el dibujo que desee: ")
    return opcion

# Definimos una función llamada 'crear_puntos' para imprimir diferentes dibujos según la opción seleccionada.
def crear_puntos(opcion):
    match opcion:
        case "1":
            print("""  .  
             . .
             .   .
             . .
             .   
            """)
        case "2":
            print(""" __
            | | |
             _ _
            | | |
             _ _
            """)
        case _:
            print("Adiós")

# En el programa principal:
# Inicializamos la opción con un valor diferente de "0" para entrar en el bucle.
opcion = "2"
while opcion != "0":
    # Llamamos a la función 'menu' para obtener la opción del usuario.
    opcion = menu()
    # Llamamos a la función 'crear_puntos' para imprimir el dibujo correspondiente a la opción.
    crear_puntos(opcion)

print("Adiós, ya hemos terminado")
