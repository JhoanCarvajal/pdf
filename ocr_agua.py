import cv2
import pytesseract
import insert
import os
def rotateImage(image, angle):
     image_center = tuple(np.array(image.shape[1::-1]) / 2)
     rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
     result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
     return result

def ocr_agua(ruta):
    imagen = cv2.imread(ruta, 0)
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    image = rotateImage(image, 90)
    
    cv2.imshow('ROI10', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
