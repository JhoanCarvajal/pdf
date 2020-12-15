from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class VentanaCrearRestaurante(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaCrearRestaurante, self).__init__(parent)
        loadUi('plantillas/crear_restaurante.ui', self)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication
    ventana = VentanaCrearRestaurante()
    ventana.show()
    app.exec_()