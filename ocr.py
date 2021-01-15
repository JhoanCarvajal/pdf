import cv2
import pytesseract
import os
from resaltar_color import *
import imutils
import numpy as np
import controlador

def ocr(id_operador, ruta):
    try:
        #imagen donde solo se ve el color negro
        # image = solo_negro(ruta)
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #lista de los rois
        lista_rois = []
        info_rois = controlador.regiones_interes_datos(id_operador)
        for string in info_rois:
            lista = list(string)
            for i in range(2, len(lista)):
                info_roi = lista[i].split(",")
                info_roi = [int(i) for i in info_roi]
                x,y,w,h = info_roi
                lista_rois.append(image[y:y+h,x:x+w])

        # #lista para guardar los datos 
        lista_datos = []

        i = 0
        #sacamos el texto de cada uno de los rois y lo agregamos a la lista
        for roi in lista_rois:
            if i > 7:
                dato = pytesseract.image_to_string(roi, config='--psm 6 -c \
                    tessedit_char_whitelist=$.,-0123456789')
            else:
                dato = pytesseract.image_to_string(roi)
            dato = dato[:len(dato) - 2]
            print(dato)
            lista_datos.append(dato)
            i += 1

        # recorremos la lista de rois para mostrarlos en una ventana
        for i in range(len(lista_rois)):
            cv2.imshow(f"ROI{i}", lista_rois[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("hasta aqui todo bien")

        #eliminanos la imagen contenida en la ruta
        os.remove(ruta)
        # retornamos la lista de datos
        return lista_datos
    except ValueError:
        #mostramos esto en caso de que ocurra un error
        print("ocr.py")