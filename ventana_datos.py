# from plantillas.datos_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import analizar_datos
import controlador

class VentanaDatos(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaDatos, self).__init__(parent)
        loadUi('plantillas/datos.ui', self)

        # QtWidgets.QMainWindow.__init__(*args, **kwargs)
        # self.setupUi(self)

        self.btn_guardar.clicked.connect(self.enviar_datos)

        # recuperamos la lista que viene en **kwargs
        self.lista_vieja = []
        for _, value in kwargs.items():
            self.lista_vieja = value

        #llenar los input con datos
        self.le_matricula.setText(str(self.lista_vieja[0]))
        self.le_inicio.setText(str(self.lista_vieja[1]))
        self.le_final.setText(str(self.lista_vieja[2]))
        self.le_valor_pagar.setText(str(self.lista_vieja[14]))
        self.le_consumo_activa.setText(str(self.lista_vieja[8]))
        self.le_consumo_reactiva.setText(str(self.lista_vieja[9]))
        self.le_kw.setText(str(self.lista_vieja[10]))
        self.le_valor_kw.setText(str(self.lista_vieja[11]))
        self.le_contribucion.setText(str(self.lista_vieja[12]))
        self.le_alumbrado.setText(str(self.lista_vieja[13]))

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()

    def enviar_datos(self):
        self.lista = []
        self.lista.append(self.le_matricula.text())
        self.lista.append(self.le_inicio.text())
        self.lista.append(self.le_final.text())
        self.lista.append(self.le_valor_pagar.text())
        self.lista.append(self.lista_vieja[3])
        self.lista.append(self.lista_vieja[6])
        self.lista.append(self.lista_vieja[7])
        self.lista.append(self.le_consumo_activa.text())
        self.lista.append(self.le_consumo_reactiva.text())
        self.lista.append(self.le_kw.text())
        self.lista.append(self.le_valor_kw.text())
        self.lista.append(self.le_contribucion.text())
        self.lista.append(self.le_alumbrado.text())
        self.lista.append(self.lista_vieja[15])
        datos_buenos = analizar_datos.analisis(lista=self.lista)
        controlador.guardar_factura(datos_buenos)
        self.abrir_ventana_principal()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = VentanaDatos()
    ventana.show()
    app.exec_()