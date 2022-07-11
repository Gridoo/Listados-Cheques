import csv
import sys
from datetime import datetime

parametros = sys.argv[1:]
archivo = parametros[0]
#archivo = input("Ingrese el nombre del archivo: ")
dni = parametros[1]
#dni = input("Ingrese el DNI: ")
salida = parametros[2]
#salida = input("Ingrese el tipo de salida (pantalla/csv): ")
tipoCheque = parametros[3]
#tipoCheque = input("Ingrese el tipo de cheque a buscar: ")
resultado = []
salida = salida.upper()
tipoCheque = tipoCheque.upper()
with open(archivo) as file:
    lector = csv.reader(file, delimiter=",")
    for fila in lector:
        documento = fila[8]
        tipoChequeOriginal = fila[9]
        estadoChequeOriginal = fila[10]
        if documento != dni or tipoCheque != tipoChequeOriginal:
            continue
        resultado.append(fila)
cantCheques = set()
for fila in resultado:
    documento = fila[8]
    Cheques = fila[0]
    CuentaOrigen = fila[3]
    if (Cheques, CuentaOrigen, documento) in cantCheques:
        resultado.append("Se repite el numero de cheque más de una vez")
    else:
        cantCheques.add((Cheques, CuentaOrigen, documento))
        if salida == "PANTALLA":
            for fila in resultado:
                print("Los datos del dni ingresado son: ",
                      documento, "\n ", fila)
        elif salida == "CSV":
            filtrado = [fila[3], fila[5], fila[6], fila[7]]
            dt = datetime.now()
            dt = dt.strftime("%d-%m-%Y")
            with open(f'{fila[8]}-{dt}.csv', 'w') as salida:
                writer = csv.writer(salida)
                writer.writerows(filtrado)
