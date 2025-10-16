from gestor_producto import Gestor_productos

def mostrar_productos_menu():
    try:
        gestor= Gestor_productos()
        while True:
            gestor.mostrar_menu()
            opcion= int(input("Ingrese la opcion:  "))
            match opcion:
                case 1:
                    gestor.agregar_producto()
                case 2: 
                    gestor.mostrar_productos()
                case 3: 
                    gestor.buscar_producto()
                case 4:
                    gestor.modificar_producto()
                case 5:
                    gestor.eliminar_producto()
                case 6:
                    print("Regresando.... ")
                    break
                case _:
                    print("Opción invalida")
    except ValueError as e:
        print("Tipo de dato incorrecto : ", e) 