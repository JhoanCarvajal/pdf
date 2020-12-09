import xlsxwriter
import datetime
import os
from subprocess import call
import threading

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
            format_border_arrb = wb.add_format({
                'top': 1,
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
            for col in range(1,14):
                new_ws.write(16, col, None, format_border_abj)
            for row in range(5,17):
                new_ws.write(row, 1, None, format_border_izq)
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

