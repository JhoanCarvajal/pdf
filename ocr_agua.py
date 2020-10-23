import cv2
import pytesseract
import insert
import os
import numpy as np

def ocr_agua(ruta):
    imagen = cv2.imread(ruta, 0)
    
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    roi_inicial = image[1715:1715+103,592:592+400]
    roi_final = image[1715:1715+103,1009:1009+381]
    roi_causa = image[4017:4017+153,4809:4809+549]
    roi_consumo = image[1447:1447+99,1961:1961+405]
    roi_otros = image[861:861+61,4177:4177+305]
    roi_alumbrado = image[1178:1178+64,4185:4185+309]
    roi_kw = image[1629:1629+93,1985:1985+405]
    roi_vr_kw = image[909:909+77,3861:3861+317]
    roi_direccion = image[1161:1161+85,477:477+1057]
    roi_matricula = image[965:965+113,1909:1909+441]

    lista = []

    print("ROI1")
    inicial = pytesseract.image_to_string(roi_inicial)
    inicial = inicial[:len(inicial) - 2]
    lista.append(inicial)
    print(inicial)
    print("--------------------------------")
    print("ROI2")
    final = pytesseract.image_to_string(roi_final)
    final = final[:len(final) - 2]
    lista.append(final)
    print(final)
    print("--------------------------------")
    print("ROI3")
    causa = pytesseract.image_to_string(roi_causa)
    causa = causa[:len(causa) - 2]
    lista.append(causa)
    print(causa)
    print("--------------------------------")
    print("ROI4")
    consumo = pytesseract.image_to_string(roi_consumo)
    consumo = consumo[:len(consumo) - 2]
    lista.append(consumo)
    print(consumo)
    print("--------------------------------")
    print("ROI5")
    otros = pytesseract.image_to_string(roi_otros)
    otros = otros[:len(otros) - 2]
    lista.append(otros)
    print(otros)
    print("--------------------------------")
    print("ROI6")
    alumbrado = pytesseract.image_to_string(roi_alumbrado)
    alumbrado = alumbrado[:len(alumbrado) - 2]
    lista.append(alumbrado)
    print(alumbrado)
    print("--------------------------------")
    print("ROI7")
    kw = pytesseract.image_to_string(roi_kw)
    kw = kw[:len(kw) - 2]
    lista.append(kw)
    print(kw)
    print("--------------------------------")
    print("ROI8")
    vr_kw = pytesseract.image_to_string(roi_vr_kw)
    vr_kw = vr_kw[:len(vr_kw) - 2]
    lista.append(vr_kw)
    print(vr_kw)
    print("--------------------------------")
    print("ROI9")
    direccion = pytesseract.image_to_string(roi_direccion)
    direccion = direccion[:len(direccion) - 2]
    lista.append(direccion)
    print(direccion)
    print("--------------------------------")
    print("ROI10")
    matricula = pytesseract.image_to_string(roi_matricula)
    matricula = matricula[:len(matricula) - 2]
    lista.append(matricula)
    print(matricula)
    print("--------------------------------")

    cv2.imshow('ROI1', roi_inicial)
    cv2.imshow('ROI2', roi_final)
    cv2.imshow('ROI3', roi_causa)
    cv2.imshow('ROI4', roi_consumo)
    cv2.imshow('ROI5', roi_otros)
    cv2.imshow('ROI6', roi_alumbrado)
    cv2.imshow('ROI7', roi_kw)
    cv2.imshow('ROI8', roi_vr_kw)
    cv2.imshow('ROI9', roi_direccion)
    cv2.imshow('ROI10', roi_matricula)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #os.remove(ruta)
    insert.insert(lista)
