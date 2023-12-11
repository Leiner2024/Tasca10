import random

def generar_codigo():
    """Genera un código de 4 dígitos aleatorio."""
    return [random.randint(0, 9) for _ in range(4)]

def comparar_codigos(codigo_secreto, intento_usuario):
    """Compara el código secreto con el intento del usuario."""
    aciertos = sum(a == b for a, b in zip(codigo_secreto, intento_usuario))
    coincidencias = sum(min(codigo_secreto.count(digito), intento_usuario.count(digito)) for digito in set(intento_usuario)) - aciertos
    return aciertos, coincidencias

def main():
    print("Bienvenido a MasterMind Simplificado. Intenta adivinar el código de 4 dígitos.")

    codigo_secreto = generar_codigo()
    intentos = 0

    while True:
        intento_usuario = input("Introduce tu intento (4 dígitos): ")

        # Verificamos que la entrada sea válida
        if not intento_usuario.isdigit() or len(intento_usuario) != 4:
            print("Por favor, introduce un código válido de 4 dígitos.")
            continue

        intento_usuario = [int(digito) for digito in intento_usuario]

        # Comparamos el intento del usuario con el código secreto
        aciertos, coincidencias = comparar_codigos(codigo_secreto, intento_usuario)
        intentos += 1

        # Mostramos el resultado
        print(f"Aciertos: {aciertos}, Coincidencias: {coincidencias}")

        # Comprobamos si el usuario ha adivinado el código
        if aciertos == 4:
            print(f"¡Felicidades! Has adivinado el código en {intentos} intentos.")
            break

if __name__ == "__main__":
    main()