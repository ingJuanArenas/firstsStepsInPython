from gestor import Gestor



gestor = Gestor()


while True: 
    try:
        gestor.mostrar_menu()
        opcion = int(input("Ingresa la opcion: "))
        match opcion:
            case 1:
                gestor.ver_tareas()
            case 2: 
                gestor.agregar_tarea()
            case 3:
                gestor.cambiar_estado()
            case 4: 
                gestor.eliminar_tarea()
            case 5:
                gestor.guardar()
            case 0: 
                break
            case _: 
                print("Opcion invalida")
    except ValueError as e:
        print("Ha ocurrido un error: " , e)
        