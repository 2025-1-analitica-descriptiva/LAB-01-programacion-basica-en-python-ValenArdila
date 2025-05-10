"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    
    with open('files/input/data.csv', 'r') as f:
        lista = []
        for line in f:
            columns = line.split("\t")
            lista.append(columns[0])
        contados = dict(zip(lista,map(lambda x: lista.count(x),lista)))
        contados = dict(sorted(contados.items(), key=lambda x: x[0]))
        contados = list(contados.items())
    return contados
if __name__ == "__main__":
    pregunta_02()



'''
Otras formas de resolver el problema:
import csv
from collections import Counter

with open('files/input/data.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    lista = [row[0] for row in reader]

contados = sorted(Counter(lista).items())
'''