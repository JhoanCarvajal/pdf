import psycopg2

con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
cursor=con.cursor()


def info_restaurante(mes,nombre,año):
    sql = """SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)
        AND (SELECT EXTRACT(MONTH FROM final)) = %s AND (SELECT EXTRACT(YEAR FROM final)) = %s
        ORDER BY id ASC """
    datos=(nombre,mes,año)
    cursor.execute(sql,datos)
    restaurantes = cursor.fetchall()
    return restaurantes

def info_todo_año(nombre,año):
    sql = """SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)
        AND (SELECT EXTRACT(YEAR FROM final)) = %s
        ORDER BY id ASC """
    datos=(nombre,año)
    cursor.execute(sql,datos)
    restaurantes = cursor.fetchall()
    return restaurantes