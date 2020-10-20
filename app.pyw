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
ventana.geometry("960x520")


frame = Frame(ventana, width=960, height=520)
frame.pack()

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
    
btn_seleccionar = Button(frame, text = "Seleccionar", command = seleccionar)
btn_seleccionar.grid(row=1,column=1)

nombre_pdf = Label(frame, text = "Seleccione una factura en pdf")
nombre_pdf.grid(row=1, column=3)

btn_analizar = Button(frame, text = "Analizar", command = analizar)
btn_analizar.grid(row=2,column=2)

btn_consulta = Button(frame, text = "Consultar", command = consultar)
btn_consulta.grid(row=4,column=0)

btn_consulta_año = Button(frame, text = "Consultar todo el año", command = consultar_año)
btn_consulta_año.grid(row=4,column=1)

lb_mes = Label(frame, text = "Mes: ")
lb_mes.grid(row=3, column=0)

cb_mes = ttk.Combobox(frame, value = meses)
cb_mes.current(0)
#cb_mes.bind("<<ComboboxSelected>>", cb_mes_click)
cb_mes.grid(row=3, column=1)

lb_restaurante = Label(frame, text = "Restaurante: ")
lb_restaurante.grid(row=3, column=2)

cb_restaurantes = ttk.Combobox(frame, value = restaurantes)
cb_restaurantes.current(0)
cb_restaurantes.grid(row=3, column=3)

lb_año = Label(frame, text = "Año: ")
lb_año.grid(row=3, column=4)

cb_años = ttk.Combobox(frame, value = años)
cb_años.current(0)
cb_años.grid(row=3, column=5)


ventana.mainloop()