from  plantillas.principal_ui import *
from PyQt5.uic import loadUi
from datetime import date
from datetime import datetime
import llenar_excel, pdf2img
import detectar_proveedor
import analizar_datos
import datos
import os
import threading
import controlador
import ventana_datos


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(VentanaPrincipal, self).__init__(*args, **kwargs)
        loadUi('plantillas/principal.ui', self)

        # QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # self.setupUi(self)

        self.restaurantes = controlador.lista_restaurantes()
        if not self.restaurantes:
            self.restaurantes.append("Ninguno")
        fecha_actual = datetime.now()
        año = fecha_actual.year
        self.años = []
        for i in range(año,(año-30),-1):
            self.años.append(i)
        for i in range(len(self.años)):
            self.años[i] = str(self.años[i])
        self.meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

        self.cb_meses.clear()
        self.cb_restaurantes.clear()
        self.cb_anhos.clear()

        self.cb_meses.addItems(self.meses)
        self.cb_restaurantes.addItems(self.restaurantes)
        self.cb_anhos.addItems(self.años)

        self.matriz_datos = []

        ####################################      eventos             ################################
        self.btn_seleccionar.clicked.connect(self.seleccionar)
        self.btn_analizar.clicked.connect(self.analizar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_consultar_mes.clicked.connect(self.consultar_mes)
        self.btn_consultar_anho.clicked.connect(self.consultar_anho)
        self.btn_consultar_todo.clicked.connect(self.consultar_todo)

    def limpiar_le(self):
        self.le_matricula.clear()
        self.le_causa.clear()
        self.le_doc_pag.clear()
        self.le_doc_aj.clear()

    def seleccionar(self):
        pdf_ruta, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir pdf", None, "pdf files (*.pdf)")
        self.lb_ruta.setText(pdf_ruta)
        if self.lb_ruta.text() != "":
            del self.matriz_datos[:]
            lista_imagenes = pdf2img.pdf2img(pdf_ruta)
            for ruta_img in lista_imagenes:
                lista_datos = detectar_proveedor.proveedor(ruta_img)
                self.matriz_datos.append(lista_datos)
                self.limpiar_le()
                self.le_matricula.setText(str(lista_datos[0]))
        else:
            self.lb_ruta.setText("Ninguno")

    def abrir_ventana(self):
        matriz = self.matriz_datos[0]
        # self.hide()
        ventana = ventana_datos.VentanaDatos(parent=self, matriz=matriz)
        ventana.show()

    def analizar(self):
        if self.le_matricula.text() == "":
            self.le_matricula.setFocus()
        elif self.le_causa.text() == "":
            self.le_causa.setFocus()
        elif self.le_doc_pag.text() == "":
            self.le_doc_pag.setFocus()
        elif self.le_doc_aj.text() == "":
            self.le_doc_aj.setFocus()
        else:
            datos = analizar_datos.analisis(self.matriz_datos[0], str(self.le_causa.text()), str(self.le_doc_pag.text()), str(self.le_doc_aj.text()),True)
            del self.matriz_datos[:]
            self.matriz_datos.append(datos)
            self.abrir_ventana()

    def guardar(self):
        controlador.guardar_factura(self.matriz_datos[0])

    def consultar_mes(self):
        mes = self.cb_mes.get()
        for m in self.meses:
            if m == mes:
                mes = self.meses.index(m) + 1
        resultado = controlador.info_restaurante(mes,self.cb_restaurantes.get(),self.cb_años.get())
        llenar_excel.consulta(resultado)

    def consultar_anho(self):
        resultado = controlador.info_todo_año(self.cb_restaurantes.get(),self.cb_años.get())
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