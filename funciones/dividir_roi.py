def dividir(roi):
    rows,cols = roi.shape
    mitad = cols / 2
    mitad = int(mitad)
    fecha_inicio = roi[0:rows,0:mitad-10]
    fecha_final = roi[0:rows,mitad+4:cols]

    return fecha_inicio, fecha_final
    
