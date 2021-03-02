from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *
import ventana_crear_operador

class VentanaOperadores(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaOperadores, self).__init__(parent)
        loadUi('plantillas/operadores.ui', self)
        self.listar_operadores()

        self.btn_actualizar.clicked.connect(self.actualizar_operadores)
        self.btn_eliminar.clicked.connect(self.eliminar_operador)
        self.btn_crear.clicked.connect(self.abrir_ventana_crear_operador)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()
    
    def abrir_ventana_crear_operador(self):
        ventana = ventana_crear_operador.VentanaCrearOperador(parent=self)
        self.statusBar().showMessage('Ventana de para crear operadores en ejecución')
        ventana.show()

    def listar_operadores(self):
        operadores = todo_operadores()
        tabla = self.table_operadores
        tabla.setRowCount(0)
        for row_number, row_data in enumerate(operadores):
            tabla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tabla.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def actualizar_operadores(self):
        tabla = self.table_operadores
        operadores = []
        fila = []
        for row_number in range(tabla.rowCount()):
            for column_number in range(tabla.columnCount()):
                if tabla.item(row_number, column_number) != None:
                    fila.append(tabla.item(row_number, column_number).text())
            if len(fila) > 0:
                operadores.append(fila)
            fila = []
        if len(operadores) > 0:
            for operador in operadores:
                resultado = actualizar_operador(operador[0], operador[1], operador[2], operador[3])
                if resultado != 0:
                    self.statusBar().showMessage('Se actualizaron los operadores')
                    self.listar_operadores()
                    

    def eliminar_operador(self):
        tabla = self.table_operadores
        if tabla.currentItem() != None:
            id = tabla.currentItem().text()
            resultado = eliminar_operador(id)
            if resultado:
                self.statusBar().showMessage(f'Se elimino el operador con id {id}')
                self.parent().cargar()
                self.listar_operadores()
            else:
                self.statusBar().showMessage('No se elimino el operador o no existe')


if __name__ == '__main__':
    app = QtWidgets.QApplication
    ventana = VentanaOperadores()
    ventana.show()
    app.exec_()