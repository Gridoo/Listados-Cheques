import csv
from datetime import datetime


dt= datetime.now()
ts=datetime.timestamp(dt)
#print(dt, ts)
with open("listado.csv") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    type(lector)
    lista=[]
    lista=list(lector)
    NroCheque=[]
    CodigoBanco=[]
    CodigoSucursal=[]
    NumeroCuentaOrigen=[]
    NumeroCuentaDestino=[]
    Valor=[]
    FechaOrigen=[]
    FechaPago=[]
    dni=[]
    Estado=[]
    Tipo=[]
    listaCheques=[]
    listaCuenta=[]
    documento=input("Ingrese su DNI: ") #Ingreso cuenta origen
    for fila in lista:
        NroCheque.append(fila[0])
        CodigoBanco.append(fila[1])
        CodigoSucursal.append(fila[2])
        NumeroCuentaOrigen.append(fila[3])
        NumeroCuentaDestino.append(fila[4])
        Valor.append(fila[5])
        FechaOrigen.append(fila[6])
        FechaPago.append(fila[7])
        dni.append(fila[8])
        Estado.append(fila[9])
        Tipo.append(fila[10])
        if documento in dni:    #ver que no se repita
            CuentasDNI=fila[3]
            listaCuenta.append(CuentasDNI)
            print("La cuenta se encuentra en la base de datos")
            print(listaCuenta) #hasta acá va bien
            ChequesDNI=fila[0]
            listaCheques.append(ChequesDNI)
    for i in listaCuenta:   #ver que no se repita
        if len (listaCheques)==len(set(listaCheques)):
            print("No hay repetidos")
        else:
            print("ERROR, hay cheques repetidos")
    #    if ChequesDNI in listaCheques:

      #      print(listaCheques)

#NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado, Tipo

#ingresa el dni, buscar el numero de cuenta de todos los que coinciden el dni
# fijarse si un numero de cuenta tiene mas de un cheque con mismo numero