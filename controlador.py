from models import *

# consulta sobre las facturas del restaurante dependiendo de un mes y un año
def info_restaurante(mes,nombre,año):
    restaurantes = Restaurante.raw("""SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)
        AND (SELECT EXTRACT(MONTH FROM final)) = %s AND (SELECT EXTRACT(YEAR FROM final)) = %s
        ORDER BY id ASC """,nombre,mes,año)
    return restaurantes

# Consulta sobre las facturas del restaurante dependiendo de un año
def info_todo_año(nombre, año):
    restaurantes = Restaurante.raw('''SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)
        AND (SELECT EXTRACT(YEAR FROM final)) = %s
        ORDER BY id ASC''',nombre, año)
    return restaurantes

# Consulta sobre todas las facturas
def todo():
    facturas = Factura.select()
    facs = db.execute(facturas)
    return facs

# Consulta sobre los restaurantes
def lista_restaurantes():
    lista = []
    restaurantes = Restaurante.select()
    for restaurante in restaurantes:
        lista.append(restaurante.nombre)
    return lista
