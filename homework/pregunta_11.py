"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        dic = {}
        for row in reader:
            claves = row[3].split(",")
            valor = int(row[1])
            for clave in claves:
                if clave not in dic:
                    dic[clave] = 0
                dic[clave]+=valor
        result = dict(sorted(dic.items(), key=lambda x:x[0]))
    
    return result


if __name__ == "__main__":
    print(pregunta_11())
