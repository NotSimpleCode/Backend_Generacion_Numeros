
import cuadrados, congruencias, utilidades,controlador,normal
from scipy.stats import norm


tipos_generacion = {
    1: "Cuadrados",
    2: "Congruencia",
    3: "Distribucion Normal"
}



def obtenerNi(tipo,min,max,ri,xi):
    if (tipo == 'Cuadrados' or tipo == 'Congruencia'):
        return crearNiUniformes(min,max,ri)

    elif (tipo == "Distribucion Normal"):

        media = utilidades.calcularMedia(xi)
        desv = utilidades.calcularDesviacion(xi)

        print(media)
        print(desv)

        return crearNiNormales(media, desv,ri)
    

def crearNiNormales(media, desv, ri):
    ni = []
    i=0
    for r in ri:
        ni.append(utilidades.truncar(norm.ppf(r, loc=media, scale=desv), 5))
    return ni

def crearNiUniformes(min, max,ri):
    ni = []
    for i in range(len(ri)):
        ni.append(utilidades.truncar(min + (max - min) * utilidades.truncar(ri[i],5),5))
    return ni
    
def establecerRi(tipo,semilla,k,c,g,m,a,paridad):
    if (tipo == 'Cuadrados'):
        return cuadrados.getRi()
    if (tipo == 'Congruencia'):
        return congruencias.getRi()
    if (tipo == "Distribucion Normal"):
        controlador.mostrar("Ahora digite los parametros usados para generar Ri que seran usados para generar Ni distribuidos normalmente")
        return normal.getRiEspecificos(semilla, k, c, g, m, a,paridad)

def establecerXi(tipo,semilla,paridad,k,c,g,m,a, file):
    if (tipo == 'Cuadrados'):
        return cuadrados.getXi(semilla)
    if (tipo == 'Congruencia'):
        return congruencias.getXi(semilla, paridad, False,k,c,g,m,a)
    if (tipo == 'Distribucion Normal'):
        return normal.getFloatFromFile(file)


def generate(semilla,tipo_elegido, min, max,paridad,k,c,g,m,a,file ):

    xi = establecerXi(tipos_generacion[tipo_elegido],semilla, paridad,k,c,g,m,a,file)

    ri = establecerRi(tipos_generacion[tipo_elegido],semilla,k,c,g,m,a,paridad)

    ni = obtenerNi(tipos_generacion[tipo_elegido], min, max,ri,xi)

    return xi,ri,ni

