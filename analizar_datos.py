import datetime
import validar_fechas
from retornar_501_551 import *
from validar_fechas import *

def numero_entero(dato):
    try:
        numero = ""
        negativo = False
        for digito in dato:
            print(digito)
            if digito == "B":
                digito = "8"
            if digito.isdigit():
                numero += str(digito)
            elif digito == "-" or digito =="~":
                negativo = True
        numero = int(numero)
        if negativo:
            numero *= -1
        return numero
    except ValueError:
        print("hubo un error al combertir a numero")

def numero_decimal(dato):
    try:
        if dato:
            numero = ""
            lista = dato.split(",")
            if len(lista) > 2:
                for digito in lista[0]:
                    if digito.isdigit():
                        numero += str(digito)
                numero += "." + lista[-1]
            else:
                try:
                    numero = float(dato)
                except:
                    numero = dato
                    while isinstance(numero, str):
                        numero = numero[:len(numero) - 1]
                        try:
                            numero = float(numero)
                        except ValueError:
                            try:
                                numero = dato
                                numero = numero[1:len(numero)]
                                numero = float(numero)
                            except:
                                numero = None
            return numero
        else:
            numero = None
            print("No hay un numero para combertir a decimal")
    except ValueError:
        print("Hubo un error innesperado al convertir numero a decimal")
    

def analisis(lista,causa,doc_pag,doc_aj):
    try:
        matricula = numero_entero(lista[0])
        if matricula < 0:
            matricula *= -1
        fecha_inicial, fecha_final = validar_fecha(lista[1])
        vr_paga = numero_entero(lista[2])
        kw = numero_entero(lista[3])
        vr_kw = numero_decimal(lista[4])
        alumbrado = numero_entero(lista[5])
        direccion = lista[6]
        consumo, contribuciones = retornar_totales(lista[7], lista[8])

        consumo = numero_entero(consumo)
        contribuciones = numero_entero(contribuciones)

        causa = int(causa)
        paga = vr_paga - contribuciones
        ajuste = paga - causa
        doc_pag = int(doc_pag)
        doc_aj = int(doc_aj)

        datos = [matricula, fecha_inicial, fecha_final, causa, paga, ajuste, doc_pag, doc_aj, consumo, kw, vr_kw, contribuciones,alumbrado]

        print("__________________________________________________________________________________________________________")
        print("ESTOS SON LOS DATOS DESPUES DE MANDARLOS AL ANALISIS ESPERO Y ESTEN BIEN")
        print(datos)
        print("__________________________________________________________________________________________________________")

        return datos
    
    except ValueError:
        print("error en el analisis")