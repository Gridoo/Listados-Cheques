import csv
from datetime import datetime


dt= datetime.now()
ts=datetime.timestamp(dt)
print(dt, ts)
with open("listado.csv") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    type(lector)
    lista=[]
    lista=list(lector)
    #print(lista)
    documento=input("Ingrese su DNI: ")
    for fila in lista:
        NroCheque=fila[0]
        CodigoBanco=fila[1]
        CodigoSucursal=fila[2]
        NumeroCuentaOrigen=fila[3]
        NumeroCuentaDestino=fila[4]
        Valor=fila[5]
        FechaOrigen=fila[6]
        FechaPago=fila[7]
        DNI=fila[8]
        Estado=fila[9]
        Tipo=fila[10]
        int(NroCheque)
        int(CodigoBanco)
        int(CodigoSucursal)
        int(NumeroCuentaOrigen)
        int(NumeroCuentaDestino)
        float(Valor)
        

        if DNI==documento:
            print("El dni se encuentra en la base de datos")
            print(DNI)

#NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado, Tipo
