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

        # recuperamos la lista que viene en **kwargs
        self.lista_vieja = []
        for _, value in kwargs.items():
            self.lista_vieja = value

        print(self.lista_vieja)

        self.buscar_causalidad(str(self.lista_vieja[0]))

        #llenar los input con datos
        self.le_matricula.setText(str(self.lista_vieja[0]))
        self.le_inicio.setText(str(self.lista_vieja[1]))
        self.le_final.setText(str(self.lista_vieja[2]))
        self.le_paga.setText(str(self.lista_vieja[4]))
        self.le_consumo_activa.setText(str(self.lista_vieja[8]))
        self.le_consumo_reactiva.setText(str(self.lista_vieja[9]))
        self.le_kw.setText(str(self.lista_vieja[10]))
        self.le_contribucion.setText(str(self.lista_vieja[12]))
        self.le_alumbrado.setText(str(self.lista_vieja[13]))

        # Eventos
        self.le_matricula.textChanged.connect(self.buscar_causalidad)
        self.btn_guardar.clicked.connect(self.enviar_datos)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()
    
    def buscar_causalidad(self, text):
        causalidad = controlador.buscar_causalidad(text)
        self.le_causalidad.clear()
        print(causalidad)
        if causalidad:
            self.le_causalidad.setText(causalidad)

    def enviar_datos(self):
        if self.le_causalidad.text() != "":
            self.lista = []
            self.lista.append(self.le_matricula.text()) # matricula
            self.lista.append(self.le_inicio.text()) # fecha inicial
            self.lista.append(self.le_final.text()) # fecha final
            self.lista.append(self.le_causalidad.text()) # causalidad
            self.lista.append(self.le_paga.text()) # paga
            self.lista.append(self.le_doc_pag.text()) # doc pag
            self.lista.append(self.le_doc_aj.text()) # doc aj
            self.lista.append(self.le_consumo_activa.text()) # consumo activa
            self.lista.append(self.le_consumo_reactiva.text()) # consumo reaciva
            self.lista.append(self.le_kw.text()) # kw/h
            self.lista.append(self.le_contribucion.text()) # contribucion
            self.lista.append(self.le_alumbrado.text()) # alumbrado
            self.lista.append(self.lista_vieja[15]) # direccion
            datos_buenos = analizar_datos.analisis(lista=self.lista)
            controlador.guardar_factura(datos_buenos)
            self.abrir_ventana_principal()
        else:
            self.le_matricula.setFocus()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = VentanaDatos()
    ventana.show()
    app.exec_()