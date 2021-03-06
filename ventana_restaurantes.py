from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *
import ventana_crear_restaurante, ventana_actualizar_restaurante

class VentanaRestaurantes(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaRestaurantes, self).__init__(parent)
        loadUi('plantillas/restaurantes.ui', self)
        self.listar_restaurantes()

        self.btn_actualizar.clicked.connect(self.actualizar_restaurantes)
        self.btn_eliminar.clicked.connect(self.eliminar_restaurante)
        self.btn_crear.clicked.connect(self.abrir_ventana_crear_restaurante)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()
    
    def abrir_ventana_crear_restaurante(self):
        ventana = ventana_crear_restaurante.VentanaCrearRestaurante(parent=self)
        self.statusBar().showMessage('Ventana de para crear restaurantes en ejecución')
        ventana.show()

    def listar_restaurantes(self):
        restaurantes = todo_restaurantes()
        tabla = self.table_restaurantes
        tabla.setRowCount(0)
        for row_number, row_data in enumerate(restaurantes):
            tabla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tabla.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def actualizar_restaurantes(self):
        tabla = self.table_restaurantes
        if tabla.currentItem() != None:
            id = tabla.currentItem().text()
            ventana = ventana_actualizar_restaurante.VentanaActualizarRestaurante(parent=self, id_resta=id)
            self.statusBar().showMessage('Ventana de para crear restaurantes en ejecución')
            ventana.show()    

    def eliminar_restaurante(self):
        tabla = self.table_restaurantes
        if tabla.currentItem() != None:
            id = tabla.currentItem().text()
            resultado = eliminar_restaurante(id)
            if resultado:
                self.statusBar().showMessage(f'Se elimino el restaurante con id {id}')
                self.parent().cargar()
                self.listar_restaurantes()
            else:
                self.statusBar().showMessage('No se elimino el restaurante o no existe')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = VentanaRestaurantes()
    ventana.show()
    app.exec_()