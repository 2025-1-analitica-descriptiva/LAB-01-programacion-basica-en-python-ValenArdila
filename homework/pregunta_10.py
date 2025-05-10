"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        lista = []
        for row in reader:
            col3 = row[3].split(",")
            col4 = row[4].split(",")
            lista.append((row[0], len(col3), len(col4)))
    
    return lista      


if __name__ == "__main__":
    print(pregunta_10())
