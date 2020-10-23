import cv2
import pytesseract
import insert
import os
import numpy as np

def ocr_agua(ruta):
    imagen = cv2.imread(ruta, 0)
    
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    roi_inicial = image[1765:1765+41,533:533+230]
    roi_final = image[1767:1767+41,780:780+220]
    
    cv2.imshow('ROI10', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ocr_agua('C:/Users/Jhoan/Documents/tecnoparque/pdf/imagenes/agua.jpg')
