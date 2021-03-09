from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from controlador import *

class VentanaActualizarRestaurante(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(VentanaActualizarRestaurante, self).__init__(parent)
        loadUi('plantillas/crear_restaurante.ui', self)

        self.lb_restaurante.setText('Actualizar Restaurante')
        self.setWindowTitle("Actualizar Restaurante")
        self.btn_guardar.setText('Actualizar')

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

        if kwargs:
            self.id_restaurante = kwargs.get("id_resta")
            self.buscar_restaurante()
            self.get_restaurante_operador()

        self.btn_guardar.clicked.connect(self.actualizar_restaurante)
        self.cb_departamentos.currentTextChanged.connect(self.buscar_id_departamento)
        self.cb_municipios.currentTextChanged.connect(self.buscar_id_municipio)
        self.cb_operadores.currentTextChanged.connect(self.buscar_id_operador)

    def buscar_restaurante(self):
        restaurante = buscar_restaurante(self.id_restaurante)
        print(self.cb_departamentos.count())
        if restaurante:
            self.le_nombre.setText(restaurante.nombre)
            self.le_direccion.setText(restaurante.direccion)
            municipio_resta = restaurante.id_municipio
            departamento_resta = municipio_resta.id_departamento
            for i, departamento in enumerate(self.departamentos):
                print(i, departamento.id, departamento.departamento)
                if departamento.id == departamento_resta.id:
                    print('igualesss')
                    self.cb_departamentos.setCurrentIndex(i)
                    self.id_departamento = departamento.id
            self.municipios_departamento_seleccionado()
            for i, municipio in enumerate(self.municipios):
                print(i, municipio.id, municipio.municipio)
                if municipio.id == municipio_resta.id:
                    print('igualesss')
                    self.cb_municipios.setCurrentIndex(i)
        
    def get_restaurante_operador(self):
        self.restaurante_operador = get_restaurante_operador(self.id_restaurante)
        if self.restaurante_operador:
            self.le_matricula.setText(self.restaurante_operador.matricula)
            operador_resta = self.restaurante_operador.id_operador
            for i, operador in enumerate(self.operadores):
                print(i, operador.id, operador.nombre)
                if operador.id == operador_resta.id:
                    print('igualesss')
                    self.cb_operadores.setCurrentIndex(i)

    def abrir_ventana_principal(self):
        self.parent().show()
        self.close()

    def buscar_restaurante_operador(self, text):
        restaurante, operador = buscar_restaurate_operador(text)
        if restaurante and operador:
            self.le_nombre.clear()
            self.le_nombre.setText(restaurante.nombre)
        
    def actualizar_restaurante(self):
        resultado = actualizar_restaurante(self.id_restaurante, self.le_nombre.text(), self.le_direccion.text(), self.id_municipio)
        if resultado != 0:
            self.parent().statusBar().showMessage('Restaurante actualizado!')
            self.actualizar_relacion()
        else:
            self.statusBar().showMessage('No se actualizo el restaurante')

    def actualizar_relacion(self):
        self.buscar_id_restaurante()
        print(f'id_resta_opera={self.restaurante_operador.id} id_operador={self.id_operador}, id_restaurante={self.id_restaurante}, matricula={self.le_matricula.text()}')
        resultado = actualizar_restaurante_operador(self.restaurante_operador.id, self.id_operador, self.id_restaurante, self.le_matricula.text())
        if resultado == 1:
            self.parent().statusBar().showMessage('Restaurante actualizado con operador de red')
            self.parent().listar_restaurantes()
            self.parent().parent().cargar()
            self.abrir_ventana_principal()
        else:
            self.statusBar().showMessage('Se actualizo el restaurante pero no se pudo relacionar con el operador')

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
        self.municipios = municipios_departamento(self.id_departamento)
        self.cb_municipios.clear()
        self.cb_municipios.addItems([municipio.municipio for municipio in self.municipios])


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = VentanaActualizarRestaurante(id_resta=16)
    ventana.show()
    app.exec_()