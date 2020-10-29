import datetime
from datetime import timedelta

def fecha(dato):
    print(dato)
    datos_fecha = dato.split("/")
    print(datos_fecha)
    meses = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
    mes=datos_fecha[1].lower()
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
        else:
            datos_fecha[0] = 1
            datos_fecha[1] = 1
            datos_fecha[2] = 1111
    print(f'otro mes pero en numero {mes_corregido}')
    if int(datos_fecha[0]) > 31:
        datos_fecha[0] = 31
    fecha = str(datos_fecha[2]) + "-" + str(mes_corregido) + "-" + str(datos_fecha[0])
    try:
        fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
    except ValueError:
        fecha = datetime.datetime.strptime("1111-01-01","%Y-%m-%d")
    return fecha

def validar_fecha(fecha_inicio, fecha_final):
    #fecha == '05/DIC/2019', '-', '03/ENE/2020'
    try:
        fecha1 = datetime.datetime.strptime(fecha_inicio,"%Y-%m-%d")
        fecha2 = datetime.datetime.strptime(fecha_final,"%Y-%m-%d")

        por_defecto = datetime.datetime.strptime("1111-01-01","%Y-%m-%d")
        if fecha1 == por_defecto:
            if fecha2 == por_defecto:
                print("imposible de saber")
            else:
                un_mes_antes = fecha2 - timedelta(month=1)
                
        else:
            if fecha2 == por_defecto:
                un_mes_despues = fecha1 + timedelta(month=1)
            else:
                print("codigo por si las dos fechas estan bien")

        return fecha1, fecha2
    except ValueError:
        print("error en validar fecha")
    