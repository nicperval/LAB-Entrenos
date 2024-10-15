import csv

from datetime import datetime
from collections import namedtuple
def lee_entrenos(ruta):
    with open(ruta, encoding='utf-8') as f:
        fichero = csv.reader(f)
        next(fichero)
        lista = []
        Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in fichero:
            fechahora = datetime.strptime(fechahora,'%d/%m/%Y %H:%M')
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = bool(compartido)
            Entreno = (tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido)
            lista.append(Entreno)
        return lista

def tipos_entreno(lista):
    nombres = []
    for Entreno in lista:
        if Entreno[0] not in nombres:
            nombres.append(Entreno[0])
    print(sorted(nombres))

def entrenos_duracion_superior(lista,d):
    entrenos_largos = []
    for Entreno in lista:
        if Entreno[3] > d:
            entrenos_largos.append(Entreno[4])
    print(entrenos_largos)

def suma_calorias(lista,f_inicio,f_fin):
    suma = 0
    f_inicio = datetime.strptime(f_inicio,'%d/%m/%Y')
    f_fin = datetime.strptime(f_fin,'%d/%m/%Y')
    for Entreno in lista:
        if Entreno[1] > f_inicio:
            if Entreno[1] < f_fin:
                suma = suma + Entreno[4]
    print(suma)