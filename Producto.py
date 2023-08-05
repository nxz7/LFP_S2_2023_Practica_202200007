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
                instruccion = linea.strip().split(';')
                nombre = instruccion[1].strip()
                cantidad = int(instruccion[2].strip())  
                precio_unitario = float(instruccion[3].strip())  
                ubicacion = instruccion[4].strip()
                producto = Producto(nombre, cantidad, precio_unitario, ubicacion)
                inventario.append(producto)
    return inventario

#lugar= r'C:\Users\natalia\Documents\archivo.inv'

#inventario_inicial = cargar_inventario(lugar)

#if len(inventario_inicial) == 0:
    #print("El inventario está vacío.")
#else:
    #for producto in inventario_inicial:
        #print("-----------------------------------------------------------------")
        #print("Nombre:",producto.nombre, "Cantidad:", producto.cantidad, "Precio Unitario:", producto.precio_unitario, "Ubicación:", producto.ubicacion )
