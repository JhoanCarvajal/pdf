import cv2
import pytesseract
import os
from resaltar_color import *
import imutils
import alinear

def ocr_epm(ruta):
    try:
        #imagen donde solo se ve el color negro
        # image = solo_negro(ruta)
        #esto es supuestamente para alinear la imagen pero no me da
        # img_alineada = alinear.alinear(ruta)

        imagen = cv2.imread(ruta, 0)

        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        image = cv2.fastNlMeansDenoising(image,None,10,7,21)

        #lista de los rois
        lista_rois = []

        #agregamos cada roi(region de interes) a nuestra lista
        lista_rois.append(image[1039:1039+75,797:797+467])#matricula
        lista_rois.append(image[1040:1040+77,1287:1287+656])#fechas de periodo de facturacion
        lista_rois.append(image[2199:2199+69,3789:3789+397])#valor a pagar
        lista_rois.append(image[1123:1123+82,2142:2142+214])#kw
        # lista_rois.append(image[1853:1853+79,293:293+317])#valor de kw
        lista_rois.append(image[4007:4007+67,937:937+451])#alumbrado
        lista_rois.append(image[611:611+88,2929:2929+664])#direccion
        lista_rois.append(image[1462:1462+182,182:182+532])#cod de concepto empresa de energia
        lista_rois.append(image[1471:1471+168,1167:1167+328])#totales de los conceptos de la empresa de energia

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

