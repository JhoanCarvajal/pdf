import datetime
from datetime import timedelta
import calendar


def letra_a_numero(dato):
    dato = dato.lower()
    print(dato)
    dato_corregido = ""
    r = ""
    for d in range(len(dato)):
        if dato[d] == "o":
            r = "0"
        if dato[d] == "i":
            r = "1"
        if dato[d] == "g":
            print("holaaaaaaaaaa")
            r = "6"
        if dato[d] == "s":
            r = "5"
        if dato[d] == "b":
            r = "8"
        dato_corregido += r
    print(f"este es el año corregido " + dato_corregido)
    return dato_corregido


def mes_letra_a_numero(dato):
    meses = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
    mes=dato.lower()
    if len(mes) == 4:
        mes = mes[:len(mes) - 1]
    mes_corregido = ""
    for letra in mes:
        if letra == "0":
            letra = "o"
        mes_corregido += letra
    print(mes)
    print(mes_corregido)
    for m in meses:
        if m == mes_corregido:
            mes_corregido = meses.index(m) + 1
    print(f'otro mes pero en numero {mes_corregido}')
    return mes_corregido


def crear_fecha(dato):
    datos_fecha = dato.split("/")
    for i in range(len(datos_fecha)):
        datos_fecha[i] = datos_fecha[i].strip()

    dia = letra_a_numero(datos_fecha[0])
    mes = mes_letra_a_numero(datos_fecha[1])
    año = letra_a_numero(datos_fecha[2])
    
    if int(dia) > 31:
        dia = 31
    fecha = año + "-" + str(mes) + "-" + dia
    try:
        fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
    except ValueError:
        fecha = datetime.datetime.strptime("1111-01-01","%Y-%m-%d")
    return fecha

def comparar_fechas(fechas):
    dia1 = fechas[0].strftime('%d')
    mes1 = fechas[0].strftime('%m')
    año1 = fechas[0].strftime('%Y')
    dia2 = fechas[1].strftime('%d')
    mes2 = fechas[1].strftime('%m')
    año2 = fechas[1].strftime('%Y')

def añadir_mes(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def restar_mes(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)


def validar_fecha(fechas):
    try:
        fechas = fechas.split("-")
        print(fechas)
        for i in range(len(fechas)):
            print(fechas[i])
            fechas[i] = crear_fecha(fechas[i])

        fechas_v = comparar_fechas(fechas)

        print(fechas)
        por_defecto = datetime.datetime.strptime("1111-01-01","%Y-%m-%d")

        if fechas[0] == por_defecto:
            if fechas[1] == por_defecto:
                # codigo por si las dos fechas estan malas
                print("imposible de saber")
            else:
                # codigo por si la primera fecha esta mala y la segunda buena
                un_mes_antes = restar_mes(fechas[1],1)
                fechas[0] = un_mes_antes
        else:
            if fechas[1] == por_defecto:
                # codigo por si la primera fecha esta buena y la segunda mala
                un_mes_despues = añadir_mes(fechas[0],1)
                fechas[1] = un_mes_despues
            else:
                # codigo por si las dos fechas estan bien
                un_mes_despues = añadir_mes(fechas[0],1)
                if fechas[1] == un_mes_despues:
                    pass
                else:
                    fechas[1] = fechas[1].strftime('%d-%m-%Y')
                    un_mes_despues = un_mes_despues.strftime('%d-%m-%Y')
        return fechas
    except ValueError:
        print("error en validar fecha")
    