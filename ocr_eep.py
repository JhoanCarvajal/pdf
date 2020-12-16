import cv2
import pytesseract
import os
from resaltar_color import *
import imutils

def ocr_eep(ruta):
    try:
        #imagen donde solo se ve el color negro
        image = solo_negro(ruta)

        #lista de los rois
        lista_rois = []

        #agregamos cada roi(region de interes) a nuestra lista
        lista_rois.append(image[142:142+76,3173:3173+966])#matricula
        lista_rois.append(image[1745:1745+88,413:413+590])#fechas de periodo de facturacion
        lista_rois.append(image[685:685+81,3795:3795+315])#valor a pagar
        lista_rois.append(image[1555:1555+75,2051:2051+337])#kw
        lista_rois.append(image[1853:1853+79,293:293+317])#valor de kw
        lista_rois.append(image[1227:1227+57,3854:3854+268])#alumbrado
        lista_rois.append(image[340:340+96,300:300+1628])#direccion
        lista_rois.append(image[3898:3898+600,375:375+125])#cod de concepto empresa de energia
        lista_rois.append(image[3898:3898+600,2033:2033+280])#totales de los conceptos de la empresa de energia

        #redimensionamos los que no se leen bien
        # lista_rois[7] = imutils.resize(lista_rois[7], width=600)
        # lista_rois[8] = imutils.resize(lista_rois[8], width=600)

        #lista para guardar los datos 
        lista_datos = []

        i = 0
        #sacamos el texto de cada uno de los rois y lo agregamos a la lista
        for roi in lista_rois:
            if i > 6:
                dato = pytesseract.image_to_string(roi, config='--psm 6 -c \
                    tessedit_char_whitelist=.,-0123456789')
            else:
                dato = pytesseract.image_to_string(roi)
            dato = dato[:len(dato) - 2]
            print(dato)
            lista_datos.append(dato)
            i += 1

        # recorremos la lista de rois para mostrarlos en una ventana
        # for i in range(len(lista_rois)):
        #     cv2.imshow(f"ROI{i}", lista_rois[i])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        #eliminanos la imagen contenida en la ruta
        os.remove(ruta)
        # retornamos la lista de datos
        return lista_datos
    except ValueError:
        #mostramos esto en caso de que ocurra un error
        print("Error en ocr_eep.py")

