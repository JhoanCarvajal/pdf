import xlsxwriter
import datetime
import os
from subprocess import call
import threading


# from openpyxl import Workbook
# import openpyxl

# class energia():
#     def __init__(self, libro, restaurantes, facturas):
#         libro = "prueba.xlsx"
#         wb = openpyxl.load_workbook(libro)

#         # En este caso la hoja ORIGEN corresponde a la hoja
#         # inicial de libro por defecto en mi caso es Hoja1
#         # aunque python la denomina en inglés: sheet
#         # ESTO ES OPCIONAL si ya la hoja tiene el NOMBRE ORIGEN
#         wb.active.title = 'MODELO'

#         # Revisar los nombres de las hojas
#         # contenidas en el libro
#         # en este caso sólo existe una hoja: ORIGEN
#         print(wb.get_sheet_names())
#         # Se imprime en este caso: ['ORIGEN']

#         # Se define una variable para 
#         # la hoja ORIGEN 
#         # a fin de no emplear "active"
#         origen = wb['MODELO']

#         # Se copian los valores de la
#         # hoja ORIGEN a la destino
#         # esta función también crea la hoja en cuestión
#         # for restaurante in restaurantes:
#         wb.copy_worksheet(origen)
#         # Se le pone el nombre "DESTINO"
#         # de lo contrario python lo define
#         # como ORIGEN Copy
#         # print(str(restaurante[0]))
#         # nueva_hoja.title= str(restaurante[0])

#         # row = 13
#         # col = 1
#         # for factura in facturas:
#         #     print(factura[1])
#         #     wss = wb.worksheets()
#         #     for factura_ws in wss:
#         #         if factura_ws.get_name() == str(factura[1]):
#         #             factura_ws.activate()
#         #             for dato in factura[3:]:
#         #                 factura_ws.write(row, col, dato)
#         #                 col += 1
#         #         col = 1
#         #         row += 1

#         # Se guarda
#         wb.save(libro)

class energia():

    def __init__(self, libro, restaurantes, facturas):
        wb = libro
        for restaurante in restaurantes:
            new_ws = wb.add_worksheet(str(restaurante[0]))

            format_titulo = wb.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'fg_color': '#FFCC99'})
            format_subtitulo = wb.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'font_color': '#0000F4'})
            format_border_izq = wb.add_format({
                'left': 1,
            })
            format_border_der = wb.add_format({
                'right': 1,
            })
            format_border_abj = wb.add_format({
                'bottom': 1,
            })
            format_border_izq_abj = wb.add_format({
                'left': 1,
                'bottom': 1,
            })
            format_border_der_abj = wb.add_format({
                'right': 1,
                'bottom': 1,
            })

            new_ws.merge_range('B2:N2','ENERGIA ELECTRICA', format_titulo)
            new_ws.merge_range('B3:C3','PER. DE COBRO', format_subtitulo)
            new_ws.merge_range('D3:J3','INFORMACIÓN CONTABILIDAD', format_subtitulo)
            new_ws.merge_range('K3:N3','INFORMACIÓN PPTOS', format_subtitulo)

            lista_titulos = ['INICIAL','FINAL','CAUSA','PAGA','AJUS','DOC PAG','DOC AJ','CONSU ACT','CONSU REAC','KW','Vr KW','Otros','ALUMBRADO']

            row = 3
            col = 1
            for i in lista_titulos:
                new_ws.write(row, col, i, format_subtitulo)
                col += 1
            new_ws.set_column('A:A', 1)
            new_ws.set_column('B:N', 12)
            for col in range(2,13):
                new_ws.write(16, col, None, format_border_abj)
            for row in range(4,16):
                new_ws.write(row, 1, None, format_border_izq)
            for row in  range(4,16):
                new_ws.write(row, 13, None, format_border_der)
            new_ws.write(16, 1, None, format_border_izq_abj)
            new_ws.write(16, 13, None, format_border_der_abj)
            # new_ws.set_column('B5:B17', None, format_border_izq)
            # new_ws.set_column('N5:N17', None, format_border_der)

        row = 5
        col = 1
        for factura in facturas:
            print(factura[1])
            wss = wb.worksheets()
            for factura_ws in wss:
                if factura_ws.get_name() == str(factura[1]):
                    factura_ws.activate()
                    for dato in factura[3:]:
                        factura_ws.write(row, col, dato)
                        col += 1
                col = 1
                row += 1
        
        print("listo")

