from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *

class VentanaCrearOperador(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaCrearOperador, self).__init__(parent)
        loadUi('plantillas/crear_operador.ui', self)

        
        self.btn_crear.clicked.connect(self.guardar_operador)
        self.le_nit.textChanged.connect(self.buscar_operador)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()

    def buscar_operador(self, text):
        operador = buscar_operador(text)
        if operador:
            self.le_nombre.clear()
            self.le_direccion.clear()
            self.le_nombre.setText(operador.nombre)
            self.le_direccion.setText(operador.direccion)

    def guardar_operador(self):
        resultado = guardar_operador(self.le_nombre.text(), self.le_nit.text(), self.le_direccion.text())
        if resultado == 1:
            self.parent().statusBar().showMessage('Operador creado')
            self.parent().listar_operadores()
            self.parent().parent().cargar()
            self.abrir_ventana_principal()
        else:
            self.statusBar().showMessage('No se creo el operador porque ya existe')


if __name__ == '__main__':
    app = QtWidgets.QApplication
    ventana = VentanaCrearOperador()
    ventana.show()
    app.exec_()