from Producto import cargar_inventario
from movimiento import cargar_movimientos

lugar = r'C:\Users\natalia\Documents\4sem\lfp\LFP_S2_2023_Practica_202200007\archivo.inv'
inventario_inicial = cargar_inventario(lugar)
mov_archivo = r'C:\Users\natalia\Documents\4sem\lfp\LFP_S2_2023_Practica_202200007\movimientos.mov'

def mostrar_menu():
    global lugar, inventario_inicial, mov_archivo  

    while True:
        print("\n-----------------------------------")
        print("Practica 1 - Lenguajes formales y de programacion")
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
                    print("Nombre:",producto.nombre, "Cantidad:", producto.cantidad, "Precio Unitario:", producto.precio_unitario, "Ubicación:", producto.ubicacion )

        elif opcion == "2":
            if lugar:
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
        elif opcion == "4":
            print("Saliendo del sistema")
            break
        else:
            print("ERROR - OPCION INVALIDA")

mostrar_menu()
