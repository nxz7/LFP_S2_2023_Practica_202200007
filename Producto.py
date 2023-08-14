class Producto:
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.ubicacion = ubicacion
    

def cargar_inventario(nombre_ar):
    inventario = []
    with open(nombre_ar, 'r') as archivo:
        for linea in archivo:
            if linea.startswith('crear_producto'):
                instruccion = linea.strip().split(' ')[1].split(';')
                nombre = instruccion[0].strip()
                cantidad = int(instruccion[1].strip())
                precio_unitario = float(instruccion[2].strip())
                ubicacion = instruccion[3].strip()
                producto = Producto(nombre, cantidad, precio_unitario, ubicacion)
                inventario.append(producto)
    return inventario
