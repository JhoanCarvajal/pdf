import psycopg2
# Coneccion con la base de datos
con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
cursor=con.cursor()

# consulta sobre las facturas del restaurante dependiendo de un mes y un año
def info_restaurante(mes,nombre,año):
    sql = """SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)
        AND (SELECT EXTRACT(MONTH FROM final)) = %s AND (SELECT EXTRACT(YEAR FROM final)) = %s
        ORDER BY id ASC """
    datos=(nombre,mes,año)
    cursor.execute(sql,datos)
    restaurantes = cursor.fetchall()
    return restaurantes
# Consulta sobre las facturas del restaurante dependiendo de un año
def info_todo_año(nombre,año):
    sql = """SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)
        AND (SELECT EXTRACT(YEAR FROM final)) = %s
        ORDER BY id ASC """
    datos=(nombre,año)
    cursor.execute(sql,datos)
    restaurantes = cursor.fetchall()
    return restaurantes
# Consulta sobre todas las facturas
def todo():
    sql = """SELECT * FROM facturas"""
    cursor.execute(sql)
    restaurantes = cursor.fetchall()
    return restaurantes
# Consulta sobre los restaurantes
def lista_restaurantes():
    sql = "select id, nombre from restaurantes"
    cursor.execute(sql)
    restaurantes = cursor.fetchall()
    lista = []
    for restaurante in restaurantes:
        lista.append(restaurante[1])
    return lista