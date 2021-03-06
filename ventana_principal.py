# from  plantillas.principal_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from datetime import date
from datetime import datetime
import llenar_excel, pdf2img
import detectar_proveedor
import analizar_datos
import os
import threading
import controlador
import ventana_datos, ventana_operadores
import ventana_restaurantes



class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(VentanaPrincipal, self).__init__(*args, **kwargs)
        loadUi('plantillas/principal.ui', self)

        self.boolean = True
        self.operador = None

        self.cargar()

        if not self.restaurantes:
            self.restaurantes.append("Ninguno")
        if not self.operadores:
            self.operadores.append("Operador")

        fecha_actual = datetime.now()
        año = fecha_actual.year
        self.años = []
        for i in range(año,(año-30),-1):
            self.años.append(i)
        for i in range(len(self.años)):
            self.años[i] = str(self.años[i])
        self.meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

        self.cb_meses.clear()
        self.cb_anhos.clear()

        self.cb_meses.addItems(self.meses)
        self.cb_anhos.addItems(self.años)

        self.matriz_datos = []

        ####################################      eventos             ################################
        self.btn_seleccionar.clicked.connect(self.seleccionar)
        self.btn_analizar.clicked.connect(self.analizar)
        self.btn_consultar_mes.clicked.connect(self.consultar_mes)
        self.btn_consultar_anho.clicked.connect(self.consultar_anho)
        self.btn_consultar_todo.clicked.connect(self.consultar_todo)
        self.btn_restaurantes.clicked.connect(self.abrir_ventana_restaurantes)
        self.btn_operadores.clicked.connect(self.abrir_ventana_operadores)
        self.le_matricula.textChanged.connect(self.buscar_restaurante_operador)
        self.cb_operador.activated[str].connect(self.buscar_operador_nombre)
        ####################################     fin eventos             ################################

    def limpiar_le(self):
        self.le_matricula.clear()
    
    def cargar(self):
        self.restaurantes = controlador.lista_restaurantes()
        self.operadores = controlador.lista_operadores()

        self.cb_restaurantes.clear()
        self.cb_operador.clear()
        
        self.cb_restaurantes.addItems(self.restaurantes)
        self.cb_operador.addItems([operador.nombre for operador in self.operadores])
        
        self.buscar_operador_nombre(self.cb_operador.currentText())

    def buscar_restaurante_operador(self, text):
        restaurante, operador = controlador.buscar_restaurate_operador(text)
        if restaurante and operador:
            self.lb_nombre_restaurante.setText(restaurante.nombre)
            self.lb_nombre_operador.setText(operador.nombre)

    def buscar_operador_nombre(self, text):
        id_operador = controlador.id_operador_nombre(text)
        if id_operador:
            print(id_operador)
            self.operador = id_operador

    def seleccionar(self):
        self.statusBar().showMessage('seleccionando archivo')
        pdf_ruta, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir pdf", None, "pdf files (*.pdf)")
        self.lb_ruta.setText(pdf_ruta)
        if self.lb_ruta.text() != "":
            self.statusBar().showMessage('Cargando el pdf seleccionado...')
            del self.matriz_datos[:]
            lista_imagenes = pdf2img.pdf2img(pdf_ruta)
            print(lista_imagenes)
            for ruta_img in lista_imagenes:
                lista_datos = detectar_proveedor.proveedor(self, ruta_img)
                print(self.operador)
                if lista_datos:
                    self.matriz_datos.append(lista_datos)
                    self.limpiar_le()
                    self.le_matricula.setText(str(lista_datos[0]))
                    self.statusBar().showMessage('Se cargo el pdf correctamente')
                    self.boolean = True
                else:
                    self.statusBar().showMessage('Este pdf no es del proveedor seleccionado o esta mal escaneado!')
        else:
            self.statusBar().showMessage('No se ha seleccionado un pdf')
            self.lb_ruta.setText("Ninguno")

    def abrir_ventana_datos(self):
        matriz = self.matriz_datos[0]
        # self.hide()
        ventana = ventana_datos.VentanaDatos(parent=self, matriz=matriz)
        self.statusBar().showMessage('Ventana de datos en ejecución')
        ventana.show()
    
    def abrir_ventana_restaurantes(self):
        ventana = ventana_restaurantes.VentanaRestaurantes(parent=self)
        self.statusBar().showMessage('Ventana de para restaurantes en ejecución')
        ventana.show()

    def abrir_ventana_operadores(self):
        ventana = ventana_operadores.VentanaOperadores(parent=self)
        self.statusBar().showMessage('Ventana de para operadores en ejecución')
        ventana.show()

    def analizar(self):
        if not self.matriz_datos[0]:
            print('No ha cargado un pdf')
            self.statusBar().showMessage('No ha cargado un pdf')
        elif self.le_matricula.text() == "":
            self.le_matricula.setFocus()
            self.statusBar().showMessage('No hay una matricula')
        else:
            self.statusBar().showMessage('Analisando datos del pdf...')
            self.matriz_datos[0][0] = self.le_matricula.text()
            datos = analizar_datos.analisis(self.operador, self.matriz_datos[0], self.boolean)
            self.boolean = False
            del self.matriz_datos[:]
            self.matriz_datos.append(datos)
            self.abrir_ventana_datos()

    def consultar_mes(self):
        mes = self.cb_meses.currentText()
        for m in self.meses:
            if m == mes:
                mes = self.meses.index(m) + 1
        print(mes, self.cb_restaurantes.currentText(), self.cb_anhos.currentText())
        resultado = controlador.info_restaurante(mes, self.cb_restaurantes.currentText(), self.cb_anhos.currentText())
        print(resultado)
        llenar_excel.consulta(resultado)

    def consultar_anho(self):
        resultado = controlador.info_todo_año(self.cb_restaurantes.currentText(),self.cb_anhos.currentText())
        llenar_excel.consulta(resultado)

    def consultar_todo(self):
        restaurantes, facturas = controlador.todo()
        llenar_excel.consulta2(restaurantes, facturas)


if __name__ == "__main__":
    import models
    models.crear_tablas()
    app = QtWidgets.QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec_()