"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    
    with open('files/input/data.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        dic = {}
        for row in reader:
            if row[0] not in dic:
                dic[row[0]] = [row[1]]
            else:
                dic[row[0]].append(row[1])
        
        resultado = [(letra, int(max(numeros)), int(min(numeros))) for letra, numeros in dic.items()]
        resultado = sorted(resultado, key=lambda x:x[0])
        
            
        return resultado
            
        
    


if __name__ == "__main__":
    print(pregunta_05())
