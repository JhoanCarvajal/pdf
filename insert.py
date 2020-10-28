import psycopg2
import datetime

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
    print(f'otro mes pero en numero {mes_corregido}')
    if int(datos_fecha[0]) > 31:
        datos_fecha[0] = 31
    fecha = str(datos_fecha[2]) + "-" + str(mes_corregido) + "-" + str(datos_fecha[0])
    fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
    return fecha

def numero_entero(dato):
    numero = ""
    for digito in dato:
        print(digito)
        if digito.isdigit():
            numero += str(digito)
    numero = int(numero)
    return numero

def numero_decimal(dato):
    try:
        if dato:
            numero = ""
            lista = dato.split(",")
            for digito in lista[0]:
                print(digito)
                if digito.isdigit():
                    numero += str(digito)
            numero += "." + lista[1]
            return numero
        else:
            numero = None
            print("No hay un numero para combertir a decimal")
    except ValueError:
        print("Hubo un error innesperado")
    

def insert(lista):
    con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
    cursor=con.cursor()

    inicial = fecha(lista[0])
    final = fecha(lista[1])
    causa = numero_entero(lista[2])
    consumo = numero_entero(lista[3])
    otros = numero_entero(lista[4])
    alumbrado = numero_entero(lista[5])
    kw = numero_entero(lista[6])
    vr_kw = numero_decimal(lista[7])
    direccion = lista[8]
    matricula = int(lista[9])

    sql = "select MAX(id) from facturas"
    cursor.execute(sql)
    max_id = cursor.fetchall()
    max_id = max_id[0][0]
    if max_id == None:
        max_id = 1
    else:
        max_id += 1

    id_restaurante = 0
    sql = "select id, matricula from restaurantes"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for datos in resultados:
        if datos[1]== matricula:
            id_restaurante = datos[0]
            sql="insert into facturas(id, id_restaurante, inicial, final,causa,consumo,otros,alumbrado,kw,valor_kw, direccion, matricula) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            datos=(max_id, id_restaurante, inicial, final, causa, consumo, otros, alumbrado, kw, vr_kw, direccion, matricula)
            print(datos)
            cursor.execute(sql, datos)
        else:
            print(f"No se ha encontrado el restaurante con esta matricula {matricula}")
    
    con.commit()
    con.close()

