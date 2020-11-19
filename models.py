from peewee import *

DATABASE = 'database.db'

db = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = db

class Restaurante(BaseModel):
    nombre = CharField(max_length=40)
    matricula = IntegerField()
    direccion = TextField()

class Factura(BaseModel):
    id_restaurante = ForeignKeyField(Restaurante, backref="racturas_de")
    matricula = IntegerField()
    inicial = DateField()
    final = DateField()
    causa = IntegerField()
    paga = IntegerField()
    ajuste = IntegerField()
    doc_pag = IntegerField()
    doc_aj = IntegerField()
    consumo_activa = IntegerField()
    consumo_reactiva = IntegerField()
    kw = IntegerField()
    valor_kw = FloatField()
    contribucion = IntegerField()
    alumbrado = IntegerField()

def crear_tablas():
    with db:
        db.create_tables([Restaurante, Factura])