def superposición(lista1, lista2):
    return bool(set(lista1) & set(lista2))
#Pp
lista_x = [6, 7, 8, 9]
lista_z = [777, 69, 6, 50]

respuesta = superposición(lista_x, lista_z)

print(respuesta)