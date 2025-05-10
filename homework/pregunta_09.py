"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        dic = {}
        for row in reader:
            pares = row[4].split(",")
            for par in pares:
                clave, valor = par.split(":")
                if clave not in dic:
                    dic[clave] = 1
                else:
                    dic[clave]+=1
        
        resultado = dict(sorted(dic.items(), key=lambda x:x[0]))
        
    return resultado
        


if __name__ == "__main__":
    print(pregunta_09())
