import random
import time

# Función donde explicamos qué sucede
def intro():
    print("""En una época donde los gigantes gobiernan Menorca. Nosotros necesitamos comer,
    Estamos siguiendo el rastro del olor de la comida, pero nos encontramos en una encrucijada.
    Al final de cada camino hay un talayot, en uno viven los gigantes buenos que nos invitarán
    y en el otro son unos caníbales hambrientos, y nos comerán apenas nos vean.
    """)

# Función donde preguntamos a qué talayot queremos ir
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("¿A cuál Talayot quieres ir? Introduce 1 o 2: ")
    return talaiot

# Función que nos indica si compartirán la comida o seremos nosotros su manjar
def trobada(talaiot, puntos):
    print("Te estás acercando al talayot...")
    time.sleep(2)
    print("Está oscuro y es tenebroso...")
    time.sleep(2)
    print("Un gran gigante salta frente a ti, te agarra y ...")
    print("")
    time.sleep(2)
    gigante_amigo = random.randint(1, 2)
    if talaiot == str(gigante_amigo):
        print("Te invita a comer...")
        puntos += 10  # Añadimos 10 puntos por compartir la comida
    else:
        print("Te come de un bocado...ÑAMÑAMÑAM")
        puntos -= 5  # Restamos 5 puntos por ser comido

    return puntos

# Función principal
puntos_totales = 0
partida_nueva = ("si")

while partida_nueva == ("s") or partida_nueva == ("si"):
    intro()
    talayot_elegido = canviTalaiot()
    puntos_totales = trobada(talayot_elegido, puntos_totales)
    print(f"Tienes {puntos_totales} puntos.")
    partida_nueva = input("¿Quieres volver a comer (jugar)? Introduce si o no: ")
    print("\n")