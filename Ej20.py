# Definimos una función llamada 'superposicion' para verificar si hay superposición entre dos listas.
def superposicion(lista1, lista2):
    # Convertimos ambas listas a conjuntos y verificamos si tienen elementos en común
    return bool(set(lista1) & set(lista2))

# En el programa principal:
# Creamos dos listas de ejemplo
lista_x = [6, 7, 8, 9]
lista_z = [777, 69, 6, 50]

# Llamamos a la función 'superposicion' para verificar si hay superposición entre las listas
respuesta = superposicion(lista_x, lista_z)

# Mostramos el resultado
print(respuesta)
