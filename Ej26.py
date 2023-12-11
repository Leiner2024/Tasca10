def leer_lista():
    resultado_lista = []
    a = '1'
    while a != ".":
        a = input("Introduce el siguiente parametro: ")
        if a != ".":
            resultado_lista.append(a)
        else:
            return resultado_lista

# Escoger la palabra con más caracteres
def palabra_más_larga(lista, p):
    max = lista[0]
    for x in lista:
        if len(x) > len(max):
            max = x
    return max

# Programa principal
l = leer_lista()
s = int(input("Introduce el tamaño que quieres filtrar: "))  
o = palabra_más_larga(l, s)

print("Lista ingresada:", l)
print("Palabras con {} caracteres:".format(s), o)