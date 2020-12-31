import datetime
import validar_fechas
from retornar_501_551 import *
from validar_fechas import *

#funcion para convertir string ej 1,234,432 a numero
def numero_entero(dato):
    try:
        if dato:
            if type(dato) == int or type(dato) == float:
                return dato
            else:
                # string para almacenar solo numeros
                numero = ""
                negativo = False
                for digito in dato:
                    # print(digito) #mostramos cada digito del string
                    if digito == "B":
                        digito = "8"
                    # si el digito es un numero lo concatenamos con la variable numero
                    if digito.isdigit():
                        numero += str(digito)
                    # si el digito es un - ó ~ el numero es negativo
                    elif digito == "-" or digito =="~":
                        negativo = True
                # convertimos el string a int
                numero = int(numero)
                # miramos si es negativo y lo convertimos
                if negativo:
                    numero *= -1
                return numero
        else:
            return 0
    except ValueError:
        pass
    

def analisis(lista=[], booleano=False):
    try:
        # Matricula de la factura
        if type(lista[0]) == str:
            matricula = numero_entero(lista[0])
            if matricula < 0:
                matricula *= -1
        else:
            matricula = lista[0]
        # si existe viene del ventana_principal.py
        if booleano:
            fecha_inicial, fecha_final = validar_fecha(lista[1])
            vr_paga = numero_entero(lista[2])
            kw = numero_entero(lista[3])
            alumbrado = numero_entero(lista[4])
            direccion = lista[5]
            consumo_activa, consumo_reactiva, contribucion = retornar_totales(lista[6], lista[7])
            consumo_activa = numero_entero(consumo_activa)
            consumo_reactiva = numero_entero(consumo_reactiva)
            contribucion = numero_entero(contribucion)
            causa = 0
            doc_pag = None
            doc_aj = None
            paga = vr_paga - contribucion
        # si no viene del archivo templates/datos/datos.py
        else:
            fecha_inicial = lista[1]
            fecha_final = lista[2]
            causa = int(lista[3])
            paga = numero_entero(lista[4])
            kw = numero_entero(lista[9])
            alumbrado = numero_entero(lista[11])
            consumo_activa = numero_entero(lista[7])
            consumo_reactiva = numero_entero(lista[8])
            contribucion = numero_entero(lista[10])
            doc_pag = lista[5]
            doc_aj = lista[6]
            direccion = lista[12]
            vr_paga = paga + contribucion
            
        ajuste = paga - causa
        vr_kw = consumo_activa / kw
        
        # creamos la lista que vamos a retornar
        datos = [matricula, fecha_inicial, fecha_final, causa, paga, ajuste, doc_pag, doc_aj, consumo_activa,\
            consumo_reactiva, kw, vr_kw, contribucion, alumbrado, vr_paga, direccion]

        return datos
    except ValueError:
        return None
