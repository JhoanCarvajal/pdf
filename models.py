from peewee import *

DATABASE = 'database.db'

db = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = db


class Region(BaseModel):
    nombre = CharField(max_length=40)


class Operador(BaseModel):
    nombre = CharField(max_length=40)
    nit = CharField(max_length=40)
    servicio = CharField(max_length=40, null=True)


class Restaurante(BaseModel):
    nombre = CharField(max_length=40)
    direccion = TextField(null=True)
    id_region = ForeignKeyField(Region, backref="restaurante_region")


class Restaurantes_operadores(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="operador_restaurante")
    id_restaurante = ForeignKeyField(Restaurante, backref="restaurante_operador")
    medidor_telefono = CharField(max_length=40)


class Factura(BaseModel):
    id_restaurante = ForeignKeyField(Restaurante, backref="factura_restaurante")
    inicial = DateField()
    final = DateField()
    causa = FloatField()
    paga = FloatField()
    ajuste = FloatField()
    doc_pag = CharField(max_length=40, null=True)
    doc_aj = CharField(max_length=40, null=True)
    consumo_activa = FloatField()
    consumo_reactiva = FloatField()
    kw = FloatField()
    valor_kw = FloatField()
    contribucion = FloatField()
    alumbrado = FloatField()


class RoiOperador(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="roiOperador_operadores")
    roi = CharField(max_length=40, null=True)
    palabra_clave = CharField(max_length=40, null=True)


class RoiDatos(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="roiDatos_operadores")
    matricula = CharField(max_length=40)
    periodo = CharField(max_length=40)
    valor = CharField(max_length=40)
    kw = CharField(max_length=40)
    alumbrado = CharField(max_length=40)
    direccion = CharField(max_length=40)
    codigos = CharField(max_length=40)
    totales = CharField(max_length=40)

def crear_tablas():
    with db:
        db.create_tables([Region, Operador, Restaurante, Restaurantes_operadores, Factura, RoiOperador, RoiDatos])