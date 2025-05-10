"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    
    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        dic = {}
        for row in reader:
            pares = row[4].split(",")
            for par in pares:
                letra, num = par.split(":") 
                if row[0] not in dic:
                    dic[row[0]] = 0
                dic[row[0]]+=int(num)
        result = dict(sorted(dic.items(), key=lambda x:x[0]))
            
    
    return result      


if __name__ == "__main__":
    print(pregunta_12())
