from validar_fechas import *

def retornar_totales(proveedor, codigos, totales):
    pos_consumo_activa = None
    pos_contribuciones = None
    pos_consumo_reactiva = None

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

    if proveedor == "eep" or proveedor == "eep_escaner":
        for i in range(len(lista_cod)):
            lista_cod[i] = letra_a_numero(lista_cod[i])

        for i in range(len(lista_cod)):
            if lista_cod[i] == "501":
                pos_consumo_activa = i
            if lista_cod[i] == "511":
                pos_consumo_reactiva = i
            if lista_cod[i] == "551":
                pos_contribuciones = i
    elif proveedor == "dicel":
        for i in range(len(lista_cod)):
            if "Energia Activa" in lista_cod[i]:
                pos_consumo_activa = i
            if "Energia Reactiva" in lista_cod[i]:
                pos_consumo_reactiva = i
            if lista_cod[i] == "Contribucion":
                pos_contribuciones = i

    if pos_consumo_activa != None:
        consumo_activa = lista_totales[pos_consumo_activa]
    else:
        consumo_activa = "0"
    if pos_consumo_reactiva != None:
        consumo_reactiva = lista_totales[pos_consumo_reactiva]
    else:
        consumo_reactiva = "0"
    if pos_contribuciones != None:
        contribuciones = lista_totales[pos_contribuciones]
    else:
        contribuciones = "0"

    return consumo_activa, consumo_reactiva, contribuciones

def eliminar_espacios_blanco(lista):
    while "" in lista or " " in lista:
        hasta = len(lista)
        for i in range(hasta):
            if lista[i] == '' or lista[i] == ' ':
                lista.pop(i)
                break

    return lista