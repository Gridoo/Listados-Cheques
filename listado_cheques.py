import csv
from datetime import datetime

archivo=input("Ingrese el nombre del archivo: ")
dni=input("Ingrese el DNI: ")
salida=input("Ingrese el tipo de salida (pantalla/csv): ")
tipoCheque=input("Ingrese el tipo de cheque a buscar: ")
resultado=[]
salida=salida.upper()
tipoCheque=tipoCheque.upper()
with open(archivo) as file:
    lector = csv.reader(file, delimiter=";")
    for fila in lector:
        documento=fila[8]
        tipoChequeOriginal=fila[9]
        estadoChequeOriginal=fila[10]
        if documento!=dni or tipoCheque != tipoChequeOriginal:
            continue
        resultado.append(fila)
cantCheques=set()
for fila in resultado:
    documento=fila[8]
    Cheques=fila[0]
    CuentaOrigen=fila[3]
    if (Cheques, CuentaOrigen, documento) in cantCheques:
        resultado.append("Se repite el numero de cheque más de una vez")
    else:
        cantCheques.add((Cheques,CuentaOrigen,documento))
if salida=="PANTALLA":
    for fila in resultado:
        print("Los datos del dni ingresado son: ", documento,"\n ",fila)
#elif salida=="CSV":

