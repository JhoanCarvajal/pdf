# Importar los paquetes necesarios
import numpy as np
import cv2

def alinear(ruta):
    # Cargar la imagen inicial del disco
    imageName = ruta
    image = cv2.imread(imageName)

    # Tratar de remover "ruido"
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

    # Convertir la imagen a escala de grises, e invertir los
    # colores de fondo y frente para asegurar que el frente
    # sea "blanco" y el fondo "negro"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    
    # Limitar la imagen, estableciendo todos los píxeles del
    # frente a 255 (blanco total), y los de fondo a 0 (negro total)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Crear máscara para rellenar colores.
    # Nótese que el tamaño debe ser 2 píxeles más grande que el de la imagen.
    h, w = thresh.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    print("[INFO] Contour rectangle: {h}, {w}".format(h=h, w=w))

    # Rellenar bordes externos con color negro
    cv2.floodFill(thresh, mask, (0,0), 0)
    cv2.floodFill(thresh, mask, (0,h-1), 0)
    cv2.floodFill(thresh, mask, (w-1,0), 0)
    cv2.floodFill(thresh, mask, (w-1,h-1), 0)

    # Tratar de remover "ruido" otra vez
    # thresh = cv2.fastNlMeansDenoising(thresh)

    #cv2.imwrite("step1.png",thresh)

    # Tomar las coordenadas (x, y) de todos los píxeles
    # con valores mayores o iguales a cero, y usarlas para
    # calcular una caja rotada que delimite todas las
    # coordenadas
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]

    # Mostrar el ángulo de corrección "crudo"
    print("[INFO] Raw angle: {:.3f}".format(angle))

    # La función `cv2.minAreaRect` retorna valores en el rango
    # [-90, 0]; como el rectángulo rota en el sentido de las
    # agujas del reloj, el ángulo obtenido tiende a cero. En
    # este caso especial debemos sumar 90 grados al ángulo.
    if angle < -45:
        angle = -(90 + angle)
    
    # De lo contrario, solo basta tomar el inverso del ángulo
    # para hacerlo positivo
    else:
        angle = -angle

    # Rotar la imagen para alinearla
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Mostrar el ángulo de corrección final
    print("[INFO] Angle: {:.3f}".format(angle))

    
    cv2.imwrite(ruta,rotated)

    return rotated
