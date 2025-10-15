import json
import os
from xml.dom import NotFoundErr
from modelos import Tarea
class Gestor:
    def __init__(self) -> None:
        self.tareas: list[Tarea] = []
        if os.path.exists("Tareas.json"):
            try:
                with open("Tareas.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tareas = [Tarea.desde_dict(d) for d in data]
            except Exception as e:
                print("Ha ocurrido un error ", e)
    def mostrar_menu(self):
        print("Bienvenido al gestor de tareas")
        print(" 1. Ver tareas")
        print(" 2. Agregar tarea")
        print(" 3. Modificar estado")
        print(" 4. Eliminar tarea")
        print(" 5. Guardar ")
        print(" 0. Salir")

    def ver_tareas(self):
        if len(self.tareas) == 0 : 
            print("La lista esta vacia")
        else: 
            for x in self.tareas:
                print(x)

    def agregar_tarea(self):
        i=0
        cantidad = int(input("Ingrese la cantidad de tareas a agregar: "))
        assert cantidad> 0, "Ingrese un numero mayor a cero"

        while i< cantidad:
            nombre = input("Ingrese el nombre de la tarea: ")
            desc= input("Ingrese la descripcion de la tarea: ")
            nueva_tarea= Tarea(nombre,desc)
            self.tareas.append(nueva_tarea)
            i+=1
        print("Operación exitosa")


    def cambiar_estado(self):
        nombre = input("Ingrese el nombre de la tarea: ")
        for tarea in self.tareas:
            if tarea.titulo == nombre:
                tarea_cambiar = tarea
                nuevo_estado= input("Ingrese el nuevo estado (En proceso / finalizado): ")
                tarea_cambiar.estado= nuevo_estado
                print(tarea_cambiar)
                break
        else: 
            raise NotFoundErr("No se ha encontrado la tarea")

    def eliminar_tarea(self):
        nombre = input("Ingrese el nombre de la tarea: ")
        for x in self.tareas:
            if x.titulo == nombre:
                self.tareas.remove(x)
                print("Operación exitosa")

                break
        else: 
            raise NotFoundErr("No se ha encontrado la tarea")    
    def guardar(self):
        tareas_json = []
        for x in self.tareas:
            tarea = {
                        "Nombre" : x.titulo,
                        "Estado" : x.estado,
                        "Fecha" : str(x.fechaCreada),
                        "Descripcion" : x.descripcion
                    }

            tareas_json.append(tarea)

        with open("Tareas.json", "w", encoding="utf-8") as f:
            json.dump(tareas_json,f, indent=4, ensure_ascii=False)
            print("Tareas almacenadas exitosamente!!")