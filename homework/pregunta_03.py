"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        dic = {}
        for row in reader:
            if row[0] not in dic:
                dic[row[0]] = 0 
            dic[row[0]] += int(row[1])
        result = sorted(dic.items(), key= lambda x:x[0])
        
    
    return result      


if __name__ == "__main__":
    pregunta_03()

    
