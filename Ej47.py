# Definimos una función para verificar si hay duplicados en una lista.
def hi_ha_duplicats(a):
    # Inicializamos un conjunto 'seen' y una lista 'dupes'.
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]

    # Verificamos si hay duplicados y mostramos el resultado.
    if len(dupes) > 0:
        print("La lista {} tiene elementos duplicados: {}".format(a, dupes))
    else:
        print("La lista {} no tiene elementos duplicados".format(a))

# Definimos una función para leer una lista de elementos hasta que se ingrese un punto (.)
def llegir_llista():
    a = []
    c = "a"
    # Mientras 'c' no sea ".", solicitamos al usuario que ingrese elementos a la lista.
    while c != ".":
        c = input("Introduce un elemento de la lista y punto (.) para terminar: ")
        # Si 'c' no es ".", agregamos el elemento a la lista.
        if c != ".":
            a.append(c)
    return a

# En la parte principal del programa:
# Llamamos a la función para leer una lista.
a = llegir_llista()

# Llamamos a la función para verificar duplicados en la lista.
hi_ha_duplicats(a)
