from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *

class VentanaCrearRestaurante(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaCrearRestaurante, self).__init__(parent)
        loadUi('plantillas/crear_restaurante.ui', self)

        self.departamentos = lista_departamentos()
        self.operadores = lista_operadores()

        self.cb_departamentos.clear()
        self.cb_municipios.clear()
        self.cb_operadores.clear()

        self.cb_departamentos.addItems([departamento.departamento for departamento in self.departamentos])
        self.cb_operadores.addItems([operador.nombre for operador in self.operadores])

        self.buscar_id_departamento()
        self.buscar_id_municipio()
        self.buscar_id_operador()

        self.btn_guardar.clicked.connect(self.guardar_restaurante)
        self.cb_departamentos.currentTextChanged.connect(self.buscar_id_departamento)
        self.cb_municipios.currentTextChanged.connect(self.buscar_id_municipio)
        self.cb_operadores.currentTextChanged.connect(self.buscar_id_operador)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()

    def buscar_restaurante_operador(self, text):
        restaurante, operador = buscar_restaurate_operador(text)
        if restaurante and operador:
            self.le_nombre.clear()
            self.le_nombre.setText(restaurante.nombre)
        
    def guardar_restaurante(self):
        resultado = guardar_restaurante(self.le_nombre.text(), self.le_direccion.text(), self.id_municipio)
        if resultado == 1:
            self.parent().statusBar().showMessage('Restaurante creado!')
            self.guardar_relacion()
        else:
            self.statusBar().showMessage('No se creo el restaurante porque ya existe')

    def guardar_relacion(self):
        self.buscar_id_restaurante()
        print(f'id_operador={self.id_operador}, id_restaurante={self.id_restaurante}, matricula={self.le_matricula.text()}')
        resultado = guardar_restaurante_operador(self.id_operador, self.id_restaurante, self.le_matricula.text())
        if resultado == 1:
            self.parent().statusBar().showMessage('Restaurante creado con operador de red')
            self.parent().listar_restaurantes()
            self.parent().parent().cargar()
            self.abrir_ventana_principal()
        else:
            self.statusBar().showMessage('Se creo el restaurante pero no se pudo relacionar con el operador')

    def buscar_id_departamento(self):
        nombre = self.cb_departamentos.currentText()
        self.id_departamento = id_departamento(nombre)
        self.municipios_departamento_seleccionado()
    
    def buscar_id_municipio(self):
        nombre = self.cb_municipios.currentText()
        self.id_municipio = id_municipio(nombre)

    def buscar_id_operador(self):
        nombre = self.cb_operadores.currentText()
        self.id_operador = id_operador_nombre(nombre)

    def buscar_id_restaurante(self):
        nombre = self.le_nombre.text()
        self.id_restaurante = id_restaurante(nombre)

    def municipios_departamento_seleccionado(self):
        print(self.id_departamento)
        self.municipios = municipios_departamento(self.id_departamento)
        self.cb_municipios.clear()
        self.cb_municipios.addItems([municipio.municipio for municipio in self.municipios])

    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = VentanaCrearRestaurante()
    ventana.show()
    app.exec_()