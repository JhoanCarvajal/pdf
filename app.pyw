from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
import select_restaurante, llenar_excel, pdf2img
import detectar_proveedor
import analizar_datos
import insert
from templates_ocr.datos.datos import create_editar
import os
import threading

import tkinter.font as tkFont

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

        self.restaurantes = select_restaurante.lista_restaurantes()
        fecha_actual = datetime.now()
        año = fecha_actual.year
        self.años = []
        for i in range(año,(año-30),-1):
            self.años.append(i)
        self.meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


        def limpiar_entrys():
            entry_matricula.delete(0, "end")
            entry_causa.delete(0, "end")
            entry_doc_pag.delete(0, "end")
            entry_doc_aj.delete(0, "end")

        matriz_datos = []
        def seleccionar():
            pdf_ruta = askopenfilename()
            nombre_pdf["text"] = str(pdf_ruta)
            if nombre_pdf.cget("text") != "":
                del matriz_datos[:]
                lista_imagenes = pdf2img.pdf2img(pdf_ruta)
                for ruta_img in lista_imagenes:
                    lista_datos = detectar_proveedor.proveedor(ruta_img)
                    matriz_datos.append(lista_datos)
                    limpiar_entrys()
                    entry_matricula.insert(0, str(lista_datos[0]))
                btn_analizar.config(state=NORMAL)
                entry_matricula.config(bg="green")
            else:
                nombre_pdf["text"] = "Ninguno"

        def abrir_ventana():
            w, top = create_editar(rt=self.ventana, matriz=matriz_datos[0])

        def analizar():
            if entry_matricula.get() == "":
                entry_matricula.config(bg="red")
            elif entry_causa.get() == "":
                entry_causa.config(bg="red")
            elif entry_doc_pag.get() == "":
                entry_doc_pag.config(bg="red")
            elif entry_doc_aj.get() == "":
                entry_doc_aj.config(bg="red")
            else:
                datos = analizar_datos.analisis(matriz_datos[0], entry_causa.get(), entry_doc_pag.get(), entry_doc_aj.get(),True)
                del matriz_datos[:]
                matriz_datos.append(datos)
                abrir_ventana()
            btn_guardar.config(state=NORMAL)

        def guardar():
            insert.insert(matriz_datos[0])
            btn_analizar.config(state=DISABLED)
            btn_guardar.config(state=DISABLED)

        def consultar():
            mes = cb_mes.get()
            for m in self.meses:
                if m == mes:
                    mes = self.meses.index(m) + 1
            resultado = select_restaurante.info_restaurante(mes,cb_restaurantes.get(),cb_años.get())
            llenar_excel.consulta(resultado)

        def consultar_año():
            resultado = select_restaurante.info_todo_año(cb_restaurantes.get(),cb_años.get())
            llenar_excel.consulta(resultado)

        def consultar_todo():
            resultado = select_restaurante.todo()
            llenar_excel.consulta(resultado)


        btn_seleccionar = Button(self.frame_seleccionar, text = "Seleccionar", fg="white", bg="#425070", font=self.fuente, width=25, height=2, command = seleccionar)
        nombre_pdf = Label(self.frame_ruta, text = "Ruta del archivo", bg="#D5DDF0")
        btn_analizar = Button(self.frame_ruta, text = "Analizar", fg="white", font=self.fuente, bg="#425070", width=25, height=2, state=DISABLED, command = analizar)
        lb_matricula = Label(self.frame_guardar, text="Matricula:")
        entry_matricula = Entry(self.frame_guardar)
        lb_causa = Label(self.frame_guardar, text="Causa:")
        entry_causa = Entry(self.frame_guardar)
        lb_doc_pag = Label(self.frame_guardar, text="Doc pag:")
        entry_doc_pag = Entry(self.frame_guardar)
        lb_doc_aj = Label(self.frame_guardar, text="Doc aj:")
        entry_doc_aj = Entry(self.frame_guardar)
        btn_guardar = Button(self.frame_guardar, text = "Guardar", fg="white", font=self.fuente, bg="#425070", width=25, height=2, state=DISABLED, command = guardar)
        lb_mes = Label(self.frame_consultas, text = "Mes: ", font=self.fuente, bg="#D5DDF0", width=20, height=2)
        cb_mes = ttk.Combobox(self.frame_consultas, font=self.fuente, width=20, value = self.meses)
        cb_mes.current(0)
        lb_restaurante = Label(self.frame_consultas, text = "Restaurante: ", font=self.fuente, bg="#D5DDF0", width=20, height=2)
        cb_restaurantes = ttk.Combobox(self.frame_consultas, font=self.fuente, width=20, value = self.restaurantes)
        cb_restaurantes.current(0)
        lb_año = Label(self.frame_consultas, text = "Año: ", bg="#D5DDF0", font=self.fuente, width=20, height=2)
        cb_años = ttk.Combobox(self.frame_consultas, font=self.fuente, width=20, value = self.años)
        cb_años.current(0)
        btn_consulta = Button(self.frame_consultas, text = "Consultar mes", fg="white", bg="#425070", font=self.fuente, width=20, height=2, command = consultar)
        btn_consulta_año = Button(self.frame_consultas, text = "Consultar año", fg="white", bg="#425070", font=self.fuente, width=20, height=2, command = consultar_año)
        btn_consulta_todo = Button(self.frame_consultas, text = "Consultar todo", fg="white", bg="#425070", font=self.fuente, width=20, height=2, command = consultar_todo)

        #pongo los widgets donde quiero
        btn_seleccionar.grid(row=0, column=0, padx=15, pady=10)
        nombre_pdf.grid(row=0, column=0, padx=15, pady=2)
        btn_analizar.grid(row=1, column=0, padx=0, pady=2)

        lb_matricula.grid(row=0, column=0, padx=0, pady=0, sticky="sw")
        entry_matricula.grid(row=1, column=0, padx=0, pady=0)
        lb_causa.grid(row=0, column=1, padx=0, pady=0, sticky="sw")
        entry_causa.grid(row=1, column=1, padx=0, pady=0)
        lb_doc_pag.grid(row=0, column=2, padx=0, pady=0, sticky="sw")
        entry_doc_pag.grid(row=1, column=2, padx=0, pady=0)
        lb_doc_aj.grid(row=0, column=3, padx=0, pady=0, sticky="sw")
        entry_doc_aj.grid(row=1, column=3, padx=0, pady=0)
        btn_guardar.grid(row=0, rowspan=2, column=4, padx=5, pady=0)
        lb_mes.grid(row=4, column=0, padx=15, pady=5)
        cb_mes.grid(row=5, column=0, padx=15, pady=5)
        lb_restaurante.grid(row=4, column=1, padx=15, pady=5)
        cb_restaurantes.grid(row=5, column=1, padx=15, pady=5)
        lb_año.grid(row=4, column=2, padx=15, pady=5)
        cb_años.grid(row=5, column=2, padx=15, pady=5)
        btn_consulta.grid(row=7, column=0, padx=15, pady=10)
        btn_consulta_año.grid(row=7, column=1, padx=15, pady=10)
        btn_consulta_todo.grid(row=7, column=2, padx=15, pady=10)

if __name__ == '__main__':
    root = Tk()
    Ventana(root)
    root.mainloop()