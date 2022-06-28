import csv
nombre_archivo = "videojuegos.csv"
with open("listado.csv", "r") as archivo:
    lector = csv.reader(archivo, delimiter=";")
    next(lector, None)
    documento = int(input("Ingrese su documento"))
    for fila in lector:
        DNI = int(fila[8])
        estado = fila[9]
        if documento == DNI:
            print(f"El DNI: '{DNI}' Tiene su cheque en estado: '{estado}'")
