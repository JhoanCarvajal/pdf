import psycopg2
import datetime
import validar_fechas


def numero_entero(dato):
    try:
        numero = ""
        negativo = False
        for digito in dato:
            print(digito)
            if digito.isdigit():
                numero += str(digito)
            elif digito == "-":
                negativo = True
        numero = int(numero)
        if negativo:
            numero *= -1
        return numero
    except ValueError:
        print("hubo un error al combertir a numero")

def numero_decimal(dato):
    try:
        if dato:
            numero = ""
            lista = dato.split(",")
            if len(lista) > 2:
                for digito in lista[0]:
                    if digito.isdigit():
                        numero += str(digito)
                numero += "." + lista[-1]
            else:
                numero = float(dato)
            return numero
        else:
            numero = None
            print("No hay un numero para combertir a decimal")
    except ValueError:
        print("Hubo un error innesperado al convertir numero a decimal")
    

def insert(lista):
    try:
        con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
        cursor=con.cursor()

        matricula = numero_entero(lista[0])
        if matricula < 0:
            matricula *= -1
        if isinstance(lista[1], str):
            inicial = validar_fechas.crear_fecha(lista[1])
        else:
            inicial = lista[1]
        if isinstance(lista[2], str):
            final = validar_fechas.crear_fecha(lista[2])
        else:
            final = lista[2]
        vr_paga = numero_entero(lista[3])
        consumo = numero_entero(lista[4])
        kw = numero_entero(lista[5])
        vr_kw = numero_decimal(lista[6])
        otros = numero_entero(lista[7])
        alumbrado = numero_entero(lista[8])
        direccion = lista[9]

        causa = 7990000
        paga = vr_paga - otros
        ajuste = paga - causa
        doc_pag = None
        doc_aj = None
        
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
                sql="insert into facturas(id, id_restaurante, matricula, inicial, final, causa, paga, ajuste, doc_pag, doc_aj, \
                    consumo, kw, vr_kw, otros, alumbrado) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                datos=(max_id, id_restaurante, matricula, inicial, final, causa, paga, ajuste, \
                    doc_pag, doc_aj, consumo, kw, vr_kw, otros, alumbrado)
                print(datos)
                cursor.execute(sql, datos)
            else:
                print(f"No se ha encontrado el restaurante con esta matricula {matricula}")
        
        con.commit()
        con.close()
        return True
    except ValueError:
        print("error en insert")
        return False

