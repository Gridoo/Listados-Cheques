import csv
import sys
from datetime import datetime

parametros = sys.argv[1:]
archivo = parametros[0]
dni = parametros[1]
salida = parametros[2]
tipoCheque = parametros[3]
fecha = None
estado = None
resultado = []

salida = salida.upper()
tipoCheque = tipoCheque.upper()

if len(parametros) == 5:
    opcional = parametros[4]
    estado = ["PENDIENTE", "APROBADO", "RECHAZADO"]
    if opcional in estado:
        estado_filtrado = opcional
    else:
        fecha = opcional.split(':')
        fecha_inicio = datetime.timestamp(
            datetime.strptime(fecha[0], '%d-%m-%Y'))
        fecha_fin = datetime.timestamp(datetime.strptime(fecha[0], '%d-%m-%Y'))
elif len(parametros) == 6:
    estado_filtrado = parametros[4]
    fecha = parametros[5].split(":")
    fecha_inicio = datetime.timestamp(datetime.strptime(fecha[0], '%d-%m-%Y'))
    fecha_fin = datetime.timestamp(datetime.strptime(fecha[0], '%d-%m-%Y'))
with open(archivo) as file:
    lector = csv.reader(file, delimiter=",")
    for fila in lector:
        documento = fila[8]
        tipoChequeOriginal = fila[9]
        estadoChequeOriginal = fila[10]
        fechacsv = float(fila[6])
        if documento != dni or tipoCheque != tipoChequeOriginal:
            continue
        if estado_filtrado and estadoChequeOriginal != estado_filtrado:
            continue
        if fecha and (fechacsv < fecha_inicio or fechacsv > fecha_fin):
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
            filtrado = [[fila[3], fila[5], fila[6], fila[7]]
                        for fila in resultado]
            dt = datetime.now()
            dt = dt.strftime("%d-%m-%Y")
            with open(f'{fila[8]}-{dt}.csv', 'w') as salida:
                writer = csv.writer(salida)
                writer.writerows(filtrado)
