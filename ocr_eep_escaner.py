import cv2
import pytesseract
import os
import resaltar_color
import imutils


def ocr(ruta):
    #imagen donde solo se ve el color negro
    image = resaltar_color.solo_negro(ruta)
    # image = cv2.imread(ruta, 1) #Si se quiere usar la imagen original

    #lista de los rois
    lista_rois = []

    #agregamos cada roi(region de interes) a nuestra lista
    lista_rois.append(image[120:120+162,3096:3096+1114])#matricula
    lista_rois.append(image[1766:1766+123,405:405+798])#fechas de periodo de facturacion
    lista_rois.append(image[710:710+148,3454:3454+735])#valor a pagar
    lista_rois.append(image[1566:1566+146,2000:2000+383])#kw
    lista_rois.append(image[1877:1877+115,295:295+711])#valor de kw
    lista_rois.append(image[1219:1219+155,3815:3815+273])#alumbrado
    lista_rois.append(image[379:379+139,269:269+1719])#direccion
    lista_rois.append(image[3963:3963+600,297:297+163])#cod de concepto empresa de energia
    lista_rois.append(image[3963:3963+600,1937:1937+425])#totales de los conceptos de la empresa de energia

    #redimensionamos los que no se leen bien 
    lista_rois[1] = imutils.resize(lista_rois[1], width=800)
    #lista_rois[7] = imutils.resize(lista_rois[7], width=800)
    #lista_rois[8] = imutils.resize(lista_rois[8], width=800)


    #lista para guardar los datos 
    lista_datos = []

    #sacamos el texto de cada uno de los rois y lo agregamos a la lista
    i = 0
    for roi in lista_rois:
        if i > 6:
            dato = pytesseract.image_to_string(roi, config='--psm 6 -c \
                tessedit_char_whitelist=.,-0123456789')
        else:
            dato = pytesseract.image_to_string(roi)
        dato = dato[:len(dato) - 2]
        print(dato)
        lista_datos.append(dato)
        i += 1

    # recorremos la lista de rois para mostrarlos en una ventana
    for i in range(len(lista_rois)):
        cv2.imshow(f"ROI{i}", lista_rois[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #eliminanos la imagen contenida en la ruta
    os.remove(ruta)
    # retornamos la lista de datos
    return lista_datos


