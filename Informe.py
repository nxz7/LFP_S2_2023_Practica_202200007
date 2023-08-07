from Producto import cargar_inventario
from movimiento import cargar_movimientos


def archivo_texto(nombre_ar, inventario):
    with open(nombre_ar, 'w') as archivo:
        archivo.write("PRODUCTO ------- CANTIDAD--------PRECIO UNITARIO-------TOTAL-------UBICACION\n")
        for producto in inventario:
            total = producto.cantidad * producto.precio_unitario
            producto_info = (f"{producto.nombre}-----------{producto.cantidad}------------${producto.precio_unitario}------------${total}---------{producto.ubicacion}\n")
            archivo.write(producto_info)
