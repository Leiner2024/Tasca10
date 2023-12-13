# Definimos una función llamada 'crear_puntos' para imprimir puntos en líneas según la lista dada.
def crear_puntos(l):
    for n in l:
        print("." * n)

# En el programa principal:
# Llamamos a la función 'crear_puntos' para imprimir puntos en líneas según la lista [1, 2, 3].
crear_puntos([1, 2, 3])
