from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *

class VentanaOperadores(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaOperadores, self).__init__(parent)
        loadUi('plantillas/operadores.ui', self)
        self.listar_operadores()

        
        self.btn_listar.clicked.connect(self.listar_operadores)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()

    def listar_operadores(self):
        operadores = todo_operadores()
        print(operadores)
        table = self.table_operadores
        table.setRowCount(0)
        for row_number, row_data in enumerate(operadores):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


if __name__ == '__main__':
    app = QtWidgets.QApplication
    ventana = VentanaOperadores()
    ventana.show()
    app.exec_()