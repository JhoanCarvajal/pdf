import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from . import datos_support
import analizar_datos
import insert

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Editar (root)
    datos_support.init(root, top)
    root.mainloop()

w = None
def create_editar(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_editar(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Editar (w, *args, **kwargs)
    datos_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_editar():
    global w
    w.destroy()
    w = None

class Editar:
    def __init__(self, top=None, *args, **kwargs):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("351x381+504+131")
        top.minsize(381, 351)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Datos")
        top.configure(background="#d9d9d9")

        # Frame
        self.contenedor = tk.Frame(top)
        self.contenedor.place(relx=0.0, rely=0.0, relheight=0.997, relwidth=1.0)
        self.contenedor.configure(relief='groove')
        self.contenedor.configure(borderwidth="2")
        self.contenedor.configure(relief="groove")
        self.contenedor.configure(background="#d9d9d9")

        # creación de widgets
        self.lb_matricula = tk.Label(self.contenedor)
        self.lb_matricula.place(relx=0.0, rely=0.026, height=20, width=100)
        self.lb_matricula.configure(anchor='w')
        self.lb_matricula.configure(background="#d9d9d9")
        self.lb_matricula.configure(disabledforeground="#a3a3a3")
        self.lb_matricula.configure(foreground="#000000")
        self.lb_matricula.configure(text='''Matricula''')

        self.lb_fecha_inicio = tk.Label(self.contenedor)
        self.lb_fecha_inicio.place(relx=0.0, rely=0.105, height=20, width=100)
        self.lb_fecha_inicio.configure(anchor='w')
        self.lb_fecha_inicio.configure(background="#d9d9d9")
        self.lb_fecha_inicio.configure(disabledforeground="#a3a3a3")
        self.lb_fecha_inicio.configure(foreground="#000000")
        self.lb_fecha_inicio.configure(text='''Fecha Inicio''')

        self.lb_fecha_final = tk.Label(self.contenedor)
        self.lb_fecha_final.place(relx=0.0, rely=0.184, height=20, width=100)
        self.lb_fecha_final.configure(anchor='w')
        self.lb_fecha_final.configure(background="#d9d9d9")
        self.lb_fecha_final.configure(disabledforeground="#a3a3a3")
        self.lb_fecha_final.configure(foreground="#000000")
        self.lb_fecha_final.configure(text='''Fecha Final''')

        self.lb_vr_paga = tk.Label(self.contenedor)
        self.lb_vr_paga.place(relx=0.0, rely=0.263, height=20, width=100)
        self.lb_vr_paga.configure(anchor='w')
        self.lb_vr_paga.configure(background="#d9d9d9")
        self.lb_vr_paga.configure(disabledforeground="#a3a3a3")
        self.lb_vr_paga.configure(foreground="#000000")
        self.lb_vr_paga.configure(text='''Valor a pagar''')

        self.lb_consumo_activa = tk.Label(self.contenedor)
        self.lb_consumo_activa.place(relx=0.0, rely=0.342, height=20, width=100)
        self.lb_consumo_activa.configure(anchor='w')
        self.lb_consumo_activa.configure(background="#d9d9d9")
        self.lb_consumo_activa.configure(disabledforeground="#a3a3a3")
        self.lb_consumo_activa.configure(foreground="#000000")
        self.lb_consumo_activa.configure(text='''Consumo activa''')

        self.lb_consumo_reactiva = tk.Label(self.contenedor)
        self.lb_consumo_reactiva.place(relx=0.0, rely=0.421, height=20
                , width=100)
        self.lb_consumo_reactiva.configure(anchor='w')
        self.lb_consumo_reactiva.configure(background="#d9d9d9")
        self.lb_consumo_reactiva.configure(disabledforeground="#a3a3a3")
        self.lb_consumo_reactiva.configure(foreground="#000000")
        self.lb_consumo_reactiva.configure(text='''Consumo reactiva''')

        self.lb_kw = tk.Label(self.contenedor)
        self.lb_kw.place(relx=0.0, rely=0.5, height=20, width=100)
        self.lb_kw.configure(anchor='w')
        self.lb_kw.configure(background="#d9d9d9")
        self.lb_kw.configure(disabledforeground="#a3a3a3")
        self.lb_kw.configure(foreground="#000000")
        self.lb_kw.configure(text='''Kw/h''')

        self.lb_vr_kw = tk.Label(self.contenedor)
        self.lb_vr_kw.place(relx=0.0, rely=0.579, height=20, width=100)
        self.lb_vr_kw.configure(anchor='w')
        self.lb_vr_kw.configure(background="#d9d9d9")
        self.lb_vr_kw.configure(disabledforeground="#a3a3a3")
        self.lb_vr_kw.configure(foreground="#000000")
        self.lb_vr_kw.configure(text='''Valor kw/h''')

        self.lb_contribucion = tk.Label(self.contenedor)
        self.lb_contribucion.place(relx=0.0, rely=0.658, height=20
                , width=100)
        self.lb_contribucion.configure(anchor='w')
        self.lb_contribucion.configure(background="#d9d9d9")
        self.lb_contribucion.configure(disabledforeground="#a3a3a3")
        self.lb_contribucion.configure(foreground="#000000")
        self.lb_contribucion.configure(text='''Contribucion''')

        self.lb_alumbrado = tk.Label(self.contenedor)
        self.lb_alumbrado.place(relx=0.0, rely=0.737, height=20, width=100)
        self.lb_alumbrado.configure(anchor='w')
        self.lb_alumbrado.configure(background="#d9d9d9")
        self.lb_alumbrado.configure(disabledforeground="#a3a3a3")
        self.lb_alumbrado.configure(foreground="#000000")
        self.lb_alumbrado.configure(text='''Alumbrado''')

        self.btn_enviar = tk.Button(self.contenedor, command=self.enviar_datos)
        self.btn_enviar.place(relx=0.249, rely=0.889, height=24, width=87)
        self.btn_enviar.configure(activebackground="#ececec")
        self.btn_enviar.configure(activeforeground="#000000")
        self.btn_enviar.configure(background="#d9d9d9")
        self.btn_enviar.configure(disabledforeground="#a3a3a3")
        self.btn_enviar.configure(foreground="#000000")
        self.btn_enviar.configure(highlightbackground="#d9d9d9")
        self.btn_enviar.configure(highlightcolor="black")
        self.btn_enviar.configure(pady="0")
        self.btn_enviar.configure(text='''Guardar''')

        self.entry_matricula = tk.Entry(self.contenedor)
        self.entry_matricula.place(relx=0.502, rely=0.026, height=20
                , relwidth=0.488)
        self.entry_matricula.configure(background="white")
        self.entry_matricula.configure(disabledforeground="#a3a3a3")
        self.entry_matricula.configure(font="TkFixedFont")
        self.entry_matricula.configure(foreground="#000000")
        self.entry_matricula.configure(insertbackground="black")

        self.entry_fecha_inicio = tk.Entry(self.contenedor)
        self.entry_fecha_inicio.place(relx=0.502, rely=0.105, height=20
                , relwidth=0.488)
        self.entry_fecha_inicio.configure(background="white")
        self.entry_fecha_inicio.configure(disabledforeground="#a3a3a3")
        self.entry_fecha_inicio.configure(font="TkFixedFont")
        self.entry_fecha_inicio.configure(foreground="#000000")
        self.entry_fecha_inicio.configure(highlightbackground="#d9d9d9")
        self.entry_fecha_inicio.configure(highlightcolor="black")
        self.entry_fecha_inicio.configure(insertbackground="black")
        self.entry_fecha_inicio.configure(selectbackground="blue")
        self.entry_fecha_inicio.configure(selectforeground="white")

        self.entry_fecha_final = tk.Entry(self.contenedor)
        self.entry_fecha_final.place(relx=0.502, rely=0.184, height=20
                , relwidth=0.488)
        self.entry_fecha_final.configure(background="white")
        self.entry_fecha_final.configure(disabledforeground="#a3a3a3")
        self.entry_fecha_final.configure(font="TkFixedFont")
        self.entry_fecha_final.configure(foreground="#000000")
        self.entry_fecha_final.configure(highlightbackground="#d9d9d9")
        self.entry_fecha_final.configure(highlightcolor="black")
        self.entry_fecha_final.configure(insertbackground="black")
        self.entry_fecha_final.configure(selectbackground="blue")
        self.entry_fecha_final.configure(selectforeground="white")

        self.entry_vr_pagar = tk.Entry(self.contenedor)
        self.entry_vr_pagar.place(relx=0.502, rely=0.263, height=20
                , relwidth=0.488)
        self.entry_vr_pagar.configure(background="white")
        self.entry_vr_pagar.configure(disabledforeground="#a3a3a3")
        self.entry_vr_pagar.configure(font="TkFixedFont")
        self.entry_vr_pagar.configure(foreground="#000000")
        self.entry_vr_pagar.configure(highlightbackground="#d9d9d9")
        self.entry_vr_pagar.configure(highlightcolor="black")
        self.entry_vr_pagar.configure(insertbackground="black")
        self.entry_vr_pagar.configure(selectbackground="blue")
        self.entry_vr_pagar.configure(selectforeground="white")

        self.entry_consumo_activa = tk.Entry(self.contenedor)
        self.entry_consumo_activa.place(relx=0.502, rely=0.342, height=20
                , relwidth=0.488)
        self.entry_consumo_activa.configure(background="white")
        self.entry_consumo_activa.configure(disabledforeground="#a3a3a3")
        self.entry_consumo_activa.configure(font="TkFixedFont")
        self.entry_consumo_activa.configure(foreground="#000000")
        self.entry_consumo_activa.configure(highlightbackground="#d9d9d9")
        self.entry_consumo_activa.configure(highlightcolor="black")
        self.entry_consumo_activa.configure(insertbackground="black")
        self.entry_consumo_activa.configure(selectbackground="blue")
        self.entry_consumo_activa.configure(selectforeground="white")

        self.entry_consumo_reactiva = tk.Entry(self.contenedor)
        self.entry_consumo_reactiva.place(relx=0.502, rely=0.421, height=20
                , relwidth=0.488)
        self.entry_consumo_reactiva.configure(background="white")
        self.entry_consumo_reactiva.configure(disabledforeground="#a3a3a3")
        self.entry_consumo_reactiva.configure(font="TkFixedFont")
        self.entry_consumo_reactiva.configure(foreground="#000000")
        self.entry_consumo_reactiva.configure(highlightbackground="#d9d9d9")
        self.entry_consumo_reactiva.configure(highlightcolor="black")
        self.entry_consumo_reactiva.configure(insertbackground="black")
        self.entry_consumo_reactiva.configure(selectbackground="blue")
        self.entry_consumo_reactiva.configure(selectforeground="white")

        self.entry_kw = tk.Entry(self.contenedor)
        self.entry_kw.place(relx=0.502, rely=0.5, height=20, relwidth=0.488)
        self.entry_kw.configure(background="white")
        self.entry_kw.configure(disabledforeground="#a3a3a3")
        self.entry_kw.configure(font="TkFixedFont")
        self.entry_kw.configure(foreground="#000000")
        self.entry_kw.configure(highlightbackground="#d9d9d9")
        self.entry_kw.configure(highlightcolor="black")
        self.entry_kw.configure(insertbackground="black")
        self.entry_kw.configure(selectbackground="blue")
        self.entry_kw.configure(selectforeground="white")

        self.entry_vr_kw = tk.Entry(self.contenedor)
        self.entry_vr_kw.place(relx=0.502, rely=0.579, height=20, relwidth=0.488)

        self.entry_vr_kw.configure(background="white")
        self.entry_vr_kw.configure(disabledforeground="#a3a3a3")
        self.entry_vr_kw.configure(font="TkFixedFont")
        self.entry_vr_kw.configure(foreground="#000000")
        self.entry_vr_kw.configure(highlightbackground="#d9d9d9")
        self.entry_vr_kw.configure(highlightcolor="black")
        self.entry_vr_kw.configure(insertbackground="black")
        self.entry_vr_kw.configure(selectbackground="blue")
        self.entry_vr_kw.configure(selectforeground="white")

        self.entry_contribucion = tk.Entry(self.contenedor)
        self.entry_contribucion.place(relx=0.502, rely=0.658, height=20
                , relwidth=0.488)
        self.entry_contribucion.configure(background="white")
        self.entry_contribucion.configure(disabledforeground="#a3a3a3")
        self.entry_contribucion.configure(font="TkFixedFont")
        self.entry_contribucion.configure(foreground="#000000")
        self.entry_contribucion.configure(highlightbackground="#d9d9d9")
        self.entry_contribucion.configure(highlightcolor="black")
        self.entry_contribucion.configure(insertbackground="black")
        self.entry_contribucion.configure(selectbackground="blue")
        self.entry_contribucion.configure(selectforeground="white")

        self.entry_alumbrado = tk.Entry(self.contenedor)
        self.entry_alumbrado.place(relx=0.502, rely=0.737, height=20
                , relwidth=0.488)
        self.entry_alumbrado.configure(background="white")
        self.entry_alumbrado.configure(disabledforeground="#a3a3a3")
        self.entry_alumbrado.configure(font="TkFixedFont")
        self.entry_alumbrado.configure(foreground="#000000")
        self.entry_alumbrado.configure(highlightbackground="#d9d9d9")
        self.entry_alumbrado.configure(highlightcolor="black")
        self.entry_alumbrado.configure(insertbackground="black")
        self.entry_alumbrado.configure(selectbackground="blue")
        self.entry_alumbrado.configure(selectforeground="white")

        # recuperamos la lista que viene en **kwargs
        self.lista_vieja = []
        for _, value in kwargs.items():
            self.lista_vieja = value

        #llenar los entrys con datos
        self.entry_matricula.insert(0, self.lista_vieja[0])
        self.entry_fecha_inicio.insert(0, self.lista_vieja[1])
        self.entry_fecha_final.insert(0, self.lista_vieja[2])
        self.entry_vr_pagar.insert(0, self.lista_vieja[14])
        self.entry_consumo_activa.insert(0, self.lista_vieja[8])
        self.entry_consumo_reactiva.insert(0, self.lista_vieja[9])
        self.entry_kw.insert(0, self.lista_vieja[10])
        self.entry_vr_kw.insert(0, self.lista_vieja[11])
        self.entry_contribucion.insert(0, self.lista_vieja[12])
        self.entry_alumbrado.insert(0, self.lista_vieja[13])

    def enviar_datos(self):
        self.lista = []
        self.lista.append(self.entry_matricula.get())
        self.lista.append(self.entry_fecha_inicio.get())
        self.lista.append(self.entry_fecha_final.get())
        self.lista.append(self.entry_vr_pagar.get())
        self.lista.append(self.lista_vieja[3])
        self.lista.append(self.lista_vieja[6])
        self.lista.append(self.lista_vieja[7])
        self.lista.append(self.entry_consumo_activa.get())
        self.lista.append(self.entry_consumo_reactiva.get())
        self.lista.append(self.entry_kw.get())
        self.lista.append(self.entry_vr_kw.get())
        self.lista.append(self.entry_contribucion.get())
        self.lista.append(self.entry_alumbrado.get())
        datos_buenos = analizar_datos.analisis(lista=self.lista)
        insert.insert(datos_buenos)
        datos_support.destroy_window()

if __name__ == '__main__':
    vp_start_gui()



