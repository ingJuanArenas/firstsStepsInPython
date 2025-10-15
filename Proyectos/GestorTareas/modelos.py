from datetime import datetime

class Tarea:
    def __init__(self, titulo: str, descripcion:str) -> None:
        self.titulo= titulo
        self.descripcion= descripcion
        self.estado= "creada"
        self.fechaCreada= datetime.now()

    @classmethod
    def desde_dict(cls, data: dict):
        obj = cls(data["Nombre"], data["Descripcion"])  # usa el constructor base
        obj.estado = data.get("Estado", "creada")
        obj.fechaCreada = data.get("Fecha")
        return obj


    def __str__(self) -> str:
        return  f""" Fecha: {self.fechaCreada}
                    Nombre: {self.titulo}
                    Descripcion: {self.descripcion}
                    Estado: {self.estado}
                """

