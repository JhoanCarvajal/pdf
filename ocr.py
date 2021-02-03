import cv2
import pytesseract
import os
from resaltar_color import *
import imutils
import numpy as np
import controlador

def ocr(id_operador, ruta, bool_solo_negro):
    try:
        print(bool_solo_negro)
        if bool_solo_negro == True:
            print("solo negro")
            # imagen donde solo se ve el color negro
            image = solo_negro(ruta)
        else:
            print("normal")
            imagen = cv2.imread(ruta, 0)
            # transformamos a escala de grises
            image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        info_rois = controlador.regiones_interes_datos(id_operador)
        #lista de los rois
        lista_rois = []
        for string in info_rois:
            lista = list(string)
            for i in range(2, len(lista)):
                if ";" in lista[i]:
                    print(lista[i])
                    lista_i = []
                    rois = lista[i].split(";")
                    for roi in rois:
                        info_roi = roi.split(",")
                        info_roi = [int(i) for i in info_roi]
                        x,y,w,h = info_roi
                        lista_i.append(image[y:y+h,x:x+w])
                    lista_rois.append(lista_i)
                else:
                    info_roi = lista[i].split(",")
                    info_roi = [int(i) for i in info_roi]
                    x,y,w,h = info_roi
                    lista_rois.append(image[y:y+h,x:x+w])

        # #lista para guardar los datos 
        lista_datos = []

        i = 0
        #sacamos el texto de cada uno de los rois y lo agregamos a la lista
        for roi in lista_rois:
            if i > 6:
                if type(roi) == list:
                    dato = ""
                    for r in roi:
                        d = pytesseract.image_to_string(r, config='--psm 6 -c \
                            tessedit_char_whitelist=$.,-0123456789')
                        dato += d[:len(d) - 1]
                else:
                    dato = pytesseract.image_to_string(roi, config='--psm 6 -c \
                        tessedit_char_whitelist=$.,-0123456789')
                    dato = dato[:len(dato) - 2]
            else:
                if type(roi) == list:
                    dato = ""
                    for r in roi:
                        d = pytesseract.image_to_string(r)
                        dato += d[:len(d) - 1]
                else:
                    dato = pytesseract.image_to_string(roi)
                    dato = dato[:len(dato) - 2]
            print(dato)
            lista_datos.append(dato)
            i += 1

        # recorremos la lista de rois para mostrarlos en una ventana
        for i in range(len(lista_rois)):
            if type(lista_rois[i]) == list:
                for r in range(len(lista_rois[i])):
                    cv2.imshow(f"ROI{i}{r}", lista_rois[i][r])
            else:
                cv2.imshow(f"ROI{i}", lista_rois[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #eliminanos la imagen contenida en la ruta
        os.remove(ruta)
        # retornamos la lista de datos
        return lista_datos
    except ValueError:
        #mostramos esto en caso de que ocurra un error
        print("ocr.py")