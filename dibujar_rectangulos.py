import cv2
import numpy as np
def dibujar(img):
    imagen = img
    #Dibujando un rectangulo
    cv2.rectangle(imagen,(120,120+162),(3096,3096+1114),(0,255,0),1)
    cv2.rectangle(imagen,(1766,1766+123),(405,405+798),(0,255,0),1)
    cv2.rectangle(imagen,(710,710+148),(3454,3454+735),(0,255,0),1)
    cv2.rectangle(imagen,(1566,1566+146),(2000,2000+383),(0,255,0),1)
    cv2.rectangle(imagen,(1877,1877+115),(295,295+711),(0,255,0),1)
    cv2.rectangle(imagen,(1219,1219+155),(3815,3815+273),(0,255,0),1)
    cv2.rectangle(imagen,(379,379+139),(269,269+1719),(0,255,0),1)
    cv2.rectangle(imagen,(3963,3963+600),(297,297+163),(0,255,0),1)
    cv2.rectangle(imagen,(3963,3963+600),(1937,1937+425),(0,255,0),1)
    cv2.imwrite('Grises.png',imagen)