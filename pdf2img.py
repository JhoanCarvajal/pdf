import os
from pdf2image import convert_from_path
import detectar_proveedor
def pdf2img(pdf):
    try:
        ruta = os.path.split(pdf)
        carpeta = ruta[0]
        nombre_completo = ruta[1]
        nombre = os.path.splitext(nombre_completo)
        nombre = nombre[0]
        print(carpeta, nombre)
        paginas = convert_from_path(pdf, 500)
        for pagina in paginas:
            pagina.save(f'{carpeta}/{nombre}.jpg', 'JPEG')
        if detectar_proveedor.proveedor(f'{carpeta}/{nombre}.jpg'):
            return True
        else:
            return False
    except ValueError:
        print("Error en pdf2img")
        return False