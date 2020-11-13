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
    print("############################### NUMERO DECIMAL ##########################")
    print(dato)
    print("#########################################################################")
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
                        print(numero)
                        print("_____________________________________________________________")
                        try:
                            numero = float(numero)
                        except:
                            if len(numero) <= 0:
                                try:
                                    numero = dato
                                    numero = numero[1:len(numero)]
                                    numero = float(numero)
                                except:
                                    print(numero)
            return numero
        else:
            numero = 0
            print("No hay un numero para combertir a decimal")
    except ValueError:
        print("Hubo un error innesperado al convertir numero a decimal")
    

def analisis(lista=[],causa=0,doc_pag=0,doc_aj=0,booleano=False):
    try:
        matricula = numero_entero(lista[0])
        if matricula < 0:
            matricula *= -1
        if booleano:
            fecha_inicial, fecha_final = validar_fecha(lista[1])
            vr_paga = numero_entero(lista[2])
            kw = numero_entero(lista[3])
            vr_kw = numero_decimal(lista[4])
            alumbrado = numero_entero(lista[5])
            direccion = lista[6]
            consumo_activa, consumo_reactiva, contribucion = retornar_totales(lista[7], lista[8])

            consumo_activa = numero_entero(consumo_activa)
            consumo_reactiva = numero_entero(consumo_reactiva)
            contribucion = numero_entero(contribucion)

            causa = int(causa)
            paga = vr_paga - contribucion
            ajuste = paga - causa
            doc_pag = int(doc_pag)
            doc_aj = int(doc_aj)
        else:
            fecha_inicial = lista[1]
            fecha_final = lista[2]
            vr_paga = numero_entero(lista[3])
            kw = numero_entero(lista[9])
            vr_kw = numero_decimal(lista[10])
            alumbrado = numero_entero(lista[12])

            consumo_activa = numero_entero(lista[7])
            consumo_reactiva = numero_entero(lista[8])
            contribucion = numero_entero(lista[11])

            causa = int(lista[4])
            paga = vr_paga - contribucion
            ajuste = paga - causa
            doc_pag = int(lista[5])
            doc_aj = int(lista[6])
            
        datos = [matricula, fecha_inicial, fecha_final, causa, paga, ajuste, doc_pag, doc_aj, consumo_activa,\
            consumo_reactiva, kw, vr_kw, contribucion, alumbrado, vr_paga]

        print("__________________________________________________________________________________________________________")
        print("ESTOS SON LOS DATOS DESPUES DE MANDARLOS AL ANALISIS ESPERO Y ESTEN BIEN")
        print(datos)
        print("__________________________________________________________________________________________________________")

        return datos
    
    except ValueError:
        print("error en el analisis")
