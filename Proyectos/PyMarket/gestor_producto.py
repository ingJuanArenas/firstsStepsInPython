from producto import Producto
class Gestor_productos:
    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def mostrar_menu(self):
            print(""" --- GESTIÓN DE PRODUCTOS ---
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Modificar producto
    5. Eliminar producto
    6. Volver al menú principal""")
        
    def pedir_datos(self):
            nombre = input("ingrese el nombre del producto: ")
            categoria= input("Ingrese la categoria del producto: ")
            precio =  int(input("Ingrese el precio: "))
            cantidad =  int(input("Ingrese la canitdad: "))

            while precio <=0 or cantidad <= 0:
                    print("Ha ingresado datos invalidos. Repita el proceso")
                    precio =  int(input("Ingrese el precio: "))
                    cantidad =  int(input("Ingrese la canitdad: "))

            nuevo_producto = Producto(nombre,categoria,precio,cantidad)

            return nuevo_producto


    def agregar_producto(self):
            cantidad_productos = int(input("Ingrese la cantidad de productos: "))
            i=0
            while i<cantidad_productos:
                print(f"Producto {i+1} de {cantidad_productos} ")
                nuevo_producto = self.pedir_datos()
                self.productos.append(nuevo_producto)
                print("Operación exitosa")
                i+=1

    def mostrar_productos(self):
            if len(self.productos) == 0:
                print("La lista está vacia")
            else:
                for producto in self.productos:
                    print("---------------------------------------")
                    print(producto)
                    print("---------------------------------------")

    def buscar_producto(self):
            nombre = input("Ingrese el nombre del producto")
            for p in self.productos:
                if p.nombre == nombre:
                    print(p)
                    return p
            else: 
                print("No hay resultados")
        
    def modificar_producto(self):
            producto= self.buscar_producto()
            if type(producto) == Producto:
                self.productos.remove(producto)
                nuevos_datos= self.pedir_datos()
                producto= nuevos_datos
                print(producto)
                self.productos.append(producto)
            else:
                print("No se encontró el producto")

    def eliminar_producto(self):
            producto = self.buscar_producto()
            productos_actualizado: list[Producto] = []
            if type(producto) == Producto:
                for p in self.productos:
                    if p.nombre == producto.nombre:
                        continue
                    else:
                        productos_actualizado.append(p)
                self.productos = productos_actualizado
                print("Operacion exitosa")
            else:
                print("No se ha encontrado")
