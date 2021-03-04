from peewee import *

DATABASE = 'database.db'

db = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = db


class Region(BaseModel):
    nombre = CharField(max_length=40)

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


class Operador(BaseModel):
    nombre = CharField(max_length=40, unique=True)
    nit = CharField(max_length=40)
    direccion = CharField(max_length=99, null=True)

    class Meta:
        table_name = 'operadores'


class Restaurante(BaseModel):
    nombre = CharField(max_length=40, unique=True)
    direccion = TextField(null=True)
    id_region = ForeignKeyField(Region, backref="restaurante_region", on_delete='CASCADE')
    id_municipio = ForeignKeyField(Municipio, backref="restaurante_municipio", on_delete='CASCADE')

    class Meta:
        table_name = 'restaurantes'


class Restaurantes_operadores(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="operador_restaurante", on_delete='CASCADE')
    id_restaurante = ForeignKeyField(Restaurante, backref="restaurante_operador", on_delete='CASCADE')
    medidor_telefono = CharField(max_length=40)

    class Meta:
        table_name = 'restaurantes_operadores'


class Factura(BaseModel):
    id_restaurante = ForeignKeyField(Restaurante, backref="factura_restaurante", on_delete='CASCADE')
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


class RoiDatos(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="roiDatos_operadores", on_delete='CASCADE')
    matricula = CharField(max_length=40)
    periodo = CharField(max_length=40)
    valor = CharField(max_length=40)
    kw = CharField(max_length=40)
    alumbrado = CharField(max_length=40)
    direccion = CharField(max_length=40)
    codigos = CharField(max_length=40)
    totales = CharField(max_length=40)

    class Meta:
        table_name = 'roi_datos'


class IdentificadorTotales(BaseModel):
    id_operador = ForeignKeyField(Operador, backref="identificadorTotales_operadores", on_delete='CASCADE')
    consumo_activa = CharField(max_length=40)
    contribucion_activa = CharField(max_length=40)
    consumo_reactiva = CharField(max_length=40)
    contribucion_reactiva = CharField(max_length=40)

    class Meta:
        table_name = 'identificadores_totales'


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
        db.create_tables([Region, Departamento, Municipio, Operador, Restaurante, 
        Restaurantes_operadores, Factura, RoiOperador, RoiDatos, IdentificadorTotales, ValidarFechas])