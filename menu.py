from Producto import cargar_inventario

def mostrar_menu():
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
            print("Cargando inventario inicial")
            lugar = r'C:\Users\natalia\Documents\archivo.inv'
            inventario_inicial = cargar_inventario(lugar)
            if len(inventario_inicial) == 0:
                print("El inventario está vacío.")
            else:
                for producto in inventario_inicial:
                    print("-----------------------------------------------------------------")
                    print("Nombre:",producto.nombre, "Cantidad:", producto.cantidad, "Precio Unitario:", producto.precio_unitario, "Ubicación:", producto.ubicacion )

        elif opcion == "2":
            print("Cargando instrucciones de movimiento")
        elif opcion == "3":
            print("Creando informe de inventario")
        elif opcion == "4":
            print("Saliendo del sistema")
            break
        else:
            print("ERROR - OPCION INVALIDA")

mostrar_menu()