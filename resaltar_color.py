import cv2
import numpy as np
import imutils
rojoBajo1 = np.array([0, 0, 0], np.uint8)
rojoAlto1 = np.array([0, 0, 14], np.uint8)
# Leer la imagen
image = cv2.imread('imagenes/carro.jpg')
image = imutils.resize(image, width=640)
# Pasamos las imágenes de BGR a: GRAY (esta a BGR nuevamente) y a HSV
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Detectamos el color rojo
maskRojo1 = cv2.inRange(imageHSV, rojoBajo1, rojoAlto1)
#mask = cv2.add(maskRojo1)
mask = cv2.medianBlur(maskRojo1, 7)
redDetected = cv2.bitwise_and(image,image,mask=mask)
# Fondo en grises
invMask = cv2.bitwise_not(mask)
bgGray = cv2.bitwise_and(imageGray,imageGray,mask=invMask)
# Sumamos bgGray y redDetected
finalImage = cv2.add(bgGray,redDetected)
# Visualización
cv2.imshow('Image',image)
cv2.imshow('finalImage', finalImage)
cv2.imshow('soloNegro', invMask)

cv2.waitKey(0)
cv2.destroyAllWindows()