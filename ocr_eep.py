import cv2
import pytesseract
import insert
import os

def ocr_eep(ruta):
    imagen = cv2.imread(ruta, 0)
    image = 255 - cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    roi_inicial = image[1765:1765+41,533:533+230]
    roi_final = image[1767:1767+41,780:780+220]
    roi_causa = image[695:695+71,3805:3805+305]
    roi_consumo = image[3913:3913+42,1537:1537+282]
    roi_otros = image[3952:3952+43,1534:1534+285]
    roi_alumbrado = image[381:381+101,3689:3689+477]
    roi_kw = image[1555:1555+75,2051:2051+337]
    roi_vr_kw = image[1853:1853+79,293:293+317]
    roi_direccion = image[340:340+96,300:300+1628]
    roi_matricula = image[142:142+76,3173:3173+966]

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

