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