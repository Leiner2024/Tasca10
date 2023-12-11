def es_palindrom(palabra):
    #Convertimos todas los carácteres minúsculas para considerar la mayúscula y minúsculas equivalentes.
    palabra = palabra.lower()
    return palabra == palabra[::-1]

#Ejmplos de uso.
print(es_palindrom("radar"))   
print(es_palindrom("air"))     
print(es_palindrom("civic"))  
print(es_palindrom("moix"))  
print(es_palindrom("tapat"))   
print(es_palindrom("casa"))   
print(es_palindrom("refer")) 