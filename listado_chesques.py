import csv
nombre_archivo = "videojuegos.csv"
with open("listado.csv", "r") as archivo:
    lector = csv.reader(archivo, delimiter=";")
    next(lector, None)
    documento = int(input("Ingrese su documento\n"))
    for fila in lector:
        DNI = int(fila[8])
        estado = fila[9]
        FechaOrigen = fila[6]
        FechaPago = fila[7]
        if documento == DNI:
            NroCheque = int(fila[0])
            for j in lector:
                if NroCheque == int(j[0]):
                    print("hay un cheque repetido con el numero", NroCheque)
                else:
                    print(fila)
