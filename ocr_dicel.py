import cv2
import pytesseract
import os
from resaltar_color import *
import imutils

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
        lista_rois.append(image[239:239+75,2005:2005+515])#matricula
        lista_rois.append(image[693:693+45,2568:2568+319])#fechas de periodo de facturacion
        lista_rois.append(image[321:321+99,3164:3164+321])#valor a pagar
        lista_rois.append(image[1154:1154+49,1814:1814+457])#kw
        lista_rois.append(image[1853:1853+79,293:293+317])#valor de kw
        lista_rois.append(image[2606:2606+69,1617:1617+501])#alumbrado
        lista_rois.append(image[519:519+63,1855:1855+675])#direccion
        lista_rois.append(image[1092:1092+533,2279:2279+729])#cod de concepto empresa de energia
        lista_rois.append(image[1102:1102+535,3259:3259+401])#totales de los conceptos de la empresa de energia

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
                    tessedit_char_whitelist=.,-0123456789')
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
        print("Error en ocr_dicel.py")

