from validar_fechas import *
import controlador 

def retornar_totales(proveedor, codigos, totales):
    pos_consumo_activa = None
    pos_contribucion_activa = None
    pos_consumo_reactiva = None
    pos_contribucion_reactiva = None

    lista_cod = codigos.split("\n")
    lista_totales = totales.split("\n")
    lista_cod = eliminar_espacios_blanco(lista_cod)
    lista_totales = eliminar_espacios_blanco(lista_totales)
    
    print("########################################################")
    print(proveedor)
    print(lista_cod)
    print(lista_totales)
    print("########################################################")

    for i in range(len(lista_totales)):
        lista_totales[i] = letra_a_numero(lista_totales[i])

    if proveedor:
        identificadores_totales = controlador.identificador_totales(proveedor)
        print(identificadores_totales)
        if identificadores_totales:
            for i in range(len(lista_cod)):
                if identificadores_totales[0][2] in lista_cod[i]:
                    pos_consumo_activa = i
                if lista_cod[i] == identificadores_totales[0][3]:
                    pos_contribucion_activa = i
                if identificadores_totales[0][4] in lista_cod[i]:
                    pos_consumo_reactiva = i
                if identificadores_totales[0][5] in lista_cod[i]:
                    pos_contribucion_reactiva = i

    if pos_consumo_activa != None and lista_totales:
        consumo_activa = lista_totales[pos_consumo_activa]
    else:
        consumo_activa = "0"
    if pos_consumo_reactiva != None and lista_totales:
        consumo_reactiva = lista_totales[pos_consumo_reactiva]
    else:
        consumo_reactiva = "0"
    if pos_contribucion_activa != None and lista_totales:
        contribucion_activa = lista_totales[pos_contribucion_activa]
    else:
        contribucion_activa = "0"
    if pos_contribucion_reactiva != None and lista_totales:
        contribucion_reactiva = lista_totales[pos_contribucion_reactiva]
    else:
        contribucion_reactiva = "0"

    return consumo_activa, consumo_reactiva, contribucion_activa, contribucion_reactiva

def eliminar_espacios_blanco(lista):
    while "" in lista or " " in lista:
        hasta = len(lista)
        for i in range(hasta):
            if lista[i] == '' or lista[i] == ' ':
                lista.pop(i)
                break

    return lista