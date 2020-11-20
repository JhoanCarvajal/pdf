from models import Restaurante, Factura, db, SQL
import datetime

# guardar nuevos registros en la tabla de facturas
def guardar_factura(lista):
    try:
        restaurantes = Restaurante.select(Restaurante.id,Restaurante.matricula)
        for restaurante in restaurantes:
            if lista[0] == restaurante.matricula:
                factura = Factura(id_restaurante=restaurante.id, matricula=lista[0], inicial=lista[1], 
                final=lista[2], causa=lista[3], paga=lista[4], ajuste=lista[5], doc_pag=lista[6],
                doc_aj=lista[7], consumo_activa=lista[8], consumo_reactiva=lista[9], kw=lista[10],
                valor_kw=lista[11], contribucion=lista[12], alumbrado=lista[13])

                factura.save()
    except:
        pass

# consulta sobre las facturas del restaurante dependiendo de un mes y un año
def info_restaurante(mes,nombre,año):
    restaurantes = Restaurante.raw("SELECT * FROM facturas WHERE id_restaurante = \
        (SELECT id FROM restaurantes WHERE nombre = ?) AND (SELECT EXTRACT(MONTH FROM final)) = ? \
            AND (SELECT EXTRACT(YEAR FROM final)) = ? ORDER BY id ASC ", (nombre, mes, año))

    print(restaurantes)

    for resta in restaurantes:
        print(resta)
    return []

# Consulta sobre las facturas del restaurante dependiendo de un año
def info_todo_año(nombre, año):
    restaurantes = Restaurante.raw("""SELECT * FROM facturas WHERE 
        id_restaurante = (SELECT id FROM restaurantes WHERE nombre = ?)
        AND (SELECT EXTRACT(YEAR FROM final)) = ?
        ORDER BY id ASC""",[nombre, año])

    print(restaurantes)
    return restaurantes

# Consulta sobre todas las facturas
def todo():
    sql = Factura.select()
    facturas = db.execute(sql)
    return facturas

# Consulta sobre los restaurantes
def lista_restaurantes():
    lista = []
    restaurantes = Restaurante.select()
    for restaurante in restaurantes:
        lista.append(restaurante.nombre)
    return lista
