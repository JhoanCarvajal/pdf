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
    causa = IntegerField()
    paga = IntegerField()
    ajuste = IntegerField()
    doc_pag = CharField(max_length=40, null=True)
    doc_aj = CharField(max_length=40, null=True)
    consumo_activa = IntegerField()
    consumo_reactiva = IntegerField()
    kw = IntegerField()
    valor_kw = FloatField()
    contribucion = IntegerField()
    alumbrado = IntegerField()


def crear_tablas():
    with db:
        db.create_tables([Region, Operador, Restaurante, Restaurantes_operadores, Factura])