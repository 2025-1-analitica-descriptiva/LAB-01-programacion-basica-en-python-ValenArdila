"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from collections import Counter

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    
    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        meses = []
        for row in reader:
            ano, mes, dia = row[2].split("-")
            meses.append(mes)
        cont = Counter(meses)
        result = sorted(cont.items(), key=lambda x:x[0])
        
    return result


if __name__ == "__main__":
    print(pregunta_04())