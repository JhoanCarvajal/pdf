# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import os
import controlador
import ocr

def proveedor(self, ruta):
    try:
        #cargamos la imagen contenida en ruta
        imagen = cv2.imread(ruta, 0)
        #transformamos a escala de grises
        image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        bool_solo_negro = None
        rois = []
        lista_string_rois = controlador.regiones_interes_operadores(self.operador)
        print(lista_string_rois)
        for operador in lista_string_rois:
            lista = list(operador)

            info_roi = lista[2].split(",")
            info_roi = [int(i) for i in info_roi]
            x,y,w,h = info_roi
            rois.append(image[y:y+h,x:x+w])
            
            info_roi = lista[4].split(",")
            info_roi = [int(i) for i in info_roi]
            x,y,w,h = info_roi
            rois.append(image[y:y+h,x:x+w])
            
            info_roi = lista[6].split(",")
            info_roi = [int(i) for i in info_roi]
            x,y,w,h = info_roi
            rois.append(image[y:y+h,x:x+w])
            
            info_roi = lista[8].split(",")
            info_roi = [int(i) for i in info_roi]
            x,y,w,h = info_roi
            rois.append(image[y:y+h,x:x+w])

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
            #las ponemos todas en minusculas
            palabras = texto.lower() # [element.lower() for element in palabras]
            lista_palabras.append(palabras)
        # print(lista_palabras)

        #comparamos para determinar que proveedor es
        for i in range(len(lista_string_rois)):
            # print(lista_string_rois[i])
            cont = 0
            for p in range(len(lista_palabras)):
                # print(lista_palabras[p])
                if lista_string_rois[i][3] in lista_palabras[p]:
                    # print(lista_string_rois[i][3])
                    cont += 1
                elif lista_string_rois[i][5] in lista_palabras[p]:
                    # print(lista_string_rois[i][5])
                    cont += 1
                elif lista_string_rois[i][7] in lista_palabras[p]:
                    # print(lista_string_rois[i][7])
                    cont += 1
                elif lista_string_rois[i][9] in lista_palabras[p]:
                    # print(lista_string_rois[i][9])
                    cont += 1
            if cont == 4:
                self.operador = lista_string_rois[i][1]
                print(f"id del operadorrrrrr= {self.operador}")
                bool_solo_negro = lista_string_rois[i][10]
                print(f"bool solo negroooooo= {bool_solo_negro}")
                lista_datos = ocr.ocr(self.operador, ruta, bool_solo_negro)
            else:
                lista_datos = []
                os.remove(ruta)

        if lista_datos:
            return lista_datos
        else:
            return []
    except ValueError:
        pass
