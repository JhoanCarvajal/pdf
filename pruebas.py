def numero_decimal(dato):
    if "." in dato and "," in dato:
        puntos = dato.count(".")
        comas = dato.count(",")
        if puntos > comas:
            # "4.523.256,56234"
            dato = dato.replace(',', '\n')
            dato = dato.replace('.', '')
            dato = dato.replace('\n', '.')
            numero = float(dato)
            numero = round(numero, 2)
        else:
            # "4,523,256.56234"
            dato = dato.replace(',', '')
            numero = float(dato)
            numero = round(numero, 2)
    elif "." in dato:
        # "1.234.234"
        puntos = dato.count(".")
        if puntos == 1:
            datos = dato.split(".")
            contador = 0
            for i in datos[1]:
                contador += 1
            if contador == 3:
                numero = dato.replace('.','')
                numero = float(numero)
            else:
                numero = float(dato)
        else:
            dato = dato.replace('.', '')
            numero = float(dato)
            numero = round(numero, 2)
    elif "," in dato:
        # "1,234,567"
        comas = dato.count(",")
        if comas == 1:
            datos = dato.split(",")
            contador = 0
            for i in datos[1]:
                contador += 1
            if contador == 3:
                numero = dato.replace(',','')
                numero = float(numero)
            else:
                numero = dato.replace(',','.')
                numero = float(numero)
        else:
            dato = dato.replace(',', '')
            numero = float(dato)
            numero = round(numero, 2)
    return numero

def numero_entero(dato):
    try:
        if dato:
            if type(dato) == int or type(dato) == float:
                return dato
            else:
                try:
                    numero = float(dato)
                    numero = round(numero, 2)
                    return numero
                except ValueError:
                    try:
                        numero = numero_decimal(dato)
                        return numero
                    except ValueError:
                        # string para almacenar solo numeros
                        numero = ""
                        negativo = False
                        for digito in dato:
                            # print(digito) #mostramos cada digito del string
                            if digito == "B":
                                digito = "8"
                            # si el digito es un numero lo concatenamos con la variable numero
                            if digito.isdigit():
                                numero += str(digito)
                            # si el digito es un - ó ~ el numero es negativo
                            elif digito == "-" or digito =="~":
                                negativo = True
                            elif digito == "." or digito == ",":
                                numero += str(digito)
                        # convertimos el string a float
                        numero = numero_decimal(numero)
                        # miramos si es negativo y lo convertimos
                        if negativo:
                            numero *= -1
                        return numero
        else:
            return 0
    except ValueError:
        pass

print(numero_entero("er431,36-"))