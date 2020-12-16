from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import lista_regiones, buscar_operador, id_region, guardar_restaurante
from controlador import buscar_restaurate_operador

class VentanaCrearRestaurante(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaCrearRestaurante, self).__init__(parent)
        loadUi('plantillas/crear_restaurante.ui', self)

        regiones = lista_regiones()
        self.cb_region.clear()
        self.cb_region.addItems(regiones)
        self.cambio_region()

        self.le_medidor_telefono.textChanged.connect(self.buscar_restaurante_operador)
        self.le_nit_operador.textChanged.connect(self.buscar_operador)
        self.btn_guardar_restaurante.clicked.connect(self.guardar_restaurante)
        self.cb_region.currentTextChanged.connect(self.cambio_region)

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
            self.le_nombre_restaurante.clear()
            self.le_direccion_restaurante.clear()
            self.le_nit_operador.clear()
            self.le_nombre_operador.clear()
            self.le_servicio_operador.clear()
            self.le_nombre_restaurante.setText(restaurante.nombre)
            self.le_direccion_restaurante.setText(restaurante.direccion)
            self.le_nit_operador.setText(operador.nit)
    
    def guardar_restaurante(self):
        restaurante = []
        restaurante.append(self.le_nombre_restaurante.text())
        restaurante.append(self.le_direccion_restaurante.text())
        restaurante.append(self.id_region)
        guardar_restaurante(restaurante)

    
    def cambio_region(self):
        print(self.cb_region.currentText())
        nombre = self.cb_region.currentText()
        self.id_region = id_region(nombre)



if __name__ == '__main__':
    app = QtWidgets.QApplication
    ventana = VentanaCrearRestaurante()
    ventana.show()
    app.exec_()