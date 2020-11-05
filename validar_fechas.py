import datetime

def letra_a_numero(dato):
    dato = dato.lower()

    print(dato)
    dato_corregido = ""

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
    dia1 = int(fechas[0].strftime('%d'))
    mes1 = int(fechas[0].strftime('%m'))
    año1 = int(fechas[0].strftime('%Y'))
    dia2 = int(fechas[1].strftime('%d'))
    mes2 = int(fechas[1].strftime('%m'))
    año2 = int(fechas[1].strftime('%Y'))
    fechas = []

    print(dia1, mes1, año1, dia2, mes2, año2)
    if mes1 == 12 and mes2 == 1:
        if año2-1 != año1:
            año1 = año2-1
    elif año1 != año2:
        año1 = año2
    fecha1 = str(año1) + "-" + str(mes1) + "-" + str(dia1)
    fecha1 = datetime.datetime.strptime(fecha1,"%Y-%m-%d")
    fechas.append(fecha1)
    fecha2 = str(año2) + "-" + str(mes2) + "-" + str(dia2)
    fecha2 = datetime.datetime.strptime(fecha2,"%Y-%m-%d")
    fechas.append(fecha2)

    return fechas



def validar_fecha(fechas):
    try:
        fechas = fechas.split("-")
        print(fechas)
        #creo las fechas
        for i in range(len(fechas)):
            print(fechas[i])
            fechas[i] = crear_fecha(fechas[i])

        #comparo los años
        fechas = comparar_fechas(fechas)

        print(f"retornamos estas fechas: {fechas}")

        #separo las fechas
        fecha_inicio = fechas[0]
        fecha_final = fechas[1]

        return fecha_inicio, fecha_final
    except ValueError:
        print("error en validar fecha")
    