import datetime
import validar_fechas
from retornar_501_551 import *
from validar_fechas import *

#funcion para convertir string ej 1,234,432 a numero
def numero_entero(dato):
    try:
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
    except ValueError:
        pass

def numero_decimal(dato):
    try:
        # preguntamos si existe un dato
        if dato:
            # string para almacenar los numeros
            numero = ""
            lista = dato.split(",")
            # cojemos la primera parte y la concatenamos con la ultima
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
                    # se ejecuta mientras la variable numero sea string
                    while isinstance(numero, str):
                        # le quitamos el ultimo digito o letra
                        numero = numero[:len(numero) - 1]
                        try:
                            # intentamos convertir a float
                            numero = float(numero)
                        except:
                            # por si no pudo convertir a float
                            if len(numero) <= 0:
                                try:
                                    numero = dato
                                    # quitamos la primera letra o digito
                                    numero = numero[1:len(numero)]
                                    numero = float(numero)
                                except:
                                    pass
            return numero
        else:
            numero = 0
    except ValueError:
        pass
    

def analisis(lista=[],causa=0,doc_pag=0,doc_aj=0,booleano=False):
    try:
        # Matricula de la factura
        matricula = numero_entero(lista[0])
        if matricula < 0:
            matricula *= -1
        # si existe viene del app.pyw
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
            doc_pag = int(doc_pag)
            doc_aj = int(doc_aj)
        # si no viene del archivo templates/datos/datos.py
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
            doc_pag = int(lista[5])
            doc_aj = int(lista[6])
            direccion = lista[13]
            
        paga = vr_paga - contribucion
        ajuste = paga - causa
        
        # creamos la lista que vamos a retornar
        datos = [matricula, fecha_inicial, fecha_final, causa, paga, ajuste, doc_pag, doc_aj, consumo_activa,\
            consumo_reactiva, kw, vr_kw, contribucion, alumbrado, vr_paga, direccion]

        # print("__________________________________________________________________________________________________________")
        # print("ESTOS SON LOS DATOS DESPUES DE MANDARLOS AL ANALISIS ESPERO Y ESTEN BIEN")
        # print(datos)
        # print("__________________________________________________________________________________________________________")

        return datos
    
    except ValueError:
        pass
