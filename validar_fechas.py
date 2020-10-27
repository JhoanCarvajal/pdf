

def validar_fecha(fechas):
    #fecha == '05/DIC/2019', '-', '03/ENE/2020'
    datos_fechas = fechas.split()
    print(datos_fechas)
    desde = datos_fechas[0]
    hasta = datos_fechas[len(datos_fechas) -1]
    print(f'desde: {desde}, hasta: {hasta}')

validar_fecha("05/DIC/2019 - OVENE/2020")