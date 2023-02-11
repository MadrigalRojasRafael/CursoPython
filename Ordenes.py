#CLASE ORDENES:
# + Contador de ordenes → Variable de Clase
# - ID orden → int
# - productos → list
# Método __str__()

from Productos import *

class Ordenes:

    #Variable de Clase para el Contador de Ordenes → contador_ordenes:
    contador_ordenes = 0

    #Método __init__() para poder crear los Objetos:
    def __init__(self, productos):
        Ordenes.contador_ordenes += 1
        self.id_orden = Ordenes.contador_ordenes
        self._productos = list(productos)

    #Método addProductos para agregar productos a la orden:
    def addProductos(self, producto):
        self._productos.append(producto)

    #Método totalOrden para saber el precio total de todos los productos de la orden:
    def totalOrden(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return f"Total: {total}"

    #Método __str__() para visualizar la información del Objeto:
    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "\n"
        return f"Orden: {self.id_orden}\nProductos:\n{productos_str}"