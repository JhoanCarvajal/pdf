from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *

class VentanaCrearRestaurante(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaCrearRestaurante, self).__init__(parent)
        loadUi('plantillas/crear_restaurante.ui', self)

        regiones = lista_regiones()
        self.cb_region.clear()
        self.cb_region.addItems(regiones)
        self.buscar_id_region()

        self.le_medidor_telefono.textChanged.connect(self.buscar_restaurante_operador)
        self.le_nit_operador.textChanged.connect(self.buscar_operador)
        self.btn_guardar_restaurante.clicked.connect(self.guardar_restaurante)
        self.btn_guardar_operador.clicked.connect(self.guardar_operador)
        self.btn_guardar_relacion.clicked.connect(self.guardar_relacion)
        self.cb_region.currentTextChanged.connect(self.buscar_id_region)
        self.le_nombre_restaurante_2.textChanged.connect(self.buscar_id_restaurante)
        self.le_nit_operador_2.textChanged.connect(self.buscar_id_operador)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()
    
    def buscar_operador(self, text):
        self.le_nombre_operador.clear()
        self.le_servicio_operador.clear()
        operador = buscar_operador(text)
        if operador:
            self.le_nombre_operador.setText(operador.nombre)
            self.le_servicio_operador.setText(operador.servicio)

    def buscar_restaurante_operador(self, text):
        restaurante, operador = buscar_restaurate_operador(text)
        if restaurante and operador:
            self.le_nombre_restaurante_2.clear()
            self.le_nit_operador_2.clear()
            self.le_nombre_restaurante_2.setText(restaurante.nombre)
            self.le_nit_operador_2.setText(operador.nit)

    def guardar_operador(self):
        operador = []
        operador.append(self.le_nombre_operador.text())
        operador.append(self.le_nit_operador.text())
        operador.append(self.le_servicio_operador.text())
        guardar_operador(operador)
        
    
    def guardar_restaurante(self):
        restaurante = []
        restaurante.append(self.le_nombre_restaurante.text())
        restaurante.append(self.le_direccion_restaurante.text())
        restaurante.append(self.id_region)
        guardar_restaurante(restaurante)

    def guardar_relacion(self):
        restaurante_operador = []
        restaurante_operador.append(self.id_operador)
        restaurante_operador.append(self.id_restaurante)
        restaurante_operador.append(self.le_medidor_telefono.text())
        guardar_restaurante_operador(restaurante_operador)

    def buscar_id_region(self):
        nombre = self.cb_region.currentText()
        self.id_region = id_region(nombre)

    def buscar_id_restaurante(self, text):
        self.id_restaurante = id_restaurante(text)
    
    def buscar_id_operador(self, text):
        self.id_operador = id_operador(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication
    ventana = VentanaCrearRestaurante()
    ventana.show()
    app.exec_()