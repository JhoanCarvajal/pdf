# codigo para detectar quien es el provedor de energia 
import cv2
import pytesseract
import insert
import os
import ocr_eep

def proveedor(ruta):
    imagen = cv2.imread(ruta, 0)
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    roi_texto = image[4821:4821+661,1:1+1365]


    print("ROI texto")
    texto = pytesseract.image_to_string(roi_texto)
    texto = texto[:len(texto) - 2]
    print(texto)
    print("--------------------------------")

    palabras = texto.split()
    print(texto)

    if "www.eep.com.co" in palabras:
        ocr_eep.ocr_eep(ruta)
    else:
        print("no se reconoce el proveedor")
