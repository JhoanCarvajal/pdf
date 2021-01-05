# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import os
import ocr_eep
import ocr_eep_escaner
import ocr_dicel
import ocr_epm
import ocr_enel
import ocr_chec

def proveedor(self, ruta):
    try:
        #cargamos la imagen contenida en ruta
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        rois = [image[8:8+114,1032:1032+649], #eep pdf
        image[3400:3400+300,86:86+698], #eep escaner
        image[197:197+737,417:417+941], # dicel
        image[5:5+1033,2829:2829+1405], #epm
        image[2123:2123+845,221:221+3221], # enel
        image[905:905+381,37:37+1881]] # chec


        #obtenemso el alto y ancho
        height, _ = image.shape
        #determinamos de donde sacar la informacion
        # if height <= 5500:
        #     roi_texto = image[4821:4821+661,1:1+1365]
        # else:
        #     #roi_texto = image[169:169+669,73:73+2265] era para la factura vertiacal de agua
        #     roi_texto = image[4821:4821+661,1:1+1365]

        #mostramos el roi de la informacion
        i = 1
        for roi in rois:
            titulo = str(i)
            cv2.imshow(titulo, roi)
            i+=1
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        lista_palabras = []
        #leemos el texto del roi
        for roi in rois:
            texto = pytesseract.image_to_string(roi)
            texto = texto[:len(texto) - 2]
            #separamos el texto por palabras
            # palabras = texto.split()
            #las ponemos todas en minusculas
            palabras = texto.lower() # [element.lower() for element in palabras]
            lista_palabras.append(palabras)
        print(lista_palabras)
        #comparamos para determinar que proveedor es
        if "web-www.eep.com.co" in lista_palabras[0]:
            print("## EEP ##")
            self.proveedor = "eep"
            lista_datos = ocr_eep.ocr(ruta)
        elif "empresa de energia de pereira" in lista_palabras[1] or "lnergia de pereira" in lista_palabras[1]:
            print("## EEP Scaner")
            self.proveedor = "eep_escaner"
            lista_datos = ocr_eep_escaner.ocr(ruta)
        elif "www.dicel.com.co" in lista_palabras[2] or "dicel" in lista_palabras[2] or "dicel." in lista_palabras[2] or "diel" in lista_palabras[2] or "deel.com" in lista_palabras[2]:
            print("## DICEL ##")
            self.proveedor = "dicel"
            lista_datos = ocr_dicel.ocr(ruta)
        elif "contrato" in lista_palabras[3]:
            print("## EPM ##")
            self.proveedor = "epm"
            lista_datos = ocr_epm.ocr_epm(ruta)
        elif "enel-codensa" in lista_palabras[4]:
            print("## ENEL ##")
            lista_datos = ocr_enel.ocr(ruta)
        elif "chec" in lista_palabras[5]:
            print("## CHEC ##")
            lista_datos = ocr_chec.ocr(ruta)
        else:
            lista_datos = []
            # os.remove(ruta)
        return lista_datos
    except ValueError:
        pass
