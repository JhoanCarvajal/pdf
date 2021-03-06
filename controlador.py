from models import Region, Operador, Restaurante, Restaurantes_operadores, Factura, db, SQL
from models import RoiOperador, RoiDatos, IdentificadorTotales, ValidarFechas, Municipio, Departamento
import datetime
import sqlite3


# consulta sobre las facturas del restaurante dependiendo de un mes y un año
def info_restaurante(mes,nombre,año):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    sql = "SELECT * FROM facturas WHERE id_restaurante_id = \
        (SELECT id FROM restaurantes WHERE nombre = ?) AND (SELECT strftime('%m', DATE(final))) = ? \
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
    sql = "SELECT * FROM facturas WHERE \
        id_restaurante_id = (SELECT id FROM restaurantes WHERE nombre = ?) \
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

# facturas
def guardar_factura(lista):
    print(lista)
    try:
        me_te = str(lista[0])
        try:
            restaurante_operador = Restaurantes_operadores.get(Restaurantes_operadores.medidor_telefono == me_te)
        except:
            restaurante_operador = None
        if restaurante_operador:
            factura = Factura(id_restaurante=restaurante_operador.id_restaurante, inicial=lista[1], 
            final=lista[2], causa=lista[3], paga=lista[4], ajuste=lista[5], doc_pag=lista[6],
            doc_aj=lista[7], consumo_activa=lista[8], consumo_reactiva=lista[9], kw=lista[10],
            valor_kw=lista[11], contribucion=lista[12], alumbrado=lista[13])

            print(factura)

            r = factura.save()
            if r != 1:
                print('Error el restaurante no existe')
            else:
                print('factura creada')
        else:
            print('no existe una relcion')
    except:
        print('Hubo un error')

def buscar_causalidad(matricula):
    causalidad = None
    try:
        restaurante_operador = Restaurantes_operadores.get(Restaurantes_operadores.medidor_telefono == matricula)
    except:
        restaurante_operador = None

    if restaurante_operador:
        id_restaurante = restaurante_operador.id_restaurante
        facturas = Factura.select().where(Factura.id_restaurante == id_restaurante)
        for factura in facturas:
            print(factura.inicial)
            fecha_inicial = factura.inicial
            mes = fecha_inicial.strftime('%m')
            print(mes)
            if mes == '01':
                causalidad = str(factura.causa)
                break
            else:
                causalidad = None
                print('No existe la factura de enero')
    else:
        causalidad = None
    return causalidad

#departamentos
def lista_departamentos():
    lista = []
    departamentos = Departamento.select()
    for departamento in departamentos:
        lista.append(departamento)
    return lista

def id_departamento(nombre):
    try:
        departamento = Departamento.get(Departamento.departamento == nombre)
        return departamento.id
    except:
        return None

#regiones
def lista_regiones():
    lista = []
    regiones = Region.select()
    for region in regiones:
        lista.append(region)
    return lista

def id_region(nombre):
    try:
        region = Region.get(Region.nombre == nombre)
        return region.id
    except:
        return None

#municipios
def lista_municipios():
    lista = []
    municipios = Municipio.select()
    for municipio in municipios:
        lista.append(municipio.municipio)
    return lista

def id_municipio(nombre):
    # retorna solo el id de una region
    try:
        municipio = Municipio.get(Municipio.municipio == nombre)
        return municipio.id
    except:
        return None

def municipios_departamento(id_depa):
    # retorna los municipios de una region
    lista = []
    municipios = Municipio.select().where(Municipio.id_departamento == id_depa)
    for municipio in municipios:
        lista.append(municipio)
    return lista

# restaurante_operador
def buscar_restaurate_operador(matricula):
    restaurante = None
    operador = None
    try:
        restaurante_operador = Restaurantes_operadores.get(Restaurantes_operadores.matricula == matricula)
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

def guardar_restaurante_operador(id_oper, id_rest, matric):
    try:
        try:
            restaurante_operador = Restaurantes_operadores.get(Restaurantes_operadores.matricula == matric)
        except:
            restaurante_operador = None

        if not restaurante_operador:
            restaurante_operador = Restaurantes_operadores(id_operador=id_oper, id_restaurante=id_rest, matricula=matric)
            resultado = restaurante_operador.save()
            return resultado
        else:
            return -1
    except:
        print('Error al crear la relacion')

def get_restaurante_operador(id_resta):
    restaurante_operador = Restaurantes_operadores.get(Restaurantes_operadores.id_restaurante == id_resta)
    return restaurante_operador

