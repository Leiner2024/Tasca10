# Definimos una función para leer una lista de elementos hasta que se ingrese un punto (.)
def llegir_llista():
    # Inicializamos una lista vacía y un carácter 'c' con un valor arbitrario "a"
    a = []
    c = "a"
    
    # Mientras 'c' no sea ".", solicitamos al usuario que ingrese elementos a la lista
    while c != ".":
        c = input("Introduce un elemento de la lista y punto (.) para terminar: ")
        # Si 'c' no es ".", agregamos el elemento a la lista.
        if c != ".":
            a.append(c)
    return a

# Definimos una función para eliminar los extremos de una lista si tiene al menos tres elementos
def eliminar_capicua(a):
    b = []
    # Verificamos si la lista tiene más de dos elementos
    if len(a) > 2:
        # Creamos una nueva lista 'b' que contiene los elementos desde el segundo hasta el penúltimo
        b = a[1:-1]
    return b

# En la parte principal del programa:
# Llamamos a la función para leer una lista.
x = llegir_llista()

# Llamamos a la función para eliminar los extremos de la lista
y = eliminar_capicua(x)

# Mostramos el resultado e forma de texto
print("La lista original {} se ha transformado en la lista {}".format(x, y))