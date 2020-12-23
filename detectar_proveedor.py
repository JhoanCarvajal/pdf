# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import os
import ocr_eep
import ocr_eep_escaner

def proveedor(ruta):
    try:
        #cargamos la imagen contenida en ruta
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        rois = [image[1032:1032+649,8:8+114], #eep pdf
        image[86:86+698,3469:3469+244], #eep escaner
        image[417:417+941,197:197+737], # dicel
        image[2829:2829+1405,1:1+1033], #epm
        image[221:221+3221,2123:2123+845], # enel
        image[37:37+1881,905:905+381]] # chec


        #obtenemso el alto y ancho
        height, _ = image.shape
        #determinamos de donde sacar la informacion
        # if height <= 5500:
        #     roi_texto = image[4821:4821+661,1:1+1365]
        # else:
        #     #roi_texto = image[169:169+669,73:73+2265] era para la factura vertiacal de agua
        #     roi_texto = image[4821:4821+661,1:1+1365]

        #mostramos el roi de la informacion
        cv2.imshow('ROI10', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        lista_palabras = []
        #leemos el texto del roi
        for roi in rois:
            texto = pytesseract.image_to_string(roi)
            texto = texto[:len(texto) - 2]
            #separamos el texto por palabras
            palabras = texto.split()
            #las ponemos todas en minusculas
            palabras = [element.lower() for element in palabras]
            lista_palabras.append(palabras)
        print(lista_palabras)
        #comparamos para determinar que proveedor es
        if "web-www.eep.com.co" in lista_palabras:
            lista_datos = ocr_eep.ocr_eep(ruta)
            print("## EEP ##")
        elif "empresa" in lista_palabras and "de" in lista_palabras and "energia" in lista_palabras and "pereira" in lista_palabras:
            print("## EEP Scaner")
        elif "www.dicel.com.co" in lista_palabras:
            lista_datos = []
            print("## DICEL ##")
        elif not lista_palabras or 'eep.com.co' in lista_palabras:
            lista_datos = ocr_eep_escaner.ocr_eep(ruta)
        else:
            lista_datos = []
            # os.remove(ruta)
        return lista_datos
    except ValueError:
        pass
