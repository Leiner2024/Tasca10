# Bucle exterior (Vueltas) que va desde 0 hasta 5
for i in range(5):
    # Bucle interno (Número) que va desde 0 hasta 15
    for j in range(15):
        #Mostrar un mensaje con el número de la vuelta (i+1) y el número actual (j+1)
        print("Vuelta {}, númnero {}".format(i+1, j+1))