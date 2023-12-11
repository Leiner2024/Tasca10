def palabra_más_larga(lista):
    max = lista[0]
    for x in lista:
        if len(x) > len(max):
            max = x
    return max



lista = ["Hola", "Ramis", "IES", "Palabraq"]
m = palabra_más_larga(lista)
print(m)