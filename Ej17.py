#Suma de lista 
def sumar_lista(llista):
    suma = 0
    for valor in llista:
        suma += valor
    return suma 
ejemplo_lista = sumar_lista([2, 30, 4, 50])
print(f"Sumar: {ejemplo_lista}")

# Multiplicación lista
def multiplicar_lista(lista):
    producte = 1
    for valor in lista:
        producte *= valor 
    return producte 
ejemplo_lista = multiplicar_lista([2, 30, 4, 50])
print(f"Multiplicación: {ejemplo_lista}")