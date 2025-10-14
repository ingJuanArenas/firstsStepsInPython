import json

mi_dict = dict({
    "name": "juan",
    "Gatos": 3,
    "Clima": "Lluvia"
})

mi_list = list(["item 1", 2, 3 ,"Numeros", "Letreas"])
try: 
    with open("Datos.json", "w") as d:
        d.write(json.dumps(mi_dict))
except FileNotFoundError:
    print("No se ha encontrado el archivo")
finally: 
    print("Operacion terminada")




try:
    with open("Datos.json","r") as d:
        print(d.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
