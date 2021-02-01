# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import os
import controlador
import ocr
import imutils

def proveedor(self, ruta):
    try:
        #cargamos la imagen contenida en ruta
        rhh = cv2.imread(ruta)
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        canny = cv2.Canny(image, 100, 200)
        canny = cv2.dilate(canny, None, iterations=1)

        contornos, h = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contornos:
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            if area > 10000:
                print(area)
                cv2.drawContours(rhh, [c], 0, (0,255,0), 3)

        img_resize = imutils.resize(rhh, width=600)
        print("contornos =", len(contornos))
        # for i in range(len(contornos)):
        #     cv2.drawContours(img_resize, contornos, i, (0,255,0), 3)
        #     cv2.imshow("imagen", img_resize)
        #     cv2.waitKey(0)

        bool_solo_negro = None
        rois = []
        lista_string_rois = controlador.regiones_interes_operadores()
        for string in lista_string_rois:
            lista = list(string)
            info_roi = lista[1].split(",")
            info_roi = [int(i) for i in info_roi]
            x,y,w,h = info_roi
            rois.append(image[y:y+h,x:x+w])

        i = 1
        for roi in rois:
            titulo = str(i)
            cv2.imshow(titulo, roi)
            i+=1
        cv2.imshow("resize", img_resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        lista_palabras = []
        #leemos el texto del roi
        for roi in rois:
            texto = pytesseract.image_to_string(roi)
            texto = texto[:len(texto) - 2]
            #las ponemos todas en minusculas
            palabras = texto.lower() # [element.lower() for element in palabras]
            lista_palabras.append(palabras)
        print(lista_palabras)
        #comparamos para determinar que proveedor es
        for i in range(len(lista_string_rois)):
            if lista_string_rois[i][2] in lista_palabras[i]:
                print(lista_string_rois[i][2])
                self.proveedor = lista_string_rois[i][0]
                bool_solo_negro = lista_string_rois[i][3]
                break
        lista_datos = ocr.ocr(self.proveedor, ruta, bool_solo_negro)
        
        if lista_datos:
            return lista_datos
        else:
            return []
    except ValueError:
        pass
