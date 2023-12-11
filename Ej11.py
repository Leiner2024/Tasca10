#Definiciones de Calculadora de Enteros
def Sumar_b():
    a = int(input("Introduce el primer Número a sumar: "))
    b = int(input("Introduce el segundo Número a sumar: "))
    print("{} + {} ={}".format(a,b,a+b))
def Restar_b():
    a = int(input("Introduce el primer Número a restar: "))
    b = int(input("Introduce el segundo Número a restar: "))
    print("{} - {} ={}".format(a,b,a-b))
def Multiplicar_b():
    a = int(input("Introduce el primer Número a multiplicar: "))
    b = int(input("Introduce el segundo Número a multiplicar: "))
    print("{} * {} ={}".format(a,b,a*b))
def División_b():
    a = int(input("Introduce el primer Número a división: "))
    b = int(input("Introduce el segundo Número a división: "))
    print("{} / {} ={}".format(a,b,a/b))
def Salir_b():
    a = print("Hasta Luego, vuelves al menú principal")
    opcio = -1

#Definiciones de Calculadora Real
def Sumar_e():
    a = float(input("Introduce el primer Número a sumar: "))
    b = float(input("Introduce el segundo Número a sumar: "))
    print("{} + {} ={}".format(a,b,a+b))
def Restar_e():
    a = float(input("Introduce el primer Número a restar: "))
    b = float(input("Introduce el segundo Número a restar: "))
    print("{} - {} ={}".format(a,b,a-b))
def Multiplicar_e():
    a = float(input("Introduce el primer Número a multiplicar: "))
    b = float(input("Introduce el segundo Número a multiplicar: "))
    print("{} * {} ={}".format(a,b,a*b))
def División_e():
    a = float(input("Introduce el primer Número a división: "))
    b = float(input("Introduce el segundo Número a división: "))
    print("{} / {} ={}".format(a,b,a/b))
def Salir_e():
    a = print("Hasta Luego, vuelves al menú principal")
    opcio = -1

#Calculadora de Enteros(1)
def calculadora_enters():
#Inicia Calculadora de enteros (1)
    opcio = 2
    while opcio>0:
        opcio =  menu_enters()
        match opcio:
            case 1:
                Sumar_b()
            case 2:
                Restar_b()
            case 3:
                Multiplicar_b()
            case 4:
                División_b()
            case 5:
                Salir_b()
                print("Vuelves")
                opcio=-1
def menu_enters():
    y = 1
    while y>0:
        print("""
            Calculadora de enters
                1. Sumar
                2. Restar
                3. Multiplicación
                4. División
                5. Salir
              """)
        y = int(input("Elige la opción: "))
        if y>0 and y<6:
                return y
        else:
            print("Vuelve a Intentarlo: \n")

#Calculadora de Reales (2)
def calculadora_reals():
    opcio = 3
    while opcio>0:
        opcio =  Menú_Reales()
        match opcio:
            case 1:
                Sumar_e()
            case 2:
                Restar_e()
            case 3:
                Multiplicar_e()
            case 4:
                División_e()
            case 5:
                Salir_e()
                print("Vuelves")
                opcio=-1

def Menú_Reales():
    b = 1
    while b>0:
        print("""
            Calculadora de enters
                1. Sumar
                2. Restar
                3. Multiplicación
                4. División
                5. Salir
              """)
        b = int(input("Elige la opción: "))
        if b>0 and b<6:
                return b
        else:
            print("Vuelve a Intentarlo: \n")

#Menú Principal (Visualización)
def menu_principal():
    x = 1
    while x>0:
        print("""
            menu_principal:
                1. Calculadora enteros
                2. Calculadora reales
                3. salida
            """)
        x = int(input("Elige la opción: "))
        if x>0 and x<4:
            return x
        else:
            print("Vuelve a Intentarlo: \n")

#Programa principal          
opcio = 1
while opcio>0:
    opcio =  menu_principal()
    match opcio:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            print("Gràcies, m'en vaig!")
            opcio=-1