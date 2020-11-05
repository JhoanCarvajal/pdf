import psycopg2

def insert(lista):
    try:
        con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
        cursor=con.cursor()
        
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
            if datos[1]== lista[0]:
                id_restaurante = datos[0]
                sql="insert into facturas(id, id_restaurante, matricula, inicial, final, causa, paga, ajuste, doc_pag, doc_aj, \
                    consumo, kw, vr_kw, otros, alumbrado) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                datos=(max_id, id_restaurante, lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], \
                    lista[6], lista[7], lista[8], lista[9], lista[10], lista[11], lista[12])
                print(datos)
                cursor.execute(sql, datos)
            else:
                print(f"No se ha encontrado el restaurante con esta matricula {lista[0]}")
        
        con.commit()
        con.close()
    except ValueError:
        print("error al guardar los datos en la base de datos")
