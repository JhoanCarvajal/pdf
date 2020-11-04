import cv2
import pytesseract
import insert
import os
import resaltar_color
from funciones.recortar_roi import *
from funciones.dividir_roi import *
from funciones.crear_roi import *
from validar_fechas import *
import imutils
import datos_confusos


def ocr_eep(ruta):
    image = resaltar_color.solo_negro(ruta)

    roi_matricula = image[120:120+162,3096:3096+1114]
    roi_fechas = image[1766:1766+123,405:405+798]
    roi_fechas = imutils.resize(roi_fechas, width=800)
    roi_valor_pagar = image[710:710+148,3454:3454+735]
    roi_consumo_otros = image[3963:3963+408,1937:1937+425]
    roi_kw = image[2133:2133+150,435:435+371]
    roi_vr_kw = image[1877:1877+115,295:295+711]
    roi_alumbrado = image[1219:1219+155,3815:3815+273]
    roi_direccion = image[379:379+139,269:269+1719]

    #lista para guardar los datos 
    lista_datos = []


    print("ROI matricula")
    matricula = pytesseract.image_to_string(roi_matricula)
    matricula = matricula[:len(matricula) - 2]
    lista_datos.append(matricula)
    print(matricula)
    print("--------------------------------")

    print("ROI fechas")
    fechas = pytesseract.image_to_string(roi_fechas)
    fechas = fechas[:len(fechas) - 2]
    print(fechas)
    print("--------------------------------")
    nuevas_fechas = validar_fecha(fechas)
    lista_datos.append(nuevas_fechas[0])
    lista_datos.append(nuevas_fechas[1])

    print("ROI valor_pagar")
    valor_pagar = pytesseract.image_to_string(roi_valor_pagar)
    valor_pagar = valor_pagar[:len(valor_pagar) - 2]
    lista_datos.append(valor_pagar)
    print(valor_pagar)
    print("--------------------------------")

    print("ROI consumo y otros")
    consumo = pytesseract.image_to_string(roi_consumo_otros)
    consumo = consumo[:len(consumo) - 2]
    consumo = consumo.split("\n")
    for i in range(len(consumo)):
        if consumo[i] == "":
            consumo.pop(i)
    lista_datos.append(consumo[0])
    print(consumo)
    print("--------------------------------")
    
    print("ROI kw")
    kw = pytesseract.image_to_string(roi_kw)
    kw = kw[:len(kw) - 2]
    lista_datos.append(kw)
    print(kw)
    print("--------------------------------")
    
    print("ROI valor kw")
    vr_kw = pytesseract.image_to_string(roi_vr_kw)
    if "tarifaria" in vr_kw.lower():
        vr_kw = vr_kw[:len(vr_kw) - 15]
    else:
        vr_kw = vr_kw[:len(vr_kw) - 2]
    lista_datos.append(vr_kw)
    print(vr_kw)
    print("--------------------------------")

    #informacion de otros que hace referencia a las contribuciones
    lista_datos.append(consumo[1])

    print("ROI alumbrado")
    alumbrado = pytesseract.image_to_string(roi_alumbrado)
    alumbrado = alumbrado[:len(alumbrado) - 2]
    lista_datos.append(alumbrado)
    print(alumbrado)
    print("--------------------------------")
    
    print("ROI direccion")
    direccion = pytesseract.image_to_string(roi_direccion)
    direccion = direccion[:len(direccion) - 2]
    lista_datos.append(direccion)
    print(direccion)
    print("--------------------------------")

    cv2.imshow('ROI10', roi_matricula)
    cv2.imshow('ROI1', roi_fechas)
    cv2.imshow('ROI3', roi_valor_pagar)
    cv2.imshow('ROI4', roi_consumo_otros)
    cv2.imshow('ROI7', roi_kw)
    cv2.imshow('ROI8', roi_vr_kw)
    cv2.imshow('ROI6', roi_alumbrado)
    cv2.imshow('ROI9', roi_direccion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"lista: {lista_datos}")

    os.remove(ruta)
    return lista_datos

