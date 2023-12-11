def contar_vocales(palabra):
    # Inicializamos los contadores para cada vocal
    a_count = e_count = i_count = o_count = u_count = 0

    # Iteramos sobre cada letra de la palabra
    for letra in palabra:
        # Convertimos la letra a minúscula para comparar sin importar el caso
        letra = letra.lower()

        # Contamos cada vocal
        if letra == 'a':
            a_count += 1
        elif letra == 'e':
            e_count += 1
        elif letra == 'i':
            i_count += 1
        elif letra == 'o':
            o_count += 1
        elif letra == 'u':
            u_count += 1

    # Devolvemos los resultados en un diccionario
    resultados = {'a': a_count, 'e': e_count, 'i': i_count, 'o': o_count, 'u': u_count}
    return resultados

# Ejemplo de uso
palabra_ejemplo = "Ratapinyada"
resultados_contados = contar_vocales(palabra_ejemplo)

# Mostramos los resultados de manera sencilla
for vocal, contador in resultados_contados.items():
    print(f"Hay {contador} {vocal}" if contador != 1 else f"Hay {contador} {vocal}")