def nums_que_comencen_per(llista_noms, lletra):
    # Convertimos la letra a minúsculas para hacer la comparación sin importar el caso
    lletra_minuscula = lletra.lower()

    # Iniciamos el contador
    contador = 0
    
    # Iteramos sobre cada nombre en la lista
    for nom in llista_noms:
        # Convertimos el nombre a minúsculas para hacer la comparación sin importar el caso
        nom_minuscula = nom.lower()

        # Verificamos si el nombre comienza con la letra especificada
        if nom_minuscula.startswith(lletra_minuscula):
            contador += 1

    # Devolvemos el resultado
    return contador

# Solicitamos al usuario que ingrese la letra
lletra_input = input("Ingresa la letra para buscar nombres que comienzan con ella: ")

# Solicitamos al usuario que ingrese una lista de nombres separados por comas
llista_noms_input = input("Ingresa una lista de nombres separados por comas: ")

# Convertimos la entrada de nombres en una lista
llista_noms = [nom.strip() for nom in llista_noms_input.split(',')]

# Llamamos a la función y mostramos el resultado
resultat_contat = nums_que_comencen_per(llista_noms, lletra_input)
print(f"En la lista hay {resultat_contat} nombres que comienzan con la letra '{lletra_input}' o '{lletra_input.lower()}'.")
