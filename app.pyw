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
ventana.geometry()#"960x520"

# frame = Frame(ventana, width=960, height=520, bg="purple")
# frame.pack_propagate(False)
# frame.pack()
# frame_archivo = Frame(frame, width=960, height=100, bg="green")
# frame_archivo.pack_propagate(False)
# frame_archivo.pack()
# frame_seleccionar = Frame(frame_archivo, width=380, height=100, bg="orange")
# frame_seleccionar.grid_propagate(False)
# frame_seleccionar.grid(row=0, column=0)
# frame_ruta = Frame(frame_archivo, width=580, height=100, bg="red")
# frame_ruta.grid_propagate(False)
# frame_ruta.grid(row=0, column=1)
# frame_guardar = Frame(frame, width=960, height=100, bg="blue")
# frame_guardar.pack_propagate(False)
# frame_guardar.pack()
# frame_consultas = Frame(frame, width=960, height=320, bg="yellow")
# frame_consultas.pack_propagate(False)
# frame_consultas.pack()

restaurantes = traer_restaurantes.lista_restaurantes()
fecha_actual = datetime.now()
año = fecha_actual.year
años = []
for i in range(año,(año-30),-1):
    años.append(i)
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
#meses = [1,2,3,4,5,6,7,8,9,10,11,12]
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


btn_seleccionar = Button(ventana, text = "Seleccionar", bg="red", command = seleccionar)
btn_seleccionar.grid(row=0, column=0)

nombre_pdf = Label(ventana, text = "Seleccione una factura en pdf")
nombre_pdf.grid(row=0, column=1)

btn_analizar = Button(ventana, text = "Analizar", command = analizar)
btn_analizar.grid(row=2, column=0)

lb_mes = Label(ventana, text = "Mes: ")
lb_mes.grid(row=4, column=0)

cb_mes = ttk.Combobox(ventana, value = meses)
cb_mes.current(0)
cb_mes.grid(row=5, column=0)

lb_restaurante = Label(ventana, text = "Restaurante: ")
lb_restaurante.grid(row=4, column=1)

cb_restaurantes = ttk.Combobox(ventana, value = restaurantes)
cb_restaurantes.current(0)
cb_restaurantes.grid(row=5, column=1)

lb_año = Label(ventana, text = "Año: ")
lb_año.grid(row=4, column=2)

cb_años = ttk.Combobox(ventana, value = años)
cb_años.current(0)
cb_años.grid(row=5, column=2)

btn_consulta = Button(ventana, text = "Consultar mes", command = consultar)
btn_consulta.grid(row=7, column=0)

btn_consulta_año = Button(ventana, text = "Consultar año", command = consultar_año)
btn_consulta_año.grid(row=7, column=1)

ventana.mainloop()