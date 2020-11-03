from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
import select_restaurante, traer_restaurantes, llenar_excel, pdf2img

import tkinter.font as tkFont

ventana = Tk()
ventana.title("prototipo facturación de frisby")
ventana.geometry("800x450")
ventana.resizable(0,0)
ventana.config(bg="#D5DDF0")

titulos = tkFont.Font(family="Arial", size=12, weight='bold')
fuente = tkFont.Font(family="Arial", size=11)

frame = Frame(ventana, bg="#D5DDF0")
frame.pack(fill=BOTH, expand=True, padx=30, pady=30)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

lb_facturas = Label(frame, text = "Seleccione la factura para guardarla en la base de datos", font=titulos, bg="#D5DDF0", anchor="e")
lb_facturas.pack()

frame_archivo = Frame(frame, bg="#9197A3")
frame_archivo.pack(fill=BOTH, expand=True)
frame_archivo.columnconfigure(1, weight=1)
frame_archivo.rowconfigure(1, weight=1)

frame_seleccionar = Frame(frame_archivo, bg="#9197A3")
frame_seleccionar.grid(row=0, column=0)

frame_ruta = Frame(frame_archivo, bg="#9197A3")
frame_ruta.grid(row=0, column=1)

frame_guardar = Frame(frame, bg="#D5DDF0")
frame_guardar.pack(fill=BOTH, expand=True)
frame_guardar.columnconfigure(1, weight=1)
frame_guardar.rowconfigure(1, weight=1)

lb_consultas = Label(frame, text = "Seleccione datos para hacer consultas", font=titulos, bg="#D5DDF0")
lb_consultas.pack()

frame_consultas = Frame(frame, bg="#9197A3")
frame_consultas.pack(fill=BOTH, expand=True)
frame_consultas.columnconfigure(1, weight=1)
frame_consultas.rowconfigure(1, weight=1)

restaurantes = traer_restaurantes.lista_restaurantes()
fecha_actual = datetime.now()
año = fecha_actual.year
años = []
for i in range(año,(año-30),-1):
    años.append(i)
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def seleccionar():
    pdf_ruta = askopenfilename()
    nombre_pdf["text"] = str(pdf_ruta)

def analizar():
    pdf_ruta = nombre_pdf["text"]
    if pdf2img.pdf2img(pdf_ruta):
        print("Todo ha ido bien")
    else:
        print("No funciono no se por que")

def cb_mes_click(event):
    pass

def cb_restaurantes_click(event):
    pass

def consultar():
    mes = cb_mes.get()
    for m in meses:
        if m == mes:
            mes = meses.index(m) + 1
    resultado = select_restaurante.info_restaurante(mes,cb_restaurantes.get(),cb_años.get())
    llenar_excel.consulta(resultado)

def consultar_año():
    resultado = select_restaurante.info_todo_año(cb_restaurantes.get(),cb_años.get())
    llenar_excel.consulta(resultado)

def consultar_todo():
    resultado = select_restaurante.todo()
    llenar_excel.consulta(resultado)


btn_seleccionar = Button(frame_seleccionar, text = "Seleccionar", fg="white", bg="#425070", font=fuente, width=25, height=2, command = seleccionar)
btn_seleccionar.grid(row=0, column=0, padx=15, pady=10)

nombre_pdf = Label(frame_ruta, text = "Ruta del archivo", font=fuente, bg="#D5DDF0")
nombre_pdf.grid(row=0, column=0, padx=15, pady=10)

btn_analizar = Button(frame_guardar, text = "Analizar y Guardar", fg="white", font=fuente, bg="#425070", width=25, height=2, command = analizar)
btn_analizar.pack(padx=15, pady=15)

lb_mes = Label(frame_consultas, text = "Mes: ", font=fuente, bg="#D5DDF0", width=20, height=2)
lb_mes.grid(row=4, column=0, padx=15, pady=5)

cb_mes = ttk.Combobox(frame_consultas, font=fuente, width=20, value = meses)
cb_mes.current(0)
cb_mes.grid(row=5, column=0, padx=15, pady=5)

lb_restaurante = Label(frame_consultas, text = "Restaurante: ", font=fuente, bg="#D5DDF0", width=20, height=2)
lb_restaurante.grid(row=4, column=1, padx=15, pady=5)

cb_restaurantes = ttk.Combobox(frame_consultas, font=fuente, width=20, value = restaurantes)
cb_restaurantes.current(0)
cb_restaurantes.grid(row=5, column=1, padx=15, pady=5)

lb_año = Label(frame_consultas, text = "Año: ", bg="#D5DDF0", font=fuente, width=20, height=2)
lb_año.grid(row=4, column=2, padx=15, pady=5)

cb_años = ttk.Combobox(frame_consultas, font=fuente, width=20, value = años)
cb_años.current(0)
cb_años.grid(row=5, column=2, padx=15, pady=5)

btn_consulta = Button(frame_consultas, text = "Consultar mes", fg="white", bg="#425070", font=fuente, width=20, height=2, command = consultar)
btn_consulta.grid(row=7, column=0, padx=15, pady=10)

btn_consulta_año = Button(frame_consultas, text = "Consultar año", fg="white", bg="#425070", font=fuente, width=20, height=2, command = consultar_año)
btn_consulta_año.grid(row=7, column=1, padx=15, pady=10)

btn_consulta_todo = Button(frame_consultas, text = "Consultar todo", fg="white", bg="#425070", font=fuente, width=20, height=2, command = consultar_todo)
btn_consulta_todo.grid(row=7, column=2, padx=15, pady=10)


ventana.mainloop()