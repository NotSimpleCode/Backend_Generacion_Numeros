from PyQt5.QtGui import QStandardItemModel, QStandardItem
from itertools import zip_longest
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup,QFileDialog

from viewCode import Ui_MainWindow

import controlador

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fileName = ""
        self.ni = []
        self.ri = []
        # Crea un grupo de botones
        self.button_group = QButtonGroup()

        # Agrega los checkboxes al grupo
        
        self.button_group.addButton(self.ui.cb_cuadrados)
        self.button_group.addButton(self.ui.cb_congruencias)
        self.button_group.addButton(self.ui.cb_normal)

        self.ui.cb_cuadrados.setChecked(True) 

        # Conecta la señal toggled al slot
        self.button_group.buttonToggled.connect(self.cambioCaja)

        self.ui.btnGenerar.clicked.connect(self.generateRandom)
        self.ui.btnSubir.clicked.connect(self.abrirArchivo)
        self.ui.btnDescargar.clicked.connect(self.descargar)
        #enlazamos los campos para que su valor pedido se vincule a un objeto de la ventana
        self.campos = {
            "a": self.ui.txt_a,
            "c": self.ui.txt_c,
            "g": self.ui.txt_g,
            "k": self.ui.txt_k,
            "m": self.ui.txt_m
        }


    def abrirArchivo(self):
        options = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)", options=options)
        if archivo:
            self.fileName = archivo
            print("Archivo subido!")
            self.ui.lb_archivo.setText("Archivo subido!")
        else:
            self.ui.lb_archivo.setText("No hay archivo")


    def cambioCaja(self, checkbox, checked):
        if checked:
            print(f"Checkbox {checkbox.text()} seleccionado")

    def generateRandom(self):
        print("Generando Numeros!")
        self.ui.lb_generacion_2.setText("Generando Numeros...")

        opcion = 1 #opcion por defecto
        if (self.ui.cb_congruencias.isChecked()):
            opcion = 2
        elif (self.ui.cb_normal.isChecked()):
            opcion = 3

        semilla = self.ui.txt_semilla.text()
        minimo = self.ui.txt_min.text()
        maximo = self.ui.txt_max.text()

        # Verifica que los campos no estén vacíos
        if semilla and minimo and maximo:
            try:
                # Convierte los valores a enteros
                semilla = int(semilla)
                minimo = int(minimo)
                maximo = int(maximo)

                k,c,g,m,a = 0,0,0,0,0

                if opcion == 2:
                    k,c,g = self.obtenerData('k'),self.obtenerData('c'),self.obtenerData('g')
                elif opcion == 3 and self.fileName == '':
                    
                    self.ui.lb_generacion_2.setText("Falta cargar el archivo")

                elif opcion == 3 and self.fileName != '':
                    c,m,a = self.obtenerData('c'),self.obtenerData('m'),self.obtenerData('a')

                try:
                        
                    xi,self.ri,self.ni = controlador.generate(semilla, opcion, minimo, maximo,self.getParidad(), k,c,g,m,a,self.fileName)
                    self.crearTabla(xi)
                    
                except:
                    if opcion != 3:
                        self.ui.lb_generacion_2.setText("No ha sido posible generar, cambie los parametros")
                    elif opcion == 3 and self.fileName != '':
                        self.ui.lb_generacion_2.setText("Error al generar con archivo cargado o en parametros dados")
                    

            except ValueError:
                self.ui.lb_generacion_2.setText("Error: Los valores deben ser números enteros")
        else:
            self.ui.lb_generacion_2.setText("Error: Todos los campos principales deben estar completos")

    def crearTabla(self, xi):
        modelo = QStandardItemModel()
        
        # Añade las cabeceras
        modelo.setHorizontalHeaderLabels(['xi', 'ri', 'ni'])
        
        # Añade los datos
        for x, r, n in zip_longest(xi, self.ri, self.ni, fillvalue=''):
            modelo.appendRow([QStandardItem(str(x) if x is not None else ''), 
                            QStandardItem(str(r) if r is not None else ''), 
                            QStandardItem(str(n) if n is not None else '')])
        
        self.ui.datos.setModel(modelo)

        self.ui.datos.show()
        self.ui.lb_generacion_2.setText("Todo OK!")
    
    def descargar(self):
        self.ui.lb_generacion_2.setdasText("Descargando archivo...")
        print("Descargando archivo")

        self.ui.lb_generacion_2.setText("Archivos descargados!")

        # Escribe los datos de la lista ri en un archivo de texto
        with open('ri.txt', 'w') as f:
            for r in self.ri:
                f.write(str(r) + '\n')

        # Escribe los datos de la lista ni en un archivo de texto
        with open('ni.txt', 'w') as f:
            for n in self.ni:
                f.write(str(n) + '\n')


        
    def obtenerData(self,campo):
        if self.campos[campo].text() == "":
            self.ui.lb_generacion_2.setText("Error en la generacion por el campo vacio: " + campo)
            return -1
        else: 
            return int(self.campos[campo].text())

    def mostrar(self,texto):
        self.ui.lb_generacion_2.setText(texto)

    def getParidad(self):
        paridad = "impar"
        if self.ui.cb_paridad.isChecked():
            paridad = "par"
        else:
            paridad = "impar"
        return paridad

if __name__ == "__main__":
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()

