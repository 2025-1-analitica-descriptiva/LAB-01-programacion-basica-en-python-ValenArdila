"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob
import os.path
import string

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('files/input/data.csv', 'r') as f:
        total = 0
        for line in f:
            columns = line.split("\t")
            total += int(columns[1])
    return total
if __name__ == "__main__":
    print(pregunta_01())
    