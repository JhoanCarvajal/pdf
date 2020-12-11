import xlsxwriter
import datetime
import os
from subprocess import call
import threading


from openpyxl import Workbook
import openpyxl

class energia():
    def __init__(self, libro, restaurantes, facturas):
        self.restaurantes = restaurantes
        self.facturas = facturas
        self.libro = "prueba.xlsx"

        self.wb = openpyxl.load_workbook(self.libro)

        # En este caso la hoja MODELO corresponde a la hoja inicial de libro
        self.wb.active.title = 'MODELO'

        # Revisar los nombres de las hojas contenidas en el libro
        print(self.wb.get_sheet_names())

        # lista de hojas
        self.hojas = self.wb.get_sheet_names()

        # Se define una variable para la hoja MODELO a fin de no emplear "active"
        self.modelo = self.wb['MODELO']

        # Se copian los valores de la hoja MODELO a la destino esta función también crea la hoja en cuestión
        for restaurante in self.restaurantes:
            if not str(restaurante[0]) in self.hojas:
                self.nueva_hoja = self.wb.copy_worksheet(self.modelo)
                # Se le pone el nombre de lo contrario python lo define como MODELO Copy
                self.nueva_hoja.title= str(restaurante[0])

        self.hojas = self.wb.get_sheet_names()
        print(self.hojas)

        for ws in self.hojas:
            print(f'ws: {ws}')
            self.llenar_datos(ws)

        
        # Se guarda
        self.wb.save(self.libro)

    def llenar_datos(self, ws):
        row = 5
        col = 2
        for factura in self.facturas:
            print(f'if {str(factura[1])} == {ws}')
            if str(factura[1]) == ws:
                hoja = self.wb[ws]
                print(f' hoja: {hoja}')
                for dato in factura[3:]:
                    hoja.cell(row=row, column=col, value=dato)
                    col += 1
                col = 2
                row += 1

