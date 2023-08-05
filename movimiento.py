from Producto_mov import Producto_mov
# HAY UN LOOP ACAAAA 
def cargar_movimientos(nombre_ar, inventario):
    movimientos = []
    with open(nombre_ar, 'r') as archivo:
        for linea in archivo:
            if linea.startswith("agregar_stock"):
                instruccion = linea.strip().split(' ')
                producto_info = instruccion[1].strip().split(';')
                nombre = producto_info[0].strip()
                cantidad_agregada_str = producto_info[1].strip()
                ubicacion = producto_info[2].strip()
                try:
                    cantidad_agregada = int(cantidad_agregada_str)
                except ValueError:
                    print("error en cantidad")
                    continue

                for producto in inventario:
                    if producto.nombre == nombre and producto.ubicacion == ubicacion:
                        producto.cantidad= producto.cantidad+cantidad_agregada
                        
                        break
                    else:
                        print("No se encontró el producto",nombre, "en la bodega:",ubicacion)

            elif linea.startswith("vender_producto"):
                instruccion = linea.strip().split(' ')
                producto_info = instruccion[1].strip().split(';')
                nombre = producto_info[0].strip()
                cantidad_vendida_str = producto_info[1].strip()
                ubicacion = producto_info[2].strip()
                try:
                    cantidad_vendida = int(cantidad_vendida_str)
                except ValueError:
                    print("error en cantidad")
                    continue

                for producto in inventario:
                    if producto.nombre == nombre and producto.ubicacion == ubicacion:
                        producto.cantidad= producto.cantidad-cantidad_vendida

                        break
                    else:
                        print("No se encontró el producto ",nombre, "en la bodega:",ubicacion)
            else:
                print("--")

    return movimientos
