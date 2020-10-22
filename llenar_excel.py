import xlsxwriter
import insert
import datetime
import os
from subprocess import call
import threading

def cosulta(resultado):
    if resultado:
        directorio = os.getcwd()
        fecha = datetime.datetime.now()
        fecha = fecha.strftime("%m_%d_%Y_%H_%M_%S")
        print(fecha)
        wb = xlsxwriter.Workbook(f'{directorio}/excel/R_C_{fecha}.xlsx')
        ws = wb.add_worksheet()

        row = 0
        col = 0

        titulos = ["#","Cod restaurante","Lectura Inicial","Lectura Final","Causa mes","Consumo mes","Otros","Alumbrado","Kw/h","Valor de Kw/h","Matricula","Dirección"]
        for titulo in titulos:
            ws.write(row, col, titulo)
            col +=1
        col = 0
        for restaurante in resultado:
            row +=1
            for dato in restaurante:
                if isinstance(dato, datetime.date):
                    dato = dato.strftime("%Y-%m-%d")
                    ws.write(row, col, dato)
                else:
                    ws.write(row, col, dato)
                col +=1
            col = 0
                
        wb.close()
        def abrir_excel():
            os.system(f"{directorio}/excel/R_C_{fecha}.xlsx")
        t = threading.Thread(target=abrir_excel)
        t.start()
    else:
        print("No hay ningun restaurante con factura en esta fecha")