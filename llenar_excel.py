import xlsxwriter
import insert
import datetime
import os
from subprocess import call
import datetime

def cosulta(resultado):
    wb = xlsxwriter.Workbook('excel/resultado_consulta.xlsx')
    ws = wb.add_worksheet()

    row = 0
    col = 0

    titulos = ["#","Cod restaurante","Lectura actual","Lectura anterior","Consumo","Vertimiento","Total a pagar","fecha"]
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
    os.system("C:/Users/Jhoan/Documents/tecnoparque/pdf/excel/resultado_consulta.xlsx")