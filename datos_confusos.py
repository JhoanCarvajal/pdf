from tkinter import *
from tkinter import ttk

def pedir_info(mensaje):
    def quit():
        ventana.destroy()

    ventana = Tk()
    lb_mensaje = Label(ventana, text=mensaje)
    dato_por_usuario = Entry(ventana)
    btn_aceptar = Button(ventana, text = "Aceptar", command = quit)
    lb_mensaje.pack()
    dato_por_usuario.pack()
    btn_aceptar.pack()
    return dato_por_usuario.get()

    ventana.mainloop()

    