import random

def generadorBateria():
    cl = [random.randint(3,4), 4]
    print(str(cl))

    opciones = [1,2,4]
    opcion = random.choice(opciones)
    subdivision_clave = opcion * cl[0]
    print(str(subdivision_clave))

    clave = []
    filler = []
    metrica = []

    for i in range(0, subdivision_clave):
        clave.append(random.randint(0,1))
        filler.append(random.randint(0,1))
        metrica.append(random.randint(0,1))

    print("clave: " + str(clave))
    print("filler: " + str(filler))
    print("metrica: " + str(metrica))

    return clave, filler, metrica, opcion, subdivision_clave