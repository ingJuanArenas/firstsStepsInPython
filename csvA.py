import csv
from math import e
from os import write

fields = []
rows = []

try:
    with open("empleados.csv", "r") as datos:
        csvReader = csv.reader(datos)
        fields = next(csvReader)

        for row in csvReader:
            rows.append(row)

        print("Rows : ", csvReader.line_num)
        print("Fields: " , fields)
except FileNotFoundError:
    print("NO se ha encontrado el archivo") 

try:
    with open("empleados.csv", "r") as datos:
        csvReader = csv.DictReader(datos)
        for row in csvReader:
            rows.append(row)

        for row in rows:
            print(row)
except FileNotFoundError:
    print("NO se ha encontrado el archivo") 

fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [
    ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]
try:
    with open("Estudiantes.csv", "w") as estudiantes:
        csvwriter = csv.writer(estudiantes)
        csvFields = csvwriter.writerow(fields)
        csvrows = csvwriter.writerows(rows)
except FileNotFoundError:
    print("NO se ha encontrado el archivo") 


data = [
    {"id": 1, "nombre": "Laura Gómez", "edad": 28, "cargo": "Analista", "salario": 3500000},
    {"id": 2, "nombre": "Carlos Pérez", "edad": 35, "cargo": "Desarrollador", "salario": 5200000},
    {"id": 3, "nombre": "Ana Torres", "edad": 30, "cargo": "Diseñadora", "salario": 4100000},
    {"id": 4, "nombre": "Juan Arenas", "edad": 25, "cargo": "Soporte Técnico", "salario": 2800000},
    {"id": 5, "nombre": "María Rojas", "edad": 40, "cargo": "Gerente", "salario": 7500000}
]
# Definir los nombres de las columnas (las claves del diccionario)
campos = ["id", "nombre", "edad", "cargo", "salario"]


try:
    with open("Estudiantes.csv", "w") as empleados:
        writer = csv.DictWriter(empleados, fieldnames= campos)
        writer.writeheader()
        writer.writerows(data)
except FileNotFoundError:
    print("NO se ha encontrado el archivo") 



mi_coleccion = {1, 'hola', 3, 1, 'hola'}
print(type(mi_coleccion))