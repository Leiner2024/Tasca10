# Definimos una función llamada 'es_palindrom' para verificar si una palabra es un palíndromo.
def es_palindrom(palabra):
    # Convertimos todos los caracteres a minúsculas para considerar mayúsculas y minúsculas como equivalentes.
    palabra = palabra.lower()
    return palabra == palabra[::-1]

# Ejemplos de uso.
print(es_palindrom("radar"))   
print(es_palindrom("air"))     
print(es_palindrom("civic"))  
print(es_palindrom("moix"))  
print(es_palindrom("tapat"))   
print(es_palindrom("casa"))   
print(es_palindrom("refer"))
