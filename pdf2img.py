import os
from pdf2image import convert_from_path
import detectar_proveedor
import datetime

def pdf2img(pdf):
    try:
        lista_imagenes = []
        ruta = os.path.split(pdf)
        carpeta = ruta[0]
        nombre_completo = ruta[1]
        nombre = os.path.splitext(nombre_completo)
        nombre = nombre[0]
        fecha = datetime.datetime.now()
        fecha = fecha.strftime("%H_%M_%S")
        paginas = convert_from_path(pdf, 500)
        cont = 1
        for pagina in paginas:
            pagina.save(f'{carpeta}/{nombre}{fecha}_{cont}.jpg', 'JPEG')
            lista_imagenes.append(f'{carpeta}/{nombre}{fecha}_{cont}.jpg')
            cont += 1
        return lista_imagenes
    except ValueError:
        pass