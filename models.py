from peewee import *

DATABASE = 'database.db'

db = SqliteDatabase(DATABASE, pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Region(BaseModel):
    nombre = CharField(max_length=40, null=False, unique=True)

    class Meta:
        table_name = 'regiones'


class Departamento(BaseModel):
    departamento = CharField(max_length=40, null=False, default='')
    id_region = ForeignKeyField(Region, backref="departamento_region", on_delete='CASCADE')

    class Meta:
        table_name = 'departamentos'


class Municipio(BaseModel):
    municipio = CharField(max_length=40, null=False, default='')
    estado = IntegerField(null=False)
    id_departamento = ForeignKeyField(Departamento, backref="municipios_departamentos", on_delete='CASCADE')

    class Meta:
        table_name = 'municipios'


class Item(BaseModel):
    nombre = CharField(max_length=40, null=False, unique=True)
    descripcion = CharField(max_length=99, null=True)

    class Meta:
        table_name = 'items'


class Operador(BaseModel):
    nombre = CharField(max_length=40, null=False, unique=True)
    nit = CharField(max_length=40, null=False)
    direccion = CharField(max_length=99, null=True)

    class Meta:
        table_name = 'operadores'


class Restaurante(BaseModel):
    nombre = CharField(max_length=40, null=False, unique=True)
    direccion = TextField(null=True)
    id_municipio = ForeignKeyField(Municipio, backref="restaurante_municipio", on_delete='CASCADE')

    class Meta:
        table_name = 'restaurantes'


class Restaurantes_operadores(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="operador_restaurante", on_delete='CASCADE')
    id_restaurante = ForeignKeyField(Restaurante, backref="restaurante_operador", on_delete='CASCADE')
    matricula = CharField(max_length=40, null=False, unique=True)

    class Meta:
        table_name = 'restaurantes_operadores'


class Items_operador(BaseModel):
    id_item = ForeignKeyField(Item, backref="items_operador_items", on_delete='CASCADE')
    id_operador = ForeignKeyField(Operador, backref="items_operador_operador", on_delete='CASCADE')
    roi_nombre = CharField(max_length=40, null=False)
    roi_valor = CharField(max_length=40, null=False)

    class Meta:
        table_name = 'restaurantes_operadores'


class Factura(BaseModel):
    id_restaurante = ForeignKeyField(Restaurante, backref="factura_restaurante", on_delete='CASCADE')
    id_items_operador = ForeignKeyField(Items_operador, backref="factura_items_operador", on_delete='CASCADE')
    valor = CharField(max_length=99, null=True)

    class Meta:
        table_name = 'facturas'


class RoiOperador(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="roiOperador_operadores", on_delete='CASCADE')
    primer_roi = CharField(max_length=40, null=True)
    primera_palabra_clave = CharField(max_length=40, null=True)
    segundo_roi = CharField(max_length=40, null=True)
    segunda_palabra_clave = CharField(max_length=40, null=True)
    tercer_roi = CharField(max_length=40, null=True)
    tercera_palabra_clave = CharField(max_length=40, null=True)
    cuarto_roi = CharField(max_length=40, null=True)
    cuarta_palabra_clave = CharField(max_length=40, null=True)
    solo_negro = BooleanField(default=False)

    class Meta:
        table_name = 'roi_operadores'


class ValidarFechas(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="ValidarFechas_operadores", on_delete='CASCADE')
    remplazar = CharField(max_length=40, null=True)
    separadores = CharField(max_length=40)
    posicion_dia_inicio = IntegerField(null=True)
    posicion_dia_final = IntegerField(null=True)
    posicion_mes_inicio = IntegerField(null=True)
    posicion_mes_final = IntegerField(null=True)
    posicion_anho_inicio = IntegerField(null=True)
    posicion_anho_final = IntegerField(null=True)

    class Meta:
        table_name = 'validar_fechas'


def crear_tablas():
    with db:
        db.create_tables([Region, Departamento, Municipio, Operador, Restaurante, Item, Restaurantes_operadores, Items_operador, Factura, RoiOperador, ValidarFechas])