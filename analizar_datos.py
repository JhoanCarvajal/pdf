import datetime
import validar_fechas
from retornar_501_551 import *
from validar_fechas import *

#funcion para convertir string ej 1,234,432 a numero
def numero_decimal(dato):
    numero = 0
    if "." in dato and "," in dato:
        puntos = dato.count(".")
        comas = dato.count(",")
        if puntos > comas:
            # "4.523.256,56234"
            dato = dato.replace(',', '\n')
            dato = dato.replace('.', '')
            dato = dato.replace('\n', '.')
            numero = float(dato)
            numero = round(numero, 2)
        elif puntos == comas:
            print("###################### punto == comas")
            cantidad = len(dato)
            lista = list(dato)
            print(cantidad)
            decimal = False
            for i in range(cantidad-1, -1, -1):
                print(lista)
                if decimal == True and (dato[i] == "," or dato[i] == "."):
                    lista[i] = ""
                if decimal == False and (dato[i] == "," or dato[i] == "."):
                    lista[i] = "."
                    decimal = True
            separador = ""
            dato = separador.join(lista)
            print(dato)
            numero = float(dato)
            numero = round(numero, 2)
            print(numero)
        else:
            # "4,523,256.56234"
            dato = dato.replace(',', '')
            numero = float(dato)
            numero = round(numero, 2)
    elif "." in dato:
        # "1.234.234"
        puntos = dato.count(".")
        if puntos == 1:
            datos = dato.split(".")
            contador = 0
            for i in datos[1]:
                contador += 1
            if contador == 3:
                numero = dato.replace('.','')
                numero = float(numero)
            else:
                numero = float(dato)
        else:
            dato = dato.replace('.', '')
            numero = float(dato)
            numero = round(numero, 2)
    elif "," in dato:
        # "1,234,567"
        comas = dato.count(",")
        if comas == 1:
            datos = dato.split(",")
            contador = 0
            for i in datos[1]:
                contador += 1
            if contador == 3:
                numero = dato.replace(',','')
                numero = float(numero)
            else:
                numero = dato.replace(',','.')
                numero = float(numero)
        else:
            dato = dato.replace(',', '')
            numero = float(dato)
            numero = round(numero, 2)
    return numero

def numero_entero(dato):
    try:
        if dato:
            if type(dato) == int or type(dato) == float:
                return dato
            else:
                try:
                    numero = float(dato)
                    numero = round(numero, 2)
                    return numero
                except ValueError:
                    try:
                        numero = numero_decimal(dato)
                        return numero
                    except ValueError:
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
                            elif digito == "." or digito == ",":
                                numero += str(digito)
                        # convertimos el string a float
                        numero = numero_decimal(numero)
                        # miramos si es negativo y lo convertimos
                        if negativo:
                            numero *= -1
                        return numero
        else:
            return 0
    except ValueError:
        pass   

def analisis(proveedor, lista=[], booleano=False):
    try:
        print(lista)
        # Matricula de la factura
        # if type(lista[0]) == str:
        #     matricula = numero_entero(lista[0])
        #     matricula = int(matricula)
        #     if matricula < 0:
        #         matricula *= -1
        # else:
        matricula = lista[0]
        # si existe viene del ventana_principal.py
        if booleano:
            fecha_inicial, fecha_final = validar_fecha(proveedor, lista[1])
            vr_paga = numero_entero(lista[2])
            kw = numero_entero(lista[3])
            alumbrado = numero_entero(lista[4])
            direccion = lista[5]
            consumo_activa, consumo_reactiva, contribucion, contribucion_reactiva = retornar_totales(proveedor, lista[6], lista[7])
            consumo_activa = numero_entero(consumo_activa)
            consumo_reactiva = numero_entero(consumo_reactiva)
            contribucion = numero_entero(contribucion)
            contribucion_reactiva = numero_entero(contribucion_reactiva)
            causa = 0
            doc_pag = None
            doc_aj = None
            paga = vr_paga - contribucion
        # si no viene del archivo templates/datos/datos.py
        else:
            fecha_inicial = lista[1]
            fecha_final = lista[2]
            causa = int(lista[3])
            paga = float(lista[4])
            kw = float(lista[9])
            alumbrado = float(lista[12])
            consumo_activa = float(lista[7])
            consumo_reactiva = float(lista[8])
            contribucion = float(lista[10])
            contribucion_reactiva = float(lista[11])
            doc_pag = lista[5]
            doc_aj = lista[6]
            direccion = lista[13]
            vr_paga = paga + contribucion
            
        ajuste = paga - causa
        if consumo_activa != 0 and kw:
            vr_kw = consumo_activa / kw
        else:
            vr_kw = 0
        
        # creamos la lista que vamos a retornar
        datos = [matricula, fecha_inicial, fecha_final, causa, paga, ajuste, doc_pag, doc_aj, consumo_activa,\
            consumo_reactiva, kw, vr_kw, contribucion, contribucion_reactiva, alumbrado, vr_paga, direccion]

        print(datos)

        return datos
    except ValueError:
        return None
