import cv2
import pytesseract
import os
from resaltar_color import *
import imutils
import numpy as np

def ocr(ruta):
    try:
        #imagen donde solo se ve el color negro
        # image = solo_negro(ruta)
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #lista de los rois
        lista_rois = []

        #agregamos cada roi(region de interes) a nuestra lista
        lista_rois.append(image[49:49+129,4889:4889+837])#matricula
        lista_rois.append(image[209:209+73,4871:4871+864])#fechas de periodo de facturacion
        lista_rois.append(image[505:505+147,4868:4868+859])#valor a pagar
        lista_rois.append(image[2401:2401+77,5785:5785+571])#kw
        # lista_rois.append(image[1853:1853+79,293:293+317])#valor de kw
        lista_rois.append(image[1427:1427+78,3439:3439+398])#alumbrado
        lista_rois.append(image[1147:1147+61,4161:4161+1341])#direccion
        lista_rois.append(image[1517:1517+593,3913:3913+695])#cod de concepto empresa de energia
        lista_rois.append(image[1517:1517+375,5609:5609+779])#totales de los conceptos de la empresa de energia

        #redimensionamos los que no se leen bien
        # lista_rois[7] = imutils.resize(lista_rois[7], width=600)
        # lista_rois[8] = imutils.resize(lista_rois[8], width=600)

        #lista para guardar los datos 
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

        #eliminanos la imagen contenida en la ruta
        os.remove(ruta)
        # retornamos la lista de datos
        return lista_datos
    except ValueError:
        #mostramos esto en caso de que ocurra un error
        print("Error en ocr_chec.py")