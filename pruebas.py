import utilidades,normal,app,vista


print(utilidades.extraer_numero(1522756,1,5))

print(utilidades.extraer_numero(27321529,2,6))

print(utilidades.extraer_numero(323761,0,4))

print(utilidades.extraer_numero(57600,0,3))

print(utilidades.extraer_numero(576,0,2))

print(utilidades.extraer_numero(576,0,1))

from PyQt5.Qt import PYQT_VERSION_STR
print(PYQT_VERSION_STR)


#print(normal.getFloatFromFile('experimentales - numeros.csv'))



print(normal.getFloatFromFile('resistencia_jugadores.csv'))

xi = normal.getFloatFromFile('resistencia_jugadores.csv')

print(utilidades.calcularMedia(xi))
print(utilidades.calcularDesviacion(xi))

#ri= [0.514629708,0.728304617,0.666991696,0.048346867,0.149263385,0.255501713,0.364368108,0.139158445,0.858478488,0.703653518,0.09768332,0.925632224,0.873749475,0.702041984,0.141013518]

#print(app.crearNiNormales(16.11,0.835,ri))

#utilidades.descargar("ni_normales", app.crearNiNormales(35,10,normal.getFloatFromFile("ri_aprobados.txt")))
