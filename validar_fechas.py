import datetime

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

# para crear una fecha
def crear_fecha(dato):
    try:
        datos_fecha = dato.split("/")
        print(datos_fecha)
        for i in range(len(datos_fecha)):
            datos_fecha[i] = datos_fecha[i].strip()
        # datos de la fecha
        dia = letra_a_numero(datos_fecha[0])
        try:
            mes = int(datos_fecha[1])
        except ValueError:
            mes = mes_letra_a_numero(datos_fecha[1])
        año = letra_a_numero(datos_fecha[2])
        # por si el dia es mayor a 31
        if int(dia) > 31:
            dia = 31
        # creamos el string de la fecha
        fecha = año + "-" + str(mes) + "-" + dia
        # intentamos convertir a datetime
        try:
            fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
        except ValueError:
            fecha = datetime.datetime.strptime("1111-01-01","%Y-%m-%d")
        return fecha
    except ValueError:
        pass

def comparar_fechas(fechas):
    try:
        # separo los datos de las dos fechas
        dia1 = int(fechas[0].strftime('%d'))
        mes1 = int(fechas[0].strftime('%m'))
        año1 = int(fechas[0].strftime('%Y'))
        dia2 = int(fechas[1].strftime('%d'))
        mes2 = int(fechas[1].strftime('%m'))
        año2 = int(fechas[1].strftime('%Y'))
        fechas = []
        # comparo los meses para saber si el primero es dic y el segundo ene
        if mes1 == 12 and mes2 == 1:
            # por si el primer año es diferente al segundo - 1 año
            if año2-1 != año1:
                año1 = año2-1
        # si no se cumple lo de los meses
        # los años tienen que ser iguales 
        elif año1 != año2:
            año1 = año2
        #creo los strings de cada fecha y los convierto a datetime
        fecha1 = str(año1) + "-" + str(mes1) + "-" + str(dia1)
        fecha1 = datetime.datetime.strptime(fecha1,"%Y-%m-%d")
        # guardo la fecha en la lista
        fechas.append(fecha1)
        fecha2 = str(año2) + "-" + str(mes2) + "-" + str(dia2)
        fecha2 = datetime.datetime.strptime(fecha2,"%Y-%m-%d")
        # guardo la fecha en la lista
        fechas.append(fecha2)

        return fechas
    except ValueError:
        pass


def validar_fecha(proveedor, fechas):
    try:
        fecha_inicio = None
        fecha_final = None
        if proveedor == 2 or proveedor == 4 or proveedor == 6 or proveedor == 9 or proveedor == 10 or proveedor == 14:
            if "-" in fechas:
                fechas = fechas.split("-")
            else:
                fechas = fechas.split("a")
            print(fechas)
            #creo las fechas
            for i in range(len(fechas)):
                fechas[i] = crear_fecha(fechas[i])

            #comparo los años
            fechas = comparar_fechas(fechas)

            #separo las fechas
            fecha_inicio = fechas[0]
            fecha_final = fechas[1]

        elif proveedor == 1:
            fechas = fechas.split()
            print(fechas)

            mes = mes_letra_a_numero(fechas[3])
            dia_inicio = letra_a_numero(fechas[0])
            dia_final = letra_a_numero(fechas[2])
            año = letra_a_numero(fechas[5])

            fecha_inicio = str(año) + "-" + str(mes) + "-" + str(dia_inicio)
            fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y-%m-%d")

            fecha_final = str(año) + "-" + str(mes) + "-" + str(dia_final)
            fecha_final = datetime.datetime.strptime(fecha_final,"%Y-%m-%d")

        elif proveedor == 3:
            fechas = fechas.split()
            print(fechas)

            dia_inicio = letra_a_numero(fechas[2])
            mes_inicio = mes_letra_a_numero(fechas[3])
            dia_final = letra_a_numero(fechas[5])
            mes_final = mes_letra_a_numero(fechas[6])
            año = datetime.datetime.now().year

            fecha_inicio = str(año) + "-" + str(mes_inicio) + "-" + str(dia_inicio)
            fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y-%m-%d")

            fecha_final = str(año) + "-" + str(mes_final) + "-" + str(dia_final)
            fecha_final = datetime.datetime.strptime(fecha_final,"%Y-%m-%d")
        # 10-01-2020/10-02-2020
        elif proveedor == 11:
            fechas = fechas.split("/")
            fecha_inicio = fechas[0]
            fecha_final = fechas[1]
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y")
            fecha_final = datetime.datetime.strptime(fecha_final, "%d-%m-%Y")
        # oct 03 a nov 03
        elif proveedor == 13:
            fechas = fechas.split(" ")
            print(fechas)
            dia_inicio = letra_a_numero(fechas[1])
            mes_inicio = mes_letra_a_numero(fechas[0])
            dia_final = letra_a_numero(fechas[4])
            mes_final = mes_letra_a_numero(fechas[3])
            año = datetime.datetime.now().year

            fecha_inicio = str(año) + "-" + str(mes_inicio) + "-" + str(dia_inicio)
            fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y-%m-%d")

            fecha_final = str(año) + "-" + str(mes_final) + "-" + str(dia_final)
            fecha_final = datetime.datetime.strptime(fecha_final,"%Y-%m-%d")

        # proveedor == 5
        else:
            fecha_inicio = datetime.datetime.now()
            fecha_final = datetime.datetime.now()

        return fecha_inicio, fecha_final

    except ValueError:
        pass
    