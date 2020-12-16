from models import Region, Operador, Restaurante, Restaurantes_operadores, Factura, db, SQL
import datetime
import sqlite3
import crear_restaurante

# guardar nuevos registros en la tabla de facturas
def guardar_factura(lista):
    print(lista)
    try:
        restaurantes_operadores = Restaurantes_operadores.select()
        r = 0
        for restaurante_operador in restaurantes_operadores:
            print(f'{lista[0]} == {restaurante_operador.medidor_telefono}')
            if str(lista[0]) == restaurante_operador.medidor_telefono:
                factura = Factura(id_restaurante=restaurante_operador.id_restaurante, inicial=lista[1], 
                final=lista[2], causa=lista[3], paga=lista[4], ajuste=lista[5], doc_pag=lista[6],
                doc_aj=lista[7], consumo_activa=lista[8], consumo_reactiva=lista[9], kw=lista[10],
                valor_kw=lista[11], contribucion=lista[12], alumbrado=lista[13])

                print(factura)

                r = factura.save()
        if r != 1:
            print('Error el restaurante no existe')
            # ans = crear_restaurante.nombre_restaurante()
            # restaurante = Restaurante(nombre = ans, matricula = lista[0], direccion = lista[15])
            # restaurante.save()
            # guardar_factura(lista)
    except:
        print('Hubo un error')

# consulta sobre las facturas del restaurante dependiendo de un mes y un año
def info_restaurante(mes,nombre,año):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    sql = "SELECT * FROM factura WHERE id_restaurante_id = \
        (SELECT id FROM restaurante WHERE nombre = ?) AND (SELECT strftime('%m', DATE(final))) = ? \
            AND (SELECT strftime('%Y', DATE(final))) = ? ORDER BY id ASC"
    datos = (str(nombre), str(mes), str(año))
    cursor.execute(sql, datos)
    restaurantes = cursor.fetchall()
    cursor.close()
    return restaurantes

# Consulta sobre las facturas del restaurante dependiendo de un año
def info_todo_año(nombre, año):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    sql = "SELECT * FROM factura WHERE \
        id_restaurante_id = (SELECT id FROM restaurante WHERE nombre = ?) \
        AND (SELECT strftime('%Y', DATE(final))) = ? \
        ORDER BY id ASC"
    datos = (str(nombre), str(año))
    cursor.execute(sql, datos)
    restaurantes = cursor.fetchall()
    cursor.close
    return restaurantes

# Consulta sobre todas las facturas
def todo():
    lista_facturas = []
    sql = Restaurante.select()
    restaurantes = db.execute(sql)
    sql = Factura.select().order_by(Factura.inicial)
    facturas = db.execute(sql)
    for factura in facturas:
        lista_facturas.append(factura)
    return restaurantes, lista_facturas

# Consulta sobre los restaurantes
def lista_restaurantes():
    lista = []
    restaurantes = Restaurante.select()
    for restaurante in restaurantes:
        lista.append(restaurante.nombre)
    return lista

def lista_regiones():
    lista = []
    regiones = Region.select()
    for region in regiones:
        lista.append(region.nombre)
    return lista

def id_region(nombre):
    region = Region.get(Region.nombre == nombre)
    print(region.nombre, region.id)
    return region.id

def buscar_operador(nit):
    try:
        operador = Operador.get(Operador.nit == nit)
        if operador:
            return operador
        else:
            return None
    except:
        pass

def buscar_restaurate_operador(medidor_telefono):
    try:
        restaurante_operador = Restaurantes_operadores.get(Restaurantes_operadores.medidor_telefono == medidor_telefono)
    except:
        restaurante_operador = None
    
    if restaurante_operador:
        id_restaurante = restaurante_operador.id_restaurante
        id_operador = restaurante_operador.id_operador
        restaurante = Restaurante.get(Restaurante.id == id_restaurante)
        operador = Operador.get(Operador.id == id_operador)
    else:
        restaurante = None
        operador = None
    
    return restaurante, operador


def guardar_restaurante(lista):
    try:
        try:
            restaurante = Restaurante.get(Restaurante.nombre == lista[0])
        except:
            restaurante = None

        if not restaurante:
            restaurante = Restaurante(nombre=lista[0], direccion=lista[1], id_region=lista[2])
            r = restaurante.save()
            if r != 1:
                print('No se creo el restaurante')
            else:
                print('restaurate creado')
        else:
            print('el restaurante ya existe', restaurante.id)
    except:
        print('error al crear un restaurante')