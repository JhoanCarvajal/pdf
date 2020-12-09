from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
import llenar_excel, pdf2img
import detectar_proveedor
import analizar_datos
import datos
import os
import threading
import tkinter.font as tkFont

import controlador

class Ventana:

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("prototipo facturación de frisby")
        self.ventana.geometry("800x450")
        self.ventana.resizable(0,0)
        self.ventana.config(bg="#D5DDF0")

        self.titulos = tkFont.Font(family="Arial", size=12, weight='bold')
        self.fuente = tkFont.Font(family="Arial", size=11)

        self.frame = Frame(self.ventana, bg="#D5DDF0")
        self.frame.pack(fill=BOTH, expand=True, padx=30, pady=30)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

        lb_facturas = Label(self.frame, text = "Seleccione la factura para guardarla en la base de datos", font=self.titulos, bg="#D5DDF0", anchor="e")
        lb_facturas.pack()

        self.frame_archivo = Frame(self.frame, bg="#9197A3")
        self.frame_archivo.pack(fill=BOTH, expand=True)
        self.frame_archivo.columnconfigure(1, weight=1)
        self.frame_archivo.rowconfigure(1, weight=1)

        self.frame_seleccionar = Frame(self.frame_archivo, bg="#9197A3")
        self.frame_seleccionar.grid(row=0, column=0)

        self.frame_ruta = Frame(self.frame_archivo, bg="#9197A3")
        self.frame_ruta.grid(row=0, column=1)

        self.frame_guardar = Frame(self.frame, bg="#D5DDF0")
        self.frame_guardar.pack(fill=BOTH, expand=True)
        self.frame_guardar.columnconfigure(1, weight=1)
        self.frame_guardar.rowconfigure(1, weight=1)

        self.lb_consultas = Label(self.frame, text = "Seleccione datos para hacer consultas", font=self.titulos, bg="#D5DDF0")
        self.lb_consultas.pack()

        self.frame_consultas = Frame(self.frame, bg="#9197A3")
        self.frame_consultas.pack(fill=BOTH, expand=True)
        self.frame_consultas.columnconfigure(1, weight=1)
        self.frame_consultas.rowconfigure(1, weight=1)

        self.restaurantes = controlador.lista_restaurantes()
        if not self.restaurantes:
            self.restaurantes.append("Ninguno")
        fecha_actual = datetime.now()
        año = fecha_actual.year
        self.años = []
        for i in range(año,(año-30),-1):
            self.años.append(i)
        self.meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

        # algunas variables
        self.matriz_datos = []

        # los widgets
        self.btn_seleccionar = Button(self.frame_seleccionar, text = "Seleccionar", fg="white", bg="#425070", font=self.fuente, width=25, height=2, command = self.seleccionar)
        self.nombre_pdf = Label(self.frame_ruta, text = "Ruta del archivo", bg="#D5DDF0")
        self.btn_analizar = Button(self.frame_ruta, text = "Analizar", fg="white", font=self.fuente, bg="#425070", width=25, height=2, state=DISABLED, command = self.analizar)
        self.lb_matricula = Label(self.frame_guardar, text="Matricula:")
        self.entry_matricula = Entry(self.frame_guardar)
        self.lb_causa = Label(self.frame_guardar, text="Causa:")
        self.entry_causa = Entry(self.frame_guardar)
        self.lb_doc_pag = Label(self.frame_guardar, text="Doc pag:")
        self.entry_doc_pag = Entry(self.frame_guardar)
        self.lb_doc_aj = Label(self.frame_guardar, text="Doc aj:")
        self.entry_doc_aj = Entry(self.frame_guardar)
        self.btn_guardar = Button(self.frame_guardar, text = "Guardar", fg="white", font=self.fuente, bg="#425070", width=25, height=2, state=DISABLED, command = self.guardar)
        self.lb_mes = Label(self.frame_consultas, text = "Mes: ", font=self.fuente, bg="#D5DDF0", width=20, height=2)
        self.cb_mes = ttk.Combobox(self.frame_consultas, font=self.fuente, width=20, value = self.meses)
        self.cb_mes.current(0)
        self.lb_restaurante = Label(self.frame_consultas, text = "Restaurante: ", font=self.fuente, bg="#D5DDF0", width=20, height=2)
        self.cb_restaurantes = ttk.Combobox(self.frame_consultas, font=self.fuente, width=20, value = self.restaurantes)
        self.cb_restaurantes.current(0)
        self.lb_año = Label(self.frame_consultas, text = "Año: ", bg="#D5DDF0", font=self.fuente, width=20, height=2)
        self.cb_años = ttk.Combobox(self.frame_consultas, font=self.fuente, width=20, value = self.años)
        self.cb_años.current(0)
        self.btn_consulta = Button(self.frame_consultas, text = "Consultar mes", fg="white", bg="#425070", font=self.fuente, width=20, height=2, command = self.consultar)
        self.btn_consulta_año = Button(self.frame_consultas, text = "Consultar año", fg="white", bg="#425070", font=self.fuente, width=20, height=2, command = self.consultar_año)
        self.btn_consulta_todo = Button(self.frame_consultas, text = "Consultar todo", fg="white", bg="#425070", font=self.fuente, width=20, height=2, command = self.consultar_todo)

        #pongo los widgets donde quiero
        self.btn_seleccionar.grid(row=0, column=0, padx=15, pady=10)
        self.nombre_pdf.grid(row=0, column=0, padx=15, pady=2)
        self.btn_analizar.grid(row=1, column=0, padx=0, pady=2)
        self.lb_matricula.grid(row=0, column=0, padx=0, pady=0, sticky="sw")
        self.entry_matricula.grid(row=1, column=0, padx=0, pady=0)
        self.lb_causa.grid(row=0, column=1, padx=0, pady=0, sticky="sw")
        self.entry_causa.grid(row=1, column=1, padx=0, pady=0)
        self.lb_doc_pag.grid(row=0, column=2, padx=0, pady=0, sticky="sw")
        self.entry_doc_pag.grid(row=1, column=2, padx=0, pady=0)
        self.lb_doc_aj.grid(row=0, column=3, padx=0, pady=0, sticky="sw")
        self.entry_doc_aj.grid(row=1, column=3, padx=0, pady=0)
        self.btn_guardar.grid(row=0, rowspan=2, column=4, padx=5, pady=0)
        self.lb_mes.grid(row=4, column=0, padx=15, pady=5)
        self.cb_mes.grid(row=5, column=0, padx=15, pady=5)
        self.lb_restaurante.grid(row=4, column=1, padx=15, pady=5)
        self.cb_restaurantes.grid(row=5, column=1, padx=15, pady=5)
        self.lb_año.grid(row=4, column=2, padx=15, pady=5)
        self.cb_años.grid(row=5, column=2, padx=15, pady=5)
        self.btn_consulta.grid(row=7, column=0, padx=15, pady=10)
        self.btn_consulta_año.grid(row=7, column=1, padx=15, pady=10)
        self.btn_consulta_todo.grid(row=7, column=2, padx=15, pady=10)

    def limpiar_entrys(self):
        self.entry_matricula.delete(0, "end")
        self.entry_causa.delete(0, "end")
        self.entry_doc_pag.delete(0, "end")
        self.entry_doc_aj.delete(0, "end")

    def seleccionar(self):
        pdf_ruta = askopenfilename()
        self.nombre_pdf["text"] = str(pdf_ruta)
        if self.nombre_pdf.cget("text") != "":
            del self.matriz_datos[:]
            lista_imagenes = pdf2img.pdf2img(pdf_ruta)
            for ruta_img in lista_imagenes:
                lista_datos = detectar_proveedor.proveedor(ruta_img)
                self.matriz_datos.append(lista_datos)
                self.limpiar_entrys()
                self.entry_matricula.insert(0, str(lista_datos[0]))
            self.btn_analizar.config(state=NORMAL)
            self.entry_matricula.config(bg="green")
        else:
            self.nombre_pdf["text"] = "Ninguno"

    def abrir_ventana(self):
        _, _ = datos.create_editar(rt=self.ventana, matriz=self.matriz_datos[0])

    def analizar(self):
        if self.entry_matricula.get() == "":
            self.entry_matricula.config(bg="red")
        elif self.entry_causa.get() == "":
            self.entry_causa.config(bg="red")
        elif self.entry_doc_pag.get() == "":
            self.entry_doc_pag.config(bg="red")
        elif self.entry_doc_aj.get() == "":
            self.entry_doc_aj.config(bg="red")
        else:
            datos = analizar_datos.analisis(self.matriz_datos[0], self.entry_causa.get(), self.entry_doc_pag.get(), self.entry_doc_aj.get(),True)
            del self.matriz_datos[:]
            self.matriz_datos.append(datos)
            self.abrir_ventana()
            self.btn_analizar.config(state=DISABLED)
        self.btn_guardar.config(state=NORMAL)

    def guardar(self):
        controlador.guardar_factura(self.matriz_datos[0])
        self.btn_analizar.config(state=DISABLED)
        self.btn_guardar.config(state=DISABLED)

    def consultar(self):
        mes = self.cb_mes.get()
        for m in self.meses:
            if m == mes:
                mes = self.meses.index(m) + 1
        resultado = controlador.info_restaurante(mes,self.cb_restaurantes.get(),self.cb_años.get())
        llenar_excel.consulta(resultado)

    def consultar_año(self):
        resultado = controlador.info_todo_año(self.cb_restaurantes.get(),self.cb_años.get())
        llenar_excel.consulta(resultado)

    def consultar_todo(self):
        restaurantes, facturas = controlador.todo()
        llenar_excel.consulta2(restaurantes, facturas)

if __name__ == '__main__':
    import models
    models.crear_tablas()
    root = Tk()
    Ventana(root)
    root.mainloop()