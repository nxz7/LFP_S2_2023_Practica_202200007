from Producto import cargar_inventario
from movimiento import cargar_movimientos
from Informe import archivo_texto

def mostrar_menu():
    lugar = input("Ingrese la dirección del archivo de inventario: ")
    inventario_inicial = cargar_inventario(lugar)
    mov_archivo = input("Ingrese la dirección del archivo de movimientos: ")

    while True:
        print("\n-----------------------------------")
        print("Práctica 1 - Lenguajes formales y de programación")
        print("-----------------------------------")
        print("SISTEMA DE INVENTARIO:")
        print("1. Cargar inventario inicial")
        print("2. Cargar instrucciones de movimiento")
        print("3. Crear informe de inventario")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            if len(inventario_inicial) == 0:
                print("El inventario está vacío.")
            else:
                for producto in inventario_inicial:
                    print("-----------------------------------------------------------------")
                    print("Nombre:", producto.nombre, "Cantidad:", producto.cantidad, "Precio Unitario:", producto.precio_unitario, "Ubicación:", producto.ubicacion)

        elif opcion == "2":
            if mov_archivo:
                print("Cargando instrucciones de movimiento")
                cargar_movimientos(mov_archivo, inventario_inicial)
                print("----------------INVENTARIO ACTUALIZADO CON LOS MOVIMIENTOS-----------------")
                for producto in inventario_inicial:
                    print("-----------------------------------------------------------------")
                    print("Nombre:", producto.nombre, "Cantidad:", producto.cantidad, "Precio Unitario:", producto.precio_unitario, "Ubicación:", producto.ubicacion)
            else:
                print("ERROR - Cargue primero el inventario inicial antes de las instrucciones de movimiento.")

        elif opcion == "3":
            print("Creando informe de inventario")
            print("INFORME DE INVENTARIO:")
            print("INFORME DESCARGADO CORRECTAMENTE")
            archivo_texto('resultado_202200007.txt', inventario_inicial)
        elif opcion == "4":
            print("Saliendo del sistema")
            break
        else:
            print("ERROR - OPCION INVALIDA")

mostrar_menu()