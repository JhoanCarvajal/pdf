import cv2
import pytesseract
import insert
import os
import numpy as np

def crear(y,y1,x,x1,ruta):
    imagen = cv2.imread(ruta, 0)
    
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    roi = image[y:y1,x:x1]

    return roi