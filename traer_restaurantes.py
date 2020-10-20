import psycopg2

con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
cursor=con.cursor()


def lista_restaurantes():
    sql = "select id, nombre from restaurantes"
    cursor.execute(sql)
    restaurantes = cursor.fetchall()
    lista = []
    for restaurante in restaurantes:
        lista.append(restaurante[1])
    return lista