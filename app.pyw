from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
import traer_restaurantes
from datetime import date
from datetime import datetime
import select_restaurante
import llenar_excel
import pdf2img

ventana = Tk()
ventana.geometry("800x450")
ventana.resizable(0,0)
ventana.config(bg="#FFF5E0")


frame = Frame(ventana)
frame.pack(fill=BOTH, expand=True, padx=60, pady=60)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

frame_archivo = Frame(frame, bg="#FFF5E0")
frame_archivo.pack(fill=BOTH, expand=True)
frame_archivo.columnconfigure(1, weight=1)
frame_archivo.rowconfigure(1, weight=1)

frame_seleccionar = Frame(frame_archivo, bg="#FFF5E0")
frame_seleccionar.grid(row=0, column=0)
# frame_seleccionar.columnconfigure(1, weight=1)
# frame_seleccionar.rowconfigure(1, weight=1)

frame_ruta = Frame(frame_archivo, bg="#FFF5E0")
frame_ruta.grid(row=0, column=1)
# frame_ruta.columnconfigure(1, weight=1)
# frame_ruta.rowconfigure(1, weight=1)

frame_guardar = Frame(frame, bg="#FFEDC7")
frame_guardar.pack(fill=BOTH, expand=True)
frame_guardar.columnconfigure(1, weight=1)
frame_guardar.rowconfigure(1, weight=1)

frame_consultas = Frame(frame, bg="#FFE5AD")
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
    pdf2img.pdf2img(pdf_ruta)

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
    llenar_excel.cosulta(resultado)

def consultar_año():
    resultado = select_restaurante.info_todo_año(cb_restaurantes.get(),cb_años.get())
    llenar_excel.cosulta(resultado)


btn_seleccionar = Button(frame_seleccionar, text = "Seleccionar", bg="#AEFFAD", width=25, height=2, command = seleccionar)
btn_seleccionar.grid(row=0, column=0, padx=15, pady=10)

nombre_pdf = Label(frame_ruta, text = "Seleccione una factura en pdf", bg="#BAD3FF")
nombre_pdf.grid(row=0, column=0, padx=15, pady=10)

btn_analizar = Button(frame_guardar, text = "Analizar", bg="#AEFFAD", width=25, height=2, command = analizar)
btn_analizar.pack(padx=15, pady=15)

lb_mes = Label(frame_consultas, text = "Mes: ", bg="#BAD3FF", width=25, height=2)
lb_mes.grid(row=4, column=0, padx=15, pady=5)

cb_mes = ttk.Combobox(frame_consultas, width=25, height=2, value = meses)
cb_mes.current(0)
cb_mes.grid(row=5, column=0, padx=15, pady=5)

lb_restaurante = Label(frame_consultas, text = "Restaurante: ", bg="#BAD3FF", width=25, height=2)
lb_restaurante.grid(row=4, column=1, padx=15, pady=5)

cb_restaurantes = ttk.Combobox(frame_consultas, width=25, value = restaurantes)
cb_restaurantes.current(0)
cb_restaurantes.grid(row=5, column=1, padx=15, pady=5)

lb_año = Label(frame_consultas, text = "Año: ", bg="#BAD3FF", width=25, height=2)
lb_año.grid(row=4, column=2, padx=15, pady=5)

cb_años = ttk.Combobox(frame_consultas, width=25, height=2, value = años)
cb_años.current(0)
cb_años.grid(row=5, column=2, padx=15, pady=5)

btn_consulta = Button(frame_consultas, text = "Consultar mes", bg="#AEFFAD", width=25, height=2, command = consultar)
btn_consulta.grid(row=7, column=0, padx=15, pady=10, sticky=W)

btn_consulta_año = Button(frame_consultas, text = "Consultar año", bg="#AEFFAD", width=25, height=2, command = consultar_año)
btn_consulta_año.grid(row=7, column=1, padx=15, pady=10, sticky=W)


ventana.mainloop()