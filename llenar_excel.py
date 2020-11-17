import xlsxwriter
import insert
import datetime
import os
from subprocess import call
import threading

def consulta(resultado):
    if resultado:
        # ruta
        directorio = os.getcwd()
        fecha = datetime.datetime.now()
        fecha = fecha.strftime("%m_%d_%Y_%H_%M_%S")
        # creamos un excel en la siguiente ruta
        wb = xlsxwriter.Workbook(f'{directorio}/R_C_{fecha}.xlsx')
        # añadimos una hoja de trabajo
        ws = wb.add_worksheet()

        row = 0
        col = 0
        # lista de los titulos para los resultados
        titulos = ["#","Cod restaurante", "Matricula", "Lectura inicial","Lectura final","Causa mes","Paga mes","Ajus","Doc pag", "Doc aj", "Consumo activa", "Consumo reactiva", "Kw/h","Valor de Kw/h","Otros","Alumbrado"]
        # escribimos los titulos en el excel
        for titulo in titulos:
            ws.write(row, col, titulo)
            col +=1
        col = 0
        # escribimos los resultados por cada restaurante en el excel
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
        # cerramos el excel
        wb.close()

        # abrimos el archivo en un subproceso para visualizar el excel
        def abrir_excel():
            os.system(f"{directorio}/R_C_{fecha}.xlsx")
        t = threading.Thread(target=abrir_excel)
        t.start()
    else:
        pass