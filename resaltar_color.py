import cv2
import numpy as np
import imutils
from PIL import Image

def solo_negro(ruta):
    negro_bajo = np.array([0, 0, 0], np.uint8)
    negro_alto = np.array([179, 255, 110], np.uint8)
    # Leer la imagen
    image = cv2.imread(ruta)
    # Pasamos las imágenes de BGR a: GRAY (esta a BGR nuevamente) y a HSV
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Detectamos el color negro
    mask_negro = cv2.inRange(imageHSV, negro_bajo, negro_alto)
    #mask = cv2.add(mask_negro)
    #mask = cv2.medianBlur(mask_negro, 3)
    # Fondo en grises
    invMask = cv2.bitwise_not(mask_negro)
    #por si la quiero guardar
    cv2.imwrite('Grises.png',invMask)
    return invMask