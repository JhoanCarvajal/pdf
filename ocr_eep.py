import cv2
import pytesseract
import insert
import os
from resaltar_color import *

def ocr_eep(ruta):
    try:
        #imagen donde solo se ve el color negro
        image = solo_negro(ruta)

        #lista de los rois
        lista_rois = []

        #agregamos cada roi(region de interes) a nuestra lista
        lista_rois.append(image[1765:1765+41,533:533+230])#fehca inicial
        lista_rois.append(image[1767:1767+41,780:780+220])#fecha final
        lista_rois.append(image[685:685+81,3795:3795+315])#totol a pagar
        lista_rois.append(image[3903:3903+52,1527:1527+292])#consumo
        lista_rois.append(image[3942:3942+53,1534:1534+285])#otros
        lista_rois.append(image[381:381+101,3689:3689+477])#alumbrado
        lista_rois.append(image[1555:1555+75,2051:2051+337])#kw
        lista_rois.append(image[1853:1853+79,293:293+317])#valor de kw
        lista_rois.append(image[340:340+96,300:300+1628])#direccion
        lista_rois.append(image[142:142+76,3173:3173+966])#matricula

        #lista para guardar los datos 
        lista_datos = []

        #sacamos el texto de cada uno de los rois y lo agregamos a la lista
        for roi in lista_rois:
            dato = pytesseract.image_to_string(roi)
            dato = dato[:len(dato) - 2]
            lista_datos.append(dato)
            print(dato)
            print("--------------------------------")

        #recorremos la lista de rois para mostrarlos en una ventana
        for i in range(len(lista_rois)):
            cv2.imshow(f"ROI{i}", lista_rois[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #eliminanos la imagen contenida en la ruta
        os.remove(ruta)
        # llamamos la funcion insert
        if insert.insert(lista_datos):
            return True
        else:
            return False
    except ValueError:
        #mostramos esto en caso de que ocurra un error
        print("Error en ocr_eep.py")
        return False

