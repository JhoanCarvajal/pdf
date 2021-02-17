import datetime
import controlador

# si hay una letra en el dia ej I5 
def letra_a_numero(dato):
    try:
        dato = dato.lower()
        dato_corregido = ""
        # si hay una letra la convertimos al numero que mas se parece
        for d in range(len(dato)):
            r = dato[d]
            if r == "o":
                r = "0"
            if r == "i":
                r = "1"
            if r == "g":
                r = "6"
            if r == "s":
                r = "5"
            if r == "b":
                r = "8"
            if r == "q":
                r = "0"
            if r == ",":
                r = ""
            dato_corregido += r
        return dato_corregido
    except ValueError:
        pass

# mes FEB = 2 
def mes_letra_a_numero(dato):
    try:
        #lista de meses
        meses = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
        mes=dato.lower()
        # por si el mes tiene punto al final
        if len(mes) == 4:
            mes = mes[:len(mes) - 1]
        # por si el mes tiene un 0 lo pasamos a una "o"
        mes_corregido = ""
        for letra in mes:
            if letra == "0":
                letra = "o"
            mes_corregido += letra
        # identificamos si el mes esta en la lista de meses
        for m in meses:
            if m == mes_corregido:
                # sacamos el numero del mes
                mes_corregido = meses.index(m) + 1
        return mes_corregido
    except ValueError:
        pass

def r(proveedor, fechas):
    lista_datos = controlador.validar_fechas(proveedor)
    if lista_datos:
        print(lista_datos)
        print(fechas)
        if lista_datos[2]:
            fechas = fechas.replace(lista_datos[2], lista_datos[3])
        print(fechas)
        fechas = fechas.split(lista_datos[3])

        for i in range(len(fechas)):
            fechas[i] = fechas[i].strip()

        dia_inicio = letra_a_numero(fechas[lista_datos[4]])
        dia_final = letra_a_numero(fechas[lista_datos[5]])
        
        try:
            mes_inicio = int(fechas[lista_datos[6]])
        except ValueError:
            mes_inicio = mes_letra_a_numero(fechas[lista_datos[6]])

        try:
            mes_final = int(fechas[lista_datos[7]])
        except ValueError:
            mes_final = mes_letra_a_numero(fechas[lista_datos[7]])

        if lista_datos[8]:
            año_inicio = letra_a_numero(fechas[lista_datos[8]])
        else:
            año_inicio = datetime.datetime.now().year

        if lista_datos[9]:
            año_final = letra_a_numero(fechas[lista_datos[9]])
        else:
            año_final = datetime.datetime.now().year

        fecha_inicio = str(año_inicio) + "-" + str(mes_inicio) + "-" + str(dia_inicio)
        fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y-%m-%d")

        fecha_final = str(año_final) + "-" + str(mes_final) + "-" + str(dia_final)
        fecha_final = datetime.datetime.strptime(fecha_final,"%Y-%m-%d")

        print(fecha_inicio)
        print(fecha_final)
        return fecha_inicio, fecha_final


def validar_fecha(proveedor, fechas):
    try:
        fecha_inicio = None
        fecha_final = None
        if fechas != "":
            fecha_inicio, fecha_final = r(proveedor, fechas)
        else:
            fecha_inicio = datetime.datetime.now()
            fecha_final = datetime.datetime.now()

        return fecha_inicio, fecha_final

    except ValueError:
        pass
    