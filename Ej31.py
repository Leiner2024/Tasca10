# Definición de la función nums_que_comencen_per
def nums_que_comencen_per(lista_nombres):
    # Iniciamos el contador
    contador = 0
    
    # Iteramos sobre cada nombre en la lista
    for nombre in lista_nombres:
        # Convertimos el nombre a minúsculas para hacer la comparación sin importar el caso
        nombre_minuscula = nombre.lower()

        # Verificamos si el nombre comienza con 'a'
        if nombre_minuscula.startswith('a'):
            contador += 1

    # Devolvemos el resultado final
    return contador

# Ejemplo de uso de la función
nombres = ["Ana", "Pedro", "Alberto", "Alicia", "Carlos", "Marta"]

# Llamamos a la función y almacenamos el resultado en cantidad_nombres_con_a
cantidad_nombres_con_a = nums_que_comencen_per(nombres)

# Imprimimos el resultado
print(f"En la lista hay {cantidad_nombres_con_a} nombres que comienzan con la letra 'A' o 'a'.")
