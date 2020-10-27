# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import insert
import os
import ocr_eep
import ocr_agua
import ocr_eep_escaner

def proveedor(ruta):
    imagen = cv2.imread(ruta, 0)
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    height, width = image.shape
    if height == 5500:
        roi_texto = image[4821:4821+661,1:1+1365]
    else: #height == 4250
        roi_texto = image[169:169+669,73:73+2265]

    cv2.imshow('ROI10', roi_texto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    texto = pytesseract.image_to_string(roi_texto)
    texto = texto[:len(texto) - 2]

    palabras = texto.split()
    palabras = [element.lower() for element in palabras]
    print(palabras)

    if "www.eep.com.co" in palabras:
        ocr_eep.ocr_eep(ruta)
    elif "efigas" in palabras:
        print("factura de efigas")
    elif "serviciudad" in palabras or "acueducto" in palabras:
        print("factura de agua")
        ocr_agua.ocr_agua(ruta)
    elif "henao" in palabras or "baena" in palabras:
        print("factura de energia de carlos")
        ocr_eep_escaner.ocr_eep(ruta)

    else:
        print("no se reconoce el proveedor")
        #os.remove(ruta)
