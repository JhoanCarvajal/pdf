# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import insert
import os
import ocr_eep
import ocr_eep_escaner

def proveedor(ruta):
    try:
        #cargamos la imagen contenida en ruta
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #obtenemso el alto y ancho
        height, _ = image.shape
        #determinamos de donde sacar la informacion
        if height <= 5500:
            roi_texto = image[4821:4821+661,1:1+1365]
        else:
            #roi_texto = image[169:169+669,73:73+2265] era para la factura vertiacal de agua
            roi_texto = image[4821:4821+661,1:1+1365]

        #mostramos el roi de la informacion
        # cv2.imshow('ROI10', roi_texto)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        #leemos el texto del roi
        texto = pytesseract.image_to_string(roi_texto)
        texto = texto[:len(texto) - 2]

        #separamos el texto por palabras
        palabras = texto.split()
        #las ponemos todas en minusculas
        palabras = [element.lower() for element in palabras]
        #comparamos para determinar que proveedor es
        if "www.eep.com.co" in palabras:
            lista_datos = ocr_eep.ocr_eep(ruta)
        elif not palabras:
            lista_datos = ocr_eep_escaner.ocr_eep(ruta)
        else:
            lista_datos = []
            os.remove(ruta)
        return lista_datos
    except ValueError:
        pass
