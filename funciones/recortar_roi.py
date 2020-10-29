def recortar(rows,cols,roi_fechas):
    print(rows,cols)
    k = []
    y = 0
    x = 0
    for i in range(rows):
        cont = 0
        for j in range(cols):
            if roi_fechas[i,j] != 255:
                cont +=1
        if cont > 3:
            y = i-5
            break
    print(y)
    for i in range(cols):
        cont = 0
        for j in range(rows):
            if roi_fechas[j,i] != 255:
                cont +=1
        if cont > 3:
            x = i-5
            break
    print(x)
    y1 = 0
    x1 = 0
    for i in range(rows-1,0,-1):
        cont = 0
        for j in range(cols-1,0,-1):
            if roi_fechas[i,j] != 255:
                cont +=1
        if cont > 3:
            y1 = i+5
            break
    print(y1)
    for i in range(cols-1,0,-1):
        cont = 0
        for j in range(rows-1,0,-1):
            if roi_fechas[j,i] != 255:
                cont +=1
        if cont > 3:
            x1 = i+8
            break
    print(x1)

    roi_fechas_nuevo = roi_fechas[y:y1,x:x1]
    return roi_fechas_nuevo