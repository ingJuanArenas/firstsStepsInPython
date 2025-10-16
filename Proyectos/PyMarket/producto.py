import random


class Producto:
    def __init__(self, nombre, categoria, precio, cantidad) -> None:
        self.__id= random.randint
        self.nombre= nombre
        self.categoria= categoria
        self.precio= precio if precio>0 else "Precio invalido"
        self.cantidad= cantidad if cantidad > 0 else "Cantidad invalida"

    def __str__(self) -> str:
        return f"""Nombre:  {self.nombre}  Precio: {self.precio}
Categoria:  {self.categoria} Cantidad:  {self.cantidad}"""