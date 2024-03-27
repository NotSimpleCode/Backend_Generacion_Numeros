import congruencias
import csv

def getFloatFromFile(file):
    with open(file, 'r') as archivo:
        lector = csv.reader(archivo)
        lista = [float(fila[0]) for fila in lector]  # Extrae el único elemento de cada sublista
    return lista
    

def getRiEspecificos(semilla, k, c, g, m, a,paridad):
    xi_temporales = congruencias.getXi(semilla, paridad, True,k,c,g,m,a)

    ri = congruencias.crearRiAvanzadoCon("",len(xi_temporales),xi_temporales)

    return ri