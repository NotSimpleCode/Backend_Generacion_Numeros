import utilidades

xi_2 = []
extracciones = []
extensiones = []
xi = []

inicial = 0

def getXi(semilla):

    xi_2.clear()
    extracciones.clear()
    extensiones.clear()
    xi.clear()

    inicializar(semilla)

    i = 0
    while (extensiones[i] >= 3):
        
        extraer(i)

        generarCuadrados(i)

        i+=1

    return xi


def generarCuadrados(i):
    xi.append(extracciones[i])        
    xi_2.append(pow(xi[i+1],2))
    extensiones.append(utilidades.obtener_largo_numero(xi_2[i+1]))



def extraer(i):

    if (extensiones[i] == 8):
        extracciones.append(utilidades.extraer_numero(xi_2[i],2,6))
    elif (extensiones[i] == 7):
        extracciones.append(utilidades.extraer_numero(xi_2[i],1,5))
    elif (extensiones[i] == 6):
        extracciones.append(utilidades.extraer_numero(xi_2[i],0,4))
    elif (extensiones[i] == 5):
        extracciones.append(utilidades.extraer_numero(xi_2[i],0,3))
    elif (extensiones[i] == 4):
        extracciones.append(utilidades.extraer_numero(xi_2[i],0,2))
    elif (extensiones[i] == 3):
        extracciones.append(utilidades.extraer_numero(xi_2[i],0,1))


def inicializar(semilla):
    xi.append(semilla)
    xi_2.append(pow(xi[0],2))
    extensiones.append(utilidades.obtener_largo_numero(xi_2[0]))

def getRi():
    ri = []
    for i in range(len(extracciones)):
        ri.append(extracciones[i]/10000)
    return ri

