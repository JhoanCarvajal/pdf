import psycopg2
import datetime

con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
cursor=con.cursor()

def fecha(dato):
    print(dato)
    datos_fecha = dato.split("/")
    print(datos_fecha)
    meses = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
    mes=datos_fecha[1].lower()
    print(mes)
    temp = len(mes)
    #mes = mes[:temp - 1]
    for m in meses:
        if m == mes:
            mes = meses.index(m) + 1
    print(f'otro mes pero en numero {mes}')
    fecha = str(datos_fecha[2]) + "-" + str(mes) + "-" + str(datos_fecha[0])
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

def insert(lista):
    inicial = fecha(lista[0])
    final = fecha(lista[1])
    causa = numero_entero(lista[2])
    consumo = numero_entero(lista[3])
    otros = numero_entero(lista[4])
    alumbrado = numero_entero(lista[5])
    kw = numero_entero(lista[6])
    vr_kw = float(lista[7])
    direccion = lista[8]

    sql = "select MAX(id) from facturas"
    cursor.execute(sql)
    max_id = cursor.fetchall()
    max_id = max_id[0][0]
    if max_id == None:
        max_id = 1
    else:
        max_id += 1

    id_restaurante = 0
    sql = "select id, direccion from restaurantes"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for datos in resultados:
        if datos[1]== direccion:
            id_restaurante = datos[0]
            sql="insert into facturas(id, id_restaurante, inicial, final,causa,consumo,otros,alumbrado,kw,direccion,valor_kw) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            datos=(max_id, id_restaurante, inicial, final, causa, consumo, otros, alumbrado, kw, direccion, vr_kw)
            print(datos)
            cursor.execute(sql, datos)
            con.commit()
            con.close()
        else:
            print(f"No se ha encontrado el restaurante con esta direccion {direccion}")

