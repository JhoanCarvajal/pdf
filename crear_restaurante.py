import tkinter as tk
from tkinter import simpledialog

def nombre_restaurante():
    root = tk.Toplevel()
    root.withdraw()
    nombre = simpledialog.askstring("Nuevo Restaurante", "Nombre del restaurante:")
    return nombre
