import cv2
import pytesseract
import insert
import os
import resaltar_color
from funciones.recortar_roi import *
from funciones.dividir_roi import *
from funciones.crear_roi import *
from validar_fechas import *


def ocr_eep(ruta):
    image = resaltar_color.solo_negro(ruta)

    imagen = cv2.imread(ruta, 0)
    img_grises = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    roi_fechas = image[1766:1766+123,405:405+798]
    roi_seg_fecha = image[1815:1815+63,728:728+232]
    roi_causa = image[710:710+148,3454:3454+735]
    roi_consumo_otros = image[3963:3963+448,1451:1451+495]
    roi_alumbrado = image[278:278+441,3583:3583+505]
    roi_kw = image[2133:2133+150,435:435+371]
    roi_vr_kw = image[1877:1877+115,295:295+711]
    roi_direccion = image[379:379+139,269:269+1719]
    roi_matricula = image[120:120+162,3096:3096+1114]

    rows,cols = roi_fechas.shape
    roi_fechas_nuevo = recortar(rows,cols,roi_fechas)
    fecha_inicio, fecha_final = dividir(roi_fechas_nuevo)

    print("ROI fechas")
    fechas = pytesseract.image_to_string(roi_fechas)
    fechas = fechas[:len(fechas) - 2]
    print(fechas)
    print("--------------------------------")
    print("ROI nuevo fechas")
    nuevo_fechas = pytesseract.image_to_string(roi_fechas_nuevo)
    nuevo_fechas = nuevo_fechas[:len(nuevo_fechas) - 2]
    print(nuevo_fechas)
    print("--------------------------------")

    print("roi fecha inicio")
    inicio = pytesseract.image_to_string(fecha_inicio)
    inicio = inicio[:len(inicio) - 2]
    print(inicio)
    print("--------------------------------")
    print("roi fecha final")
    final = pytesseract.image_to_string(fecha_final)
    final = final[:len(final) - 2]
    print(final)
    print("--------------------------------")

    fecha1,fecha2 = validar_fecha(inicio,final)
    print("555555555555555555555555555555555555555555555")
    print(fecha1, fecha2)

    # print("ROI segunda fecha")
    # segunda_fecha = pytesseract.image_to_string(roi_seg_fecha)
    # segunda_fecha = segunda_fecha[:len(segunda_fecha) - 2]
    # print(segunda_fecha)
    # print("--------------------------------")
    # print("ROI causa")
    # causa = pytesseract.image_to_string(roi_causa, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    # causa = causa[:len(causa) - 2]
    # print(causa)
    # print("--------------------------------")
    # print("ROI consumo y otros")
    # consumo = pytesseract.image_to_string(roi_consumo_otros)
    # consumo = consumo[:len(consumo) - 2]
    # print(consumo)
    # print("--------------------------------")
    # print("ROI alumbrado")
    # alumbrado = pytesseract.image_to_string(roi_alumbrado)
    # alumbrado = alumbrado[:len(alumbrado) - 2]
    # print(alumbrado)
    # print("--------------------------------")
    # print("ROI kw")
    # kw = pytesseract.image_to_string(roi_kw, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    # kw = kw[:len(kw) - 2]
    # print(kw)
    # print("--------------------------------")
    # print("ROI valor kw")
    # vr_kw = pytesseract.image_to_string(roi_vr_kw)
    # if "tarifaria" in vr_kw.lower():
    #     vr_kw = vr_kw[:len(vr_kw) - 15]
    # else:
    #     vr_kw = vr_kw[:len(vr_kw) - 2]
    # print(vr_kw)
    # print("--------------------------------")
    # print("ROI direccion")
    # direccion = pytesseract.image_to_string(roi_direccion)
    # direccion = direccion[:len(direccion) - 2]
    # print(direccion)
    # print("--------------------------------")
    # print("ROI matricula")
    # matricula = pytesseract.image_to_string(roi_matricula)
    # matricula = matricula[:len(matricula) - 2]
    # print(matricula)
    # print("--------------------------------")

    cv2.imshow('ROI1', roi_fechas)
    cv2.imshow('ROIadif', roi_fechas_nuevo)
    cv2.imshow('roi_fecha_inicio', fecha_inicio)
    cv2.imshow('roi_fecha_final', fecha_final)
    # cv2.imshow('ROIsegundafecha', roi_seg_fecha)
    # cv2.imshow('ROI3', roi_causa)
    # cv2.imshow('ROI4', roi_consumo_otros)
    # cv2.imshow('ROI6', roi_alumbrado)
    # cv2.imshow('ROI7', roi_kw)
    # cv2.imshow('ROI8', roi_vr_kw)
    # cv2.imshow('ROI9', roi_direccion)
    # cv2.imshow('ROI10', roi_matricula)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #os.remove(ruta)
    #insert.insert(lista)