def actualizar_restaurante_operador(id, id_oper, id_rest, matric):
    try:
        query = Restaurantes_operadores.update(id_operador=id_oper, id_restaurante=id_rest, matricula=matric).where(Restaurantes_operadores.id == id)
        resultado = query.execute()
        return resultado
    except ValueError():
        print('Error al actualizar restaurantes')

# regiones de interes del operador
def regiones_interes_operadores(id):
    lista = []
    sql = RoiOperador.select().where(RoiOperador.id_operador == id)
    resultados = db.execute(sql)
    for dato in resultados:
        lista.append(dato)
    return lista

#regiones de interes para los datos
def regiones_interes_datos(id_operador):
    lista = []
    sql = RoiDatos.select().where(RoiDatos.id_operador == id_operador)
    resultados = db.execute(sql)
    for dato in resultados:
        lista.append(dato)
    return lista

# identificador de los totales
def identificador_totales(id_operador):
    lista = []
    sql = IdentificadorTotales.select().where(IdentificadorTotales.id_operador == id_operador)
    resultados = db.execute(sql)
    for dato in resultados:
        lista.append(dato)
    return lista

# validar fechas
def validar_fechas(id_operador):
    lista = []
    sql = ValidarFechas.select().where(ValidarFechas.id_operador == id_operador)
    resultados = db.execute(sql)
    for dato in resultados:
        for d in dato:
            lista.append(d)
    return lista

# Operadores de red
def lista_operadores():
    lista = []
    operadores = Operador.select()
    for operador in operadores:
        lista.append(operador)
    return lista

def guardar_operador(nom, ni, dire):
    try:
        try:
            operador = Operador.get((Operador.nit == ni) | (Operador.nombre == nom))
        except:
            operador = None

        if not operador:
            operador = Operador(nombre=nom, nit=ni, direccion=dire)
            resultado = operador.save()
            return resultado
        else:
            return -1
    except:
        print('Error al crear un operador')

def todo_operadores():
    sql = Operador.select()
    operadores = db.execute(sql)
    return operadores

def eliminar_operador(id):
    try:
        resultado = Operador.delete_by_id(id)
        return resultado
    except ValueError():
        print('Error al eliminar el operador')

def actualizar_operador(id, nom, ni, dire):
    try:
        query = Operador.update(nombre=nom, nit=ni, direccion=dire).where(Operador.id == id)
        resultado = query.execute()
        return resultado
    except ValueError():
        print('Error al actualizar operador')

def id_operador_nit(nit):
    try:
        operador = Operador.get(Operador.nit == nit)
        return operador.id
    except:
        return None

def id_operador_nombre(nombre):
    try:
        operador = Operador.get(Operador.nombre == nombre)
        return operador.id
    except:
        return None

def buscar_operador(nit):
    try:
        operador = Operador.get(Operador.nit == nit)
        if operador:
            return operador
        else:
            return None
    except:
        pass

# Restaurantes
def lista_restaurantes():
    lista = []
    restaurantes = Restaurante.select()
    for restaurante in restaurantes:
        lista.append(restaurante.nombre)
    return lista

def todo_restaurantes():
    sql = Restaurante.select()
    restaurantes = db.execute(sql)
    return restaurantes

def eliminar_restaurante(id):
    try:
        resultaodo1 = Restaurantes_operadores.delete().where(Restaurantes_operadores.id_restaurante == id).execute()
        resultado2 = Restaurante.delete().where(Restaurante.id == id).execute()
        return resultado2
    except ValueError():
        print('Error al eliminar el restaurante')

def actualizar_restaurante(id, nom, dire, id_mun):
    try:
        query = Restaurante.update(nombre=nom, direccion=dire, id_municipio=id_mun).where(Restaurante.id == id)
        resultado = query.execute()
        return resultado
    except ValueError():
        print('Error al actualizar restaurantes')

def buscar_restaurante(id):
    restaurante = Restaurante.get(Restaurante.id == id)
    return restaurante

def id_restaurante(nombre):
    try:
        restaurante = Restaurante.get(Restaurante.nombre == nombre)
        return restaurante.id
    except:
        return None

def guardar_restaurante(nom, dire, id_mun):
    try:
        try:
            restaurante = Restaurante.get(Restaurante.nombre == nom)
        except:
            restaurante = None

        if not restaurante:
            restaurante = Restaurante(nombre=nom, direccion=dire, id_municipio=id_mun)
            resultado = restaurante.save()
            return resultado
        else:
            return -1
    except:
        print('Error al crear un restaurante')

